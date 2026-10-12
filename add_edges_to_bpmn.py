import xml.etree.ElementTree as ET
import os

def process_bpmn(file_path):
    print(f"Processing: {file_path}")
    tree = ET.parse(file_path)
    root = tree.getroot()

    ns = {
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        'bpmndi': 'http://www.omg.org/spec/BPMN/20100524/DI',
        'dc': 'http://www.omg.org/spec/DD/20100524/DC',
        'di': 'http://www.omg.org/spec/DD/20100524/DI'
    }

    # Register namespaces so they don't get ns0 prefixes
    ET.register_namespace('', 'http://www.omg.org/spec/BPMN/20100524/MODEL')
    ET.register_namespace('bpmndi', 'http://www.omg.org/spec/BPMN/20100524/DI')
    ET.register_namespace('dc', 'http://www.omg.org/spec/DD/20100524/DC')
    ET.register_namespace('di', 'http://www.omg.org/spec/DD/20100524/DI')
    ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')

    plane = root.find('.//bpmndi:BPMNPlane', ns)
    if plane is None:
        print("Error: No BPMNPlane found!")
        return

    # Find existing edges
    existing_edges = set()
    for edge in plane.findall('bpmndi:BPMNEdge', ns):
        existing_edges.add(edge.get('bpmnElement'))

    # Collect shape bounds
    shapes = {}
    for s in plane.findall('bpmndi:BPMNShape', ns):
        el_id = s.get('bpmnElement')
        bounds = s.find('dc:Bounds', ns)
        if bounds is not None:
            shapes[el_id] = {
                'x': int(round(float(bounds.get('x')))),
                'y': int(round(float(bounds.get('y')))),
                'w': int(round(float(bounds.get('width')))),
                'h': int(round(float(bounds.get('height'))))
            }

    # Find all sequence flows
    seq_flows = root.findall('.//bpmn:sequenceFlow', ns)
    added_count = 0

    for sf in seq_flows:
        sf_id = sf.get('id')
        src_id = sf.get('sourceRef')
        tgt_id = sf.get('targetRef')

        if sf_id in existing_edges:
            continue

        if src_id not in shapes or tgt_id not in shapes:
            print(f"Warning: Missing shape for flow {sf_id} ({src_id} -> {tgt_id})")
            continue

        s = shapes[src_id]
        t = shapes[tgt_id]

        sx, sy, sw, sh = s['x'], s['y'], s['w'], s['h']
        tx, ty, tw, th = t['x'], t['y'], t['w'], t['h']

        scx = sx + sw // 2
        scy = sy + sh // 2
        tcx = tx + tw // 2
        tcy = ty + th // 2

        waypoints = []

        # Check if source is a boundary event
        is_boundary = 'Boundary' in src_id

        # Loop back condition (target is to the left of source)
        if tx + tw < sx:
            # Loop back flow
            if is_boundary:
                # Boundary event loop
                start_x, start_y = scx, sy + sh
                bottom_y = max(sy + sh, ty + th) + 40
                waypoints = [
                    (start_x, start_y),
                    (start_x, bottom_y),
                    (tcx, bottom_y),
                    (tcx, ty + th)
                ]
            else:
                # Decide whether to loop via top or bottom
                if tcy <= scy:
                    top_y = min(sy, ty) - 45
                    waypoints = [
                        (scx, sy),
                        (scx, top_y),
                        (tcx, top_y),
                        (tcx, ty)
                    ]
                else:
                    bot_y = max(sy + sh, ty + th) + 45
                    waypoints = [
                        (scx, sy + sh),
                        (scx, bot_y),
                        (tcx, bot_y),
                        (tcx, ty + th)
                    ]

        # Target is strictly or roughly below source
        elif abs(scx - tcx) <= max(sw, tw) // 2 and ty >= sy + sh - 5:
            if abs(scx - tcx) <= 8:
                waypoints = [
                    (scx, sy + sh),
                    (tcx, ty)
                ]
            else:
                mid_y = (sy + sh + ty) // 2
                waypoints = [
                    (scx, sy + sh),
                    (scx, mid_y),
                    (tcx, mid_y),
                    (tcx, ty)
                ]

        # Target is strictly or roughly above source
        elif abs(scx - tcx) <= max(sw, tw) // 2 and sy >= ty + th - 5:
            if abs(scx - tcx) <= 8:
                waypoints = [
                    (scx, sy),
                    (tcx, ty + th)
                ]
            else:
                mid_y = (sy + ty + th) // 2
                waypoints = [
                    (scx, sy),
                    (scx, mid_y),
                    (tcx, mid_y),
                    (tcx, ty + th)
                ]

        # Target is to the right (standard forward flow)
        else:
            if is_boundary:
                # From boundary event
                start_x = scx
                start_y = sy + sh
                if abs(start_y - tcy) <= 10:
                    waypoints = [
                        (sx + sw, scy),
                        (tx, tcy)
                    ]
                else:
                    mid_x = (start_x + tx) // 2
                    waypoints = [
                        (start_x, start_y),
                        (start_x, tcy),
                        (tx, tcy)
                    ]
            else:
                # From normal task / gateway / event
                start_x = sx + sw
                start_y = scy
                end_x = tx
                end_y = tcy

                if abs(start_y - end_y) <= 8:
                    # Same horizontal line
                    waypoints = [
                        (start_x, start_y),
                        (end_x, end_y)
                    ]
                else:
                    # Orthogonal bend
                    mid_x = (start_x + end_x) // 2
                    waypoints = [
                        (start_x, start_y),
                        (mid_x, start_y),
                        (mid_x, end_y),
                        (end_x, end_y)
                    ]

        # Create BPMNEdge element
        edge_elem = ET.Element('{http://www.omg.org/spec/BPMN/20100524/DI}BPMNEdge', {
            'id': f'BPMNEdge_{sf_id}',
            'bpmnElement': sf_id
        })

        for wx, wy in waypoints:
            wp = ET.SubElement(edge_elem, '{http://www.omg.org/spec/DD/20100524/DI}waypoint', {
                'x': str(wx),
                'y': str(wy)
            })

        # If sequence flow has a name/label, add BPMNLabel
        sf_name = sf.get('name')
        if sf_name and len(waypoints) >= 2:
            # Place label near midpoint
            mid_wp_idx = len(waypoints) // 2
            lx = (waypoints[mid_wp_idx - 1][0] + waypoints[mid_wp_idx][0]) // 2 - 20
            ly = (waypoints[mid_wp_idx - 1][1] + waypoints[mid_wp_idx][1]) // 2 - 18
            lbl = ET.SubElement(edge_elem, '{http://www.omg.org/spec/BPMN/20100524/DI}BPMNLabel')
            ET.SubElement(lbl, '{http://www.omg.org/spec/DD/20100524/DC}Bounds', {
                'x': str(lx),
                'y': str(ly),
                'width': '60',
                'height': '14'
            })

        plane.append(edge_elem)
        added_count += 1

    print(f"Added {added_count} BPMNEdge elements to {file_path}")
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    for f in [
        r"d:\BPMN\October\BPMN_Assignment_3\Assignment3_BPMN_Diagram.bpmn",
        r"d:\BPMN\October\Final_Submission\Assignment3_BPMN_Diagram.bpmn",
        r"d:\BPMN\October\BPMN_Assignment_2\Assignment2_BPMN_Diagram.bpmn",
        r"d:\BPMN\October\Final_Submission\Assignment2_BPMN_Diagram.bpmn"
    ]:
        if os.path.exists(f):
            process_bpmn(f)
