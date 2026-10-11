import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # Blank slide

    # Theme Colors
    BG_DARK = RGBColor(11, 25, 44)        # Deep Navy #0B192C
    BG_CARD = RGBColor(24, 38, 62)        # Slate Navy Card #18263E
    BG_CARD_ALT = RGBColor(30, 48, 80)    # Slightly lighter card
    BORDER_CARD = RGBColor(45, 68, 102)   # Card border #2D4466
    TEXT_WHITE = RGBColor(248, 250, 252)  # Bright White #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)  # Muted Slate #94A3B8
    CYAN_ACCENT = RGBColor(0, 210, 235)   # Cyan #00D2EB
    BLUE_ACCENT = RGBColor(96, 165, 250)  # Bright Blue #60A5FA
    GREEN_ACCENT = RGBColor(52, 211, 153) # Emerald #34D399
    AMBER_ACCENT = RGBColor(251, 146, 60) # Amber #FB923C
    RED_ACCENT = RGBColor(248, 113, 113)  # Coral Red #F87171
    PURPLE_ACCENT = RGBColor(192, 132, 252) # Soft Purple #C084FC

    def apply_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_badge="BPMN 2.0 ACADEMIC PRESENTATION"):
        # Category badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(3.4), Inches(0.32))
        badge.fill.solid()
        badge.fill.fore_color.rgb = BG_CARD
        badge.line.color.rgb = CYAN_ACCENT
        badge.line.width = Pt(1)
        tf = badge.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = category_badge
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

        # Slide Title
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.78), Inches(11.7), Inches(0.65))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Arial"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

    def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=BORDER_CARD, radius=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # ==========================================================
    # SLIDE 1: Title Slide
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s1)

    # Decorative header element
    dec = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(1.2), Inches(0.08))
    dec.fill.solid()
    dec.fill.fore_color.rgb = CYAN_ACCENT
    dec.line.fill.background()

    # Title & Subtitle Box
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(2.2))
    tf = t_box.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = "Loan Origination & Approval System"
    p0.font.name = "Arial"
    p0.font.size = Pt(36)
    p0.font.bold = True
    p0.font.color.rgb = TEXT_WHITE
    p0.space_after = Pt(10)

    p1 = tf.add_paragraph()
    p1.text = "Enterprise BPMN 2.0 Process Modelling, Concurrency & Exception Architecture"
    p1.font.name = "Arial"
    p1.font.size = Pt(18)
    p1.font.color.rgb = CYAN_ACCENT

    # Student & Institutional Meta Cards
    c1 = add_card(s1, Inches(0.8), Inches(3.7), Inches(5.6), Inches(2.8), BG_CARD, BORDER_CARD)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "CANDIDATE INFORMATION"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(14)

    fields1 = [
        ("Student Name:", "Mayank Singh"),
        ("Registration Number:", "RA2411003010116"),
        ("Course / Subject:", "Workflow Automation"),
        ("Academic Institution:", "SRMIST"),
    ]
    for lbl, val in fields1:
        p_row = tf1.add_paragraph()
        p_row.space_after = Pt(8)
        run_lbl = p_row.add_run()
        run_lbl.text = f"{lbl}  "
        run_lbl.font.bold = True
        run_lbl.font.size = Pt(12)
        run_lbl.font.color.rgb = TEXT_MUTED
        run_val = p_row.add_run()
        run_val.text = val
        run_val.font.bold = True
        run_val.font.size = Pt(13)
        run_val.font.color.rgb = TEXT_WHITE

    # Project Scope & Architecture Meta Card
    c2 = add_card(s1, Inches(6.8), Inches(3.7), Inches(5.7), Inches(2.8), BG_CARD, BORDER_CARD)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "MODELLING SPECIFICATION & SCOPE"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p.space_after = Pt(14)

    fields2 = [
        ("Specification Standard:", "OMG BPMN 2.0 (XML & Graphical Notation)"),
        ("Architectural Scope:", "7 Lanes (6 Internal + 1 External Pool)"),
        ("Execution Integrity:", "Parallel Gateway Concurrency & Error Boundaries"),
        ("Validation Status:", "Validated on Camunda Modeler 5.49 & bpmn-js"),
    ]
    for lbl, val in fields2:
        p_row = tf2.add_paragraph()
        p_row.space_after = Pt(8)
        run_lbl = p_row.add_run()
        run_lbl.text = f"{lbl}  "
        run_lbl.font.bold = True
        run_lbl.font.size = Pt(12)
        run_lbl.font.color.rgb = TEXT_MUTED
        run_val = p_row.add_run()
        run_val.text = val
        run_val.font.size = Pt(12)
        run_val.font.color.rgb = TEXT_WHITE

    s1.notes_slide.notes_text_frame.text = (
        "Good morning Professor and classmates. My name is Mayank Singh, registration number RA2411003010116, "
        "presenting our academic project for the Workflow Automation course at SRMIST. "
        "Today, I will walk you through our comprehensive BPMN 2.0 process model for the Loan Origination and Approval System. "
        "In enterprise banking, loan origination is one of the most critical and complex workflows because it balances customer satisfaction, "
        "strict regulatory compliance like KYC and AML, and credit risk control. Rather than modelling a naive 'happy path', our model captures "
        "the full end-to-end reality: deterministic concurrency using Parallel Gateways, asynchronous collaboration with external credit bureaus, "
        "and 12 granular failure paths with robust boundary event handling. Let us begin by examining the core problem and objectives."
    )

    # ==========================================================
    # SLIDE 2: Problem Statement and Objectives
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s2)
    add_header(s2, "Problem Statement & Process Objectives", "PROJECT CONTEXT")

    # Left Column: Problem & Motivation (5.7 in)
    c_prob = add_card(s2, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3), BG_CARD, BORDER_CARD)
    tf = c_prob.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "THE REAL-WORLD BANKING CHALLENGE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RED_ACCENT
    p.space_after = Pt(10)

    prob_bullets = [
        ("High Drop-off & Documentation Latency: ", "Retail loan applicants face long cycle times due to repeated missing document exchanges and lack of automated validation schemas."),
        ("Multi-Departmental Silos: ", "Underwriters, compliance teams, loan officers, and core banking operations frequently communicate through unstructured channels, causing compliance blindspots."),
        ("Strict Regulatory Mandates: ", "Zero-tolerance requirements for KYC identity matching and AML watchlist screening necessitate deterministic, auditable gatekeeping before loan commitment."),
        ("External Dependency Fragility: ", "Credit bureau APIs frequently experience network timeouts, requiring structured non-blocking retry mechanisms rather than stalling the application."),
    ]
    for b_title, b_desc in prob_bullets:
        bp = tf.add_paragraph()
        bp.space_after = Pt(10)
        r1 = bp.add_run()
        r1.text = "• " + b_title
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = TEXT_WHITE
        r2 = bp.add_run()
        r2.text = b_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    # Right Column: Process Objectives & Why BPMN (5.7 in)
    c_obj = add_card(s2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.6), BG_CARD, BORDER_CARD)
    tf_obj = c_obj.text_frame
    tf_obj.word_wrap = True
    p = tf_obj.paragraphs[0]
    p.text = "PROCESS DESIGN OBJECTIVES"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    objs = [
        "1. Model End-to-End Orchestration: From applicant document submission to NEFT/RTGS disbursement.",
        "2. Parallelize Background Checks: Execute KYC/AML, Credit Bureau scoring, and DTI ratio checks simultaneously.",
        "3. Resilient Failure Containment: Provide explicit recovery or terminal paths for all 12 potential failure triggers.",
        "4. Enforce SLA Compliance: Introduce timer-based offer expirations and non-blocking e-signature follow-ups.",
    ]
    for o in objs:
        op = tf_obj.add_paragraph()
        op.space_after = Pt(6)
        op.text = o
        op.font.size = Pt(11)
        op.font.color.rgb = TEXT_WHITE

    c_bpmn = add_card(s2, Inches(6.8), Inches(4.35), Inches(5.7), Inches(2.55), BG_CARD, BORDER_CARD)
    tf_bpmn = c_bpmn.text_frame
    tf_bpmn.word_wrap = True
    p = tf_bpmn.paragraphs[0]
    p.text = "WHY BPMN 2.0 IS THE SUPERIOR MODELLING STANDARD"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    bpmn_reasons = [
        ("Standardized Semantics: ", "Unlike basic flowcharts, BPMN 2.0 distinguishes User, Service, and Send tasks with unambiguous execution semantics."),
        ("Pools vs Lanes Rigor: ", "Enforces strict organizational boundary isolation (Sequence Flows strictly within a Pool; Message Flows between Pools)."),
        ("Event-Driven Architecture: ", "Supports interrupting and non-interrupting boundary events essential for enterprise timeout and technical fault trapping."),
    ]
    for r_title, r_desc in bpmn_reasons:
        rp = tf_bpmn.add_paragraph()
        rp.space_after = Pt(6)
        r1 = rp.add_run()
        r1.text = "✔ " + r_title
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = rp.add_run()
        r2.text = r_desc
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    s2.notes_slide.notes_text_frame.text = (
        "On Slide 2, we define the real-world operational problem. In retail banking, loan applications frequently suffer from high abandonment rates "
        "and multi-week processing delays. When loan officers rely on email chains and manual handoffs, compliance violations occur, and applications "
        "stall silently when external credit agencies fail to respond. "
        "Our objective in this project is to model a rigorous, production-grade automated process. We divide the work across six internal departments "
        "and one external partner. We chose BPMN 2.0 over traditional UML activity diagrams or flowcharts because BPMN provides formal execution semantics: "
        "it explicitly defines who does what via swimlanes, prevents deadlock using synchronized gateways, and handles asynchronous timeouts via boundary events."
    )

    # ==========================================================
    # SLIDE 3: Overall BPMN Process
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s3)
    add_header(s3, "Overall BPMN 2.0 Architecture & Process Topology", "SYSTEM ARCHITECTURE")

    # Diagram preview card on Left (7.8 inches)
    c_diag = add_card(s3, Inches(0.8), Inches(1.5), Inches(7.8), Inches(5.4), BG_CARD, BORDER_CARD)
    img_path = r"d:\BPMN\October\BPMN_Assignment_3\Assignment3_BPMN_Diagram.png"
    if os.path.exists(img_path):
        s3.shapes.add_picture(img_path, Inches(0.9), Inches(1.6), Inches(7.6), Inches(5.2))

    # Architecture Breakdown Cards on Right (4.0 inches)
    c_part = add_card(s3, Inches(8.8), Inches(1.5), Inches(3.7), Inches(2.6), BG_CARD, BORDER_CARD)
    tf_p = c_part.text_frame
    tf_p.word_wrap = True
    p = tf_p.paragraphs[0]
    p.text = "PARTICIPANTS & SWIMLANES (7 TOTAL)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    lanes = [
        ("Applicant: ", "Submits docs, reviews offer, e-signs agreement"),
        ("Loan Officer: ", "Screens docs, verifies income, issues offers"),
        ("Underwriter: ", "Adjudicates borderline risks & collateral LTV"),
        ("Compliance Team: ", "Manual KYC adjudication & AML fraud probes"),
        ("Core Banking: ", "Parallel execution, scoring, DTI computation"),
        ("Operations: ", "Disbursement prep & manual fallback channels"),
        ("Credit Bureau (Pool): ", "External partner exchanging message flows"),
    ]
    for l_title, l_desc in lanes:
        lp = tf_p.add_paragraph()
        lp.space_after = Pt(3)
        r1 = lp.add_run()
        r1.text = "• " + l_title
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = lp.add_run()
        r2.text = l_desc
        r2.font.size = Pt(9)
        r2.font.color.rgb = TEXT_MUTED

    c_bounds = add_card(s3, Inches(8.8), Inches(4.25), Inches(3.7), Inches(2.65), BG_CARD, BORDER_CARD)
    tf_b = c_bounds.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.text = "PROCESS BOUNDARIES & METRICS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    metrics = [
        ("Start Event: ", "Applicant submits online application & docs"),
        ("Happy End Event: ", "Loan Disbursed & Account Created (Success)"),
        ("Failure End States (6): ", "Rejected, Withdrawn, Lapsed, Expired, Fraud Terminated, Disbursement Failed"),
        ("Construct Inventory: ", "28 Total Flow Nodes, 13 Gateways, 4 Boundary Events, 2 Message Flows"),
        ("Schema Conformance: ", "100% Valid BPMN 2.0 XML (Camunda tested)"),
    ]
    for m_title, m_desc in metrics:
        mp = tf_b.add_paragraph()
        mp.space_after = Pt(4)
        r1 = mp.add_run()
        r1.text = "✔ " + m_title
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = mp.add_run()
        r2.text = m_desc
        r2.font.size = Pt(9)
        r2.font.color.rgb = TEXT_MUTED

    s3.notes_slide.notes_text_frame.text = (
        "Slide 3 presents the macro-architecture of our entire BPMN 2.0 model, generated directly from our Camunda XML deliverable. "
        "As shown in the diagram on the left, the model features a primary pool representing the commercial bank, structured into six functional lanes, "
        "and a completely separate external pool for the Credit Bureau. "
        "Notice the process boundaries: the lifecycle begins with an untyped Start Event where the applicant submits documents through the portal, "
        "and concludes successfully with the 'Loan Disbursed' end event. "
        "However, rather than a linear pipeline, the model contains multiple parallel splits, loops for document correction, and six distinct terminal "
        "failure end events. Every flow node belongs strictly to the lane responsible for its execution."
    )

    # ==========================================================
    # SLIDE 4: Task Types Used
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s4)
    add_header(s4, "Task Types Used & Technical Justification", "BPMN CONSTRUCTS")

    # 4 Columns of Cards for the 4 Task Types actually used
    task_data = [
        ("USER TASK", "👤", "Human interaction supported by a graphical user interface",
         "• Submit Loan Application (Applicant)\n• Underwriter Full Manual Review (Underwriter)\n• E-Sign Loan Agreement (Applicant)\n• Verify Income & Employment (Loan Officer)",
         "Requires human cognition, subjective judgement, or digital signature input. Cannot be fully automated by a script or API.",
         CYAN_ACCENT),
        ("SERVICE TASK", "⚙️", "Automated software execution without human intervention",
         "• Check Document Completeness\n• KYC Identity Verification API\n• AML Watchlist Screening\n• Calculate Eligibility & Risk Score\n• Disburse Loan Funds (Core Banking)",
         "Executes deterministic computational logic, external REST/SOAP API calls, or database operations with immediate automated return.",
         GREEN_ACCENT),
        ("SEND TASK", "✉️", "Outbound message dispatch to an external pool or participant",
         "• Request Credit Report (dispatched to Credit Bureau external pool)\n• Send Loan Offer to Applicant\n• Notify Applicant of Disbursement",
         "Models active dispatch of asynchronous communications crossing participant boundaries. Decouples sender execution from recipient processing.",
         BLUE_ACCENT),
        ("RECEIVE TASK / CATCH", "📥", "Waiting state for incoming message from an external pool",
         "• Receive Credit Report (Core Banking lane catches response from Credit Bureau pool)",
         "Halts sequence flow progression until a correlated message payload arrives from an independent external system. Non-polling asynchronous wait.",
         PURPLE_ACCENT)
    ]

    card_w = Inches(2.78)
    card_gap = Inches(0.2)
    left_start = Inches(0.8)

    for i, (t_name, icon, definition, examples, justification, accent_c) in enumerate(task_data):
        c_left = left_start + i * (card_w + card_gap)
        c = add_card(s4, c_left, Inches(1.5), card_w, Inches(5.4), BG_CARD, BORDER_CARD)
        tf = c.text_frame
        tf.word_wrap = True

        # Header badge
        p0 = tf.paragraphs[0]
        p0.text = f"{icon}  {t_name}"
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = accent_c
        p0.space_after = Pt(10)

        # Definition section
        p_d_lbl = tf.add_paragraph()
        p_d_lbl.text = "DEFINITION:"
        p_d_lbl.font.size = Pt(9.5)
        p_d_lbl.font.bold = True
        p_d_lbl.font.color.rgb = TEXT_MUTED

        p_d = tf.add_paragraph()
        p_d.text = definition
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_WHITE
        p_d.space_after = Pt(10)

        # Project Examples
        p_e_lbl = tf.add_paragraph()
        p_e_lbl.text = "PROJECT EXAMPLES:"
        p_e_lbl.font.size = Pt(9.5)
        p_e_lbl.font.bold = True
        p_e_lbl.font.color.rgb = accent_c

        p_e = tf.add_paragraph()
        p_e.text = examples
        p_e.font.size = Pt(9.5)
        p_e.font.color.rgb = TEXT_MUTED
        p_e.space_after = Pt(10)

        # Justification
        p_j_lbl = tf.add_paragraph()
        p_j_lbl.text = "WHY THIS TYPE?:"
        p_j_lbl.font.size = Pt(9.5)
        p_j_lbl.font.bold = True
        p_j_lbl.font.color.rgb = TEXT_MUTED

        p_j = tf.add_paragraph()
        p_j.text = justification
        p_j.font.size = Pt(9.5)
        p_j.font.color.rgb = TEXT_WHITE

    s4.notes_slide.notes_text_frame.text = (
        "Slide 4 covers our first mandatory core topic: Task Types Used. In BPMN 2.0, an unadorned task has no execution semantics. "
        "Therefore, every single task in our model was assigned a deliberate type based on its runtime behaviour. "
        "We utilized four distinct task constructs: "
        "First, User Tasks for human interactions requiring portal forms or expert decision-making, such as Underwriter Manual Review. "
        "Second, Service Tasks for automated computations and API integrations, such as KYC verification and Core Banking disbursement. "
        "Third, Send Tasks for dispatching outbound messages, such as requesting a credit score from the Credit Bureau. "
        "Fourth, Receive Events for asynchronously catching incoming messages. "
        "Importantly, we did not use Script Tasks because calculations like DTI and eligibility involve enterprise business logic and external "
        "database lookups, which are properly modelled as Service Tasks in an enterprise SOA architecture."
    )

    # ==========================================================
    # SLIDE 5: Gateways Used
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s5)
    add_header(s5, "Gateways Architecture & Concurrency Control", "CONTROL FLOW")

    # Left: Parallel Gateway Deep-Dive (5.7 in)
    c_and = add_card(s5, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_and = c_and.text_frame
    tf_and.word_wrap = True

    p = tf_and.paragraphs[0]
    p.text = "✛  PARALLEL GATEWAY (AND) — CONCURRENCY"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    p_sub = tf_and.add_paragraph()
    p_sub.text = "BPMN Symbol: Diamond with plus sign (+) marker"
    p_sub.font.size = Pt(10)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.space_after = Pt(10)

    and_points = [
        ("Purpose & Semantics: ", "Forks one incoming sequence flow into multiple concurrent execution paths without condition evaluation. The join waits for ALL incoming paths to complete before continuing."),
        ("Exact Model Location: ", "Fork: 'Start Parallel Verification Checks'\nJoin: 'All Parallel Checks Complete'"),
        ("The Three Concurrent Branches: ", "1. Fraud & Compliance Lane: Automated KYC & AML screening.\n2. Core Banking Lane: Outbound Credit Bureau request & catch.\n3. Core Banking Lane: Automated DTI ratio calculation."),
        ("Why AND is Mandatory Here: ", "If these checks ran sequentially, total onboarding time would be additive (SLA penalty). Running them in parallel drastically reduces latency. Synchronizing them at the join ensures the loan officer has complete data before manual underwriting begins."),
    ]
    for t, desc in and_points:
        p_row = tf_and.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = t
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_MUTED

    # Right: Exclusive Gateway Deep-Dive (5.7 in)
    c_xor = add_card(s5, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_xor = c_xor.text_frame
    tf_xor.word_wrap = True

    p = tf_xor.paragraphs[0]
    p.text = "✕  EXCLUSIVE GATEWAY (XOR) — DECISION ROUTING"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    p_sub = tf_xor.add_paragraph()
    p_sub.text = "BPMN Symbol: Diamond with an 'X' marker (or empty diamond)"
    p_sub.font.size = Pt(10)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.space_after = Pt(10)

    xor_points = [
        ("Purpose & Semantics: ", "Evaluates condition expressions and selects EXACTLY ONE outgoing branch. In alternative joining, it passes the first token that arrives without synchronization."),
        ("Key Decision Points in Model: ", "• 'Documents Complete?': Incomplete → return loop; Complete → proceed.\n• 'KYC Passed?': Pass → AML; Fail → Manual KYC; Unresolvable → Terminate.\n• 'Eligibility Decision': Score ≥ 750 → Auto-Approve; 600-749 → Manual Review; < 600 → Reject.\n• 'Underwriter Decision': Approve / Collateral Required / Reject.\n• 'Applicant Decision': Accept Offer / Counter-Offer / Withdraw."),
        ("Why Inclusive Gateways (OR) Were Avoided: ", "An Inclusive Gateway allows 1 to N branches to fire based on non-exclusive criteria. In our loan process, outcomes like 'Approve' and 'Reject' are mutually exclusive; an application cannot be simultaneously approved and rejected. Using XOR guarantees deterministic, bug-free execution."),
    ]
    for t, desc in xor_points:
        p_row = tf_xor.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = t
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_MUTED

    s5.notes_slide.notes_text_frame.text = (
        "Slide 5 details the Gateway architecture. In process modelling, gateways control the divergence and convergence of sequence flows. "
        "Our model relies on two primary gateway types: the Parallel Gateway and the Exclusive Gateway. "
        "The Parallel Gateway is critical for our verification stage: once document completeness passes, we fork execution into three concurrent "
        "streams: KYC and AML compliance, external Credit Bureau report retrieval, and Debt-to-Income ratio calculation. "
        "The Parallel Join ensures synchronization—the process cannot prematurely advance to income verification until all three background branches complete. "
        "Every other decision point—such as eligibility scoring and applicant offer acceptance—uses an Exclusive Gateway (XOR). "
        "A common viva question is why we did not use an Inclusive Gateway (OR). We explain clearly here: loan adjudication outcomes are strictly mutually "
        "exclusive. You cannot simultaneously approve and reject an application. XOR enforces mathematical determinism."
    )

    # ==========================================================
    # SLIDE 6: Intermediate Events Used
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s6)
    add_header(s6, "Intermediate & Boundary Events Deep-Dive", "EVENT ARCHITECTURE")

    # Top Banner explaining Boundary vs Normal Intermediate Event distinction
    c_banner = add_card(s6, Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.9), BG_CARD, BORDER_CARD)
    tf_b = c_banner.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.text = "CRITICAL BPMN DISTINCTION: INLINE INTERMEDIATE EVENTS VS. BOUNDARY EVENTS"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p_b_body = tf_b.add_paragraph()
    p_b_body.text = "• Inline Intermediate Events sit directly on sequence flows and pause normal flow progression until triggered.\n• Boundary Events attach to task perimeters; they monitor active task execution and handle external exceptions, deadlines, or faults."
    p_b_body.font.size = Pt(9.5)
    p_b_body.font.color.rgb = TEXT_WHITE

    # 4 Event Cards Below
    event_cards = [
        ("INTERMEDIATE MESSAGE CATCH", "✉️ (Catch)", "Inline Intermediate Event",
         "Trigger: Asynchronous incoming payload from Credit Bureau external pool.\nLocation: Core Banking Lane ('Receive Credit Report').\nAction: Unblocks sequence flow and passes credit report data into the scoring engine.\nWhy Needed: Models non-polling, asynchronous inter-organizational communication.",
         CYAN_ACCENT),
        ("NON-INTERRUPTING TIMER", "⏱️ (Dashed Double Ring)", "Boundary Event on Task",
         "Trigger: 24-Hour SLA expiry on Credit Bureau request; 48-Hour SLA on e-signature.\nLocation: 'Request Credit Report' & 'E-Sign Agreement'.\nAction: Fires a parallel recovery path (retry request / manual wet-signature alert) WITHOUT cancelling the main task.\nWhy Needed: Prevents application stall while preserving customer self-service window.",
         BLUE_ACCENT),
        ("INTERRUPTING TIMER", "⏱️ (Solid Double Ring)", "Boundary Event on Task",
         "Trigger: 7-Day deadline expiry on loan offer.\nLocation: Attached to 'Review Loan Offer' (Applicant).\nAction: Immediately CANCELS the active offer review task and diverts the token to 'EndEvent: Loan Offer Expired'.\nWhy Needed: Enforces commercial and regulatory validity; banks cannot leave interest rates open indefinitely.",
         AMBER_ACCENT),
        ("INTERRUPTING ERROR BOUNDARY", "⚡ (Solid Double Ring)", "Boundary Event on Task",
         "Trigger: System fault thrown by core banking (NEFT/RTGS API failure, frozen account).\nLocation: Attached to 'Disburse Loan Funds' Service Task.\nAction: Traps the technical exception, halts auto-disbursement, and routes to Operations for manual fallback retry.\nWhy Needed: Isolates financial transaction faults; prevents silent system failures.",
         RED_ACCENT),
    ]

    cw = Inches(2.78)
    cg = Inches(0.2)
    for i, (name, sym, ev_type, body, acc) in enumerate(event_cards):
        c_left = Inches(0.8) + i * (cw + cg)
        c = add_card(s6, c_left, Inches(2.55), cw, Inches(4.35), BG_CARD, BORDER_CARD)
        tf = c.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = name
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = acc
        p0.space_after = Pt(4)

        p_sym = tf.add_paragraph()
        p_sym.text = f"Symbol: {sym}"
        p_sym.font.size = Pt(9.5)
        p_sym.font.bold = True
        p_sym.font.color.rgb = TEXT_MUTED

        p_type = tf.add_paragraph()
        p_type.text = f"Category: {ev_type}"
        p_type.font.size = Pt(9.5)
        p_type.font.color.rgb = TEXT_WHITE
        p_type.space_after = Pt(8)

        p_body = tf.add_paragraph()
        p_body.text = body
        p_body.font.size = Pt(9.5)
        p_body.font.color.rgb = TEXT_MUTED

    s6.notes_slide.notes_text_frame.text = (
        "Slide 6 provides our deep-dive into Intermediate and Boundary Events, which is a mandatory topic in the evaluation rubric. "
        "It is crucial to avoid mislabeling boundary events as inline flow events. "
        "We clearly demonstrate the architectural difference: inline events sit directly in the sequence flow, while boundary events attach to task perimeters. "
        "Our model employs four distinct event configurations: "
        "1. Intermediate Message Catch: sits inline in the Core Banking lane, waiting for the external credit report. "
        "2. Non-interrupting Timer Boundary Events: with dashed double borders, these fire parallel escalations—like a 24-hour credit retry or a 48-hour "
        "e-signature reminder—without aborting the underlying user task. "
        "3. Interrupting Timer Boundary Event: with solid double borders on the 7-day offer review, which terminates the task and transitions directly to Offer Expired. "
        "4. Interrupting Error Boundary Event: attached to the automated disbursement service task to catch banking transfer exceptions and route them to Operations."
    )

    # ==========================================================
    # SLIDE 7: Happy Path / Critical Path
    # ==========================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s7)
    add_header(s7, "The Happy Path & Business-Critical Flow", "EXECUTION LIFECYCLE")

    # Step-by-Step Happy Path Flow (Left 7.8 in)
    c_happy = add_card(s7, Inches(0.8), Inches(1.5), Inches(7.8), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_h = c_happy.text_frame
    tf_h.word_wrap = True

    p = tf_h.paragraphs[0]
    p.text = "THE 15-STEP SEQUENTIAL HAPPY PATH"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    steps = [
        "1. Start Event: Applicant prepares and submits online loan application and KYC/income documents.",
        "2. Service Task: System validates document schema completeness (ID, pay slips, statements present).",
        "3. Parallel Split: Concurrently triggers KYC/AML screening, Credit Bureau request, and DTI computation.",
        "4. Fraud & Compliance: KYC identity matches government database; AML screening returns zero watchlist hits.",
        "5. External Credit Bureau: Returns credit score above threshold (Score ≥ 750) via Message Flow.",
        "6. Core Banking: Calculates DTI ratio within policy limit (DTI < 40%).",
        "7. Parallel Join: Synchronizes all three successful background streams.",
        "8. User Task: Loan Officer verifies submitted salary slips and employer standing.",
        "9. Service Task: Scoring engine calculates composite risk score → qualifies for Auto-Approval.",
        "10. User Task: Loan Officer generates standard loan offer letter with approved interest rate.",
        "11. Send Task: System dispatches formal offer letter to applicant portal & registered email.",
        "12. User Task: Applicant reviews terms and selects 'Accept Offer' within 7-day validity window.",
        "13. User Task: Applicant digitally e-signs loan agreement via integrated platform.",
        "14. User Task: Operations team verifies disbursement instructions and linked bank account.",
        "15. Service Task & End: Core Banking executes NEFT/RTGS transfer, creates loan account → Loan Disbursed!"
    ]
    for s in steps:
        sp = tf_h.add_paragraph()
        sp.space_after = Pt(2)
        sp.text = s
        sp.font.size = Pt(9.5)
        sp.font.color.rgb = TEXT_WHITE

    # Right: Terminology Clarification & Milestones (3.7 in)
    c_cpm = add_card(s7, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_cpm = c_cpm.text_frame
    tf_cpm.word_wrap = True

    p = tf_cpm.paragraphs[0]
    p.text = "CRITICAL BPMN TERMINOLOGY CLARIFICATION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    cpm_points = [
        ("Happy Path vs Critical Path: ", "In academic workflow modelling, the 'Happy Path' describes the optimal successful business execution with zero rework or failures. It should NOT be confused with the mathematically calculated Critical Path Method (CPM)."),
        ("Why CPM is Not Inferred: ", "CPM requires deterministic task duration distributions (earliest/latest start and slack). BPMN defines behavioral control-flow semantics. Inventing arbitrary durations without empirical log data is academically unsound."),
        ("Business-Critical Milestones: ", "1. Automated Verification Gate (all 3 parallel checks pass).\n2. Eligibility Adjudication (risk tier established).\n3. Customer Commitment (offer acceptance & e-signature).\n4. Fund Disbursement & Account Creation."),
    ]
    for t, desc in cpm_points:
        p_row = tf_cpm.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = t
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = TEXT_MUTED

    s7.notes_slide.notes_text_frame.text = (
        "On Slide 7, we trace the complete Happy Path of our system. The happy path represents the uninterrupted ideal flow: "
        "an eligible customer submits documents, passes automated KYC, AML, credit score, and DTI ratio checks concurrently, "
        "qualifies for auto-approval, accepts the generated offer, e-signs the agreement, and receives disbursement into their account. "
        "I want to draw your attention to an important academic distinction highlighted on the right: "
        "We explicitly distinguish the 'Happy Path' from the 'Critical Path'. In project management, the Critical Path Method relies on mathematical "
        "durations and zero float time. Because this assignment focuses on business process choreography rather than statistical queue simulations, "
        "we do not invent artificial task durations. Instead, we define the Happy Path as the business-critical sequence required to achieve value."
    )

    # ==========================================================
    # SLIDE 8: Critical Failure Points
    # ==========================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s8)
    add_header(s8, "Critical Failure Points Matrix (L1 – L6)", "EXCEPTION REGISTER")

    # Table of 6 Critical Failures: Trigger -> Detection -> Recovery -> Outcome
    c_tbl = add_card(s8, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_t = c_tbl.text_frame
    tf_t.word_wrap = True

    p = tf_t.paragraphs[0]
    p.text = "MANDATORY FAILURE PATH REGISTER — AUTOMATED VERIFICATION PHASE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RED_ACCENT
    p.space_after = Pt(8)

    failures_l1_l6 = [
        ("L1", "Document Incompleteness", "Missing Aadhaar/PAN, illegible bank statements, wrong PDF format.",
         "Service Task validation schema fails → Exclusive Gateway routes to 'Return Application'.",
         "Loan Officer issues correction notice; Applicant resubmits via loop. Timer limits lapse window.",
         "Correction Loop OR 'EndEvent: Application Lapsed'"),
        ("L2", "KYC Identity Mismatch", "Name misspelling, date of birth mismatch, expired ID document.",
         "KYC Service Task returns API error code → Exclusive Gateway branches to exception.",
         "Compliance Officer reviews document manually. If verified, rejoins AML flow; else terminates.",
         "Manual Clearance OR 'EndEvent: Fraud Terminated'"),
        ("L3", "AML / Watchlist Flag", "Applicant name matches sanctioned individuals, PEP lists, or fraud DB.",
         "AML Service Task flags risk score ≥ threshold → Exclusive Gateway branches to probe.",
         "Compliance Officer conducts deep manual investigation. Zero tolerance for sanctioned entities.",
         "Terminal 'EndEvent: Application Terminated – Fraud/AML'"),
        ("L4", "Credit Bureau Timeout", "Credit bureau service unresponsive, network partition, timeout > 24h.",
         "Non-interrupting Timer Boundary Event (24h) fires on outbound request task.",
         "Core Banking retries request asynchronously up to threshold, preserving customer session.",
         "Resilient Catch on retry OR manual credit assessment fallback"),
        ("L5", "Credit Score Rejection", "Report returns credit bureau score below minimum underwriting floor (< 600).",
         "Credit Bureau gateway evaluates score; feeds failed attribute into parallel join.",
         "Eligibility calculation incorporates sub-prime score; triggers auto-rejection decision.",
         "Terminal 'EndEvent: Loan Rejected – Low Credit Score'"),
        ("L6", "Excessive DTI Ratio", "Applicant liabilities result in debt-to-income ratio exceeding 50% limit.",
         "Automated DTI Service Task computes ratio > threshold → Exclusive Gateway routes to reject.",
         "Application marked financially unviable. Immediate rejection dispatched to applicant.",
         "Terminal 'EndEvent: Loan Rejected – Excessive DTI'"),
    ]

    for fid, name, cause, detect, recovery, outcome in failures_l1_l6:
        p_row = tf_t.add_paragraph()
        p_row.space_after = Pt(5)
        r0 = p_row.add_run()
        r0.text = f"[{fid}] {name}: "
        r0.font.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = CYAN_ACCENT

        r1 = p_row.add_run()
        r1.text = f"Trigger: {cause} | "
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = TEXT_MUTED

        r2 = p_row.add_run()
        r2.text = f"Detection: {detect} | "
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = TEXT_WHITE

        r3 = p_row.add_run()
        r3.text = f"Outcome: {outcome}"
        r3.font.bold = True
        r3.font.size = Pt(9.5)
        r3.font.color.rgb = AMBER_ACCENT

    s8.notes_slide.notes_text_frame.text = (
        "Slide 8 presents the first half of our Failure Path Register, covering failures L1 through L6. "
        "A key requirement of this project was to avoid simplifying the workflow into only the happy path. "
        "We followed the structured pattern requested: Failure Trigger → Detection Element → Recovery Action → Resulting Outcome. "
        "Notice how our model handles each failure gracefully: "
        "For L1, missing documents do not instantly kill the application; instead, a correction loop allows the student or customer to resubmit, "
        "governed by a lapse timer. "
        "For L2, automated KYC failures trigger a human compliance fallback rather than an immediate false-positive rejection. "
        "For L3, AML watchlist matches trigger an unrecoverable Terminate End Event. "
        "For L4, credit bureau outages are handled via non-interrupting timer retries, preventing system deadlocks."
    )

    # ==========================================================
    # SLIDE 9: Alternate and Exception Paths
    # ==========================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s9)
    add_header(s9, "Alternate & Exception Paths (L7 – L12)", "BRANCHING LOGIC")

    # Left: Underwriter & Collateral Re-valuation Loop (L7 & L8) (5.7 in)
    c_uw = add_card(s9, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_uw = c_uw.text_frame
    tf_uw.word_wrap = True

    p = tf_uw.paragraphs[0]
    p.text = "UNDERWRITER ADJUDICATION & COLLATERAL LOOP (L7 & L8)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    uw_steps = [
        ("Borderline Risk Scoring (L7): ", "When eligibility scoring falls into the 600–749 range or loan amount exceeds policy caps, the Exclusive Gateway diverts the application away from auto-approval to 'Underwriter Full Manual Review'."),
        ("Underwriter Three-Way Branch: ", "The underwriter has three mutually exclusive outcomes:\n• Approve: overrides risk tier, proceeds to offer generation.\n• Require Collateral: triggers secured asset evaluation (L8).\n• Reject: terminates flow to 'EndEvent: Loan Rejected'."),
        ("Collateral Valuation & Re-underwrite Loop (L8): ", "If collateral is required, a User Task requests an appraiser valuation. An Exclusive Gateway checks if Loan-to-Value (LTV) meets policy. If insufficient, 'Re-Underwrite' loops back to Underwriter Review with revised terms, avoiding premature rejection."),
    ]
    for t, desc in uw_steps:
        p_row = tf_uw.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = t
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = TEXT_MUTED

    # Right: Offer Expiry, Withdrawal, E-Sign & Disbursement (L9 – L12) (5.7 in)
    c_post = add_card(s9, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_post = c_post.text_frame
    tf_post.word_wrap = True

    p = tf_post.paragraphs[0]
    p.text = "OFFER EXPIRY, WITHDRAWAL & DISBURSEMENT FAULTS (L9 – L12)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p.space_after = Pt(8)

    post_steps = [
        ("L9 Offer Acceptance Timeout: ", "An interrupting boundary timer on 'Review Loan Offer' fires after 7 days, immediately aborting the offer and routing to 'EndEvent: Loan Offer Expired'."),
        ("L10 Applicant Withdrawal / Negotiation: ", "Applicants can select 'Counter-Offer' (initiating negotiation with Loan Officer) or 'Withdraw Application' (routing to data archival and 'EndEvent: Application Withdrawn')."),
        ("L11 E-Signature Latency: ", "A non-interrupting boundary timer (48h) triggers an Operations alert for wet-signature preparation without cancelling digital signing capability."),
        ("L12 Core Banking Disbursement Error: ", "An interrupting Error Boundary Event on 'Disburse Loan Funds' catches payment gateway / RTGS faults, preventing double-transfers and routing to Operations retry."),
    ]
    for t, desc in post_steps:
        p_row = tf_post.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = t
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = TEXT_MUTED

    s9.notes_slide.notes_text_frame.text = (
        "Slide 9 demonstrates how our model handles alternate and exception paths in the later stages of the lifecycle, specifically L7 through L12. "
        "A standout architectural feature on the left is our Underwriting and Collateral loop: borderline applications are not discarded. "
        "They are routed to an expert underwriter who can request collateral. If collateral appraisal reveals insufficient Loan-to-Value, "
        "the re-underwriting task loops back to adjust the loan terms dynamically. "
        "On the right, we showcase post-approval robustness: if a borrower ignores an offer, a 7-day interrupting timer expires the contract. "
        "If they request a counter-offer, an alternate negotiation loop is activated. "
        "Finally, for L12, should the core banking disbursement fail due to a network glitch or frozen account, an Error Boundary Event catches the technical "
        "fault, completely preventing untracked financial transactions and enabling operational recovery."
    )

    # ==========================================================
    # SLIDE 10: Failure Handling and Recovery
    # ==========================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s10)
    add_header(s10, "Failure Handling, Robustness & Governance", "FAULT ARCHITECTURE")

    # 4 Governance Pillar Cards
    pillars = [
        ("RETRY LIMITS & LOOP CONTROL", "🔁",
         "Uncontrolled loops create infinite execution deadlocks. Our model enforces strict loop limits on document corrections (L1) and credit bureau retries (L4). Once retry thresholds are exhausted, the flow deterministically escalates or terminates to an explicit Lapsed End Event.",
         CYAN_ACCENT),
        ("SLA TIMERS & ESCALATION", "⏰",
         "Strict temporal boundaries govern customer and operational responsiveness. Interrupting timers enforce commercial validity (7-day offer expiry), while non-interrupting timers trigger parallel administrative alerts (e-sign delays) without breaking customer self-service.",
         GREEN_ACCENT),
        ("HUMAN-IN-THE-LOOP FALLBACK", "👥",
         "Automated services can yield false negatives. When automated KYC API fails (L2), the model falls back to a Compliance Officer User Task. When e-signature platforms fail (L11), operations can execute physical wet-signatures, ensuring high conversion rates.",
         BLUE_ACCENT),
        ("RECOVERY VS. COMPENSATION", "⚖️",
         "In BPMN 2.0, 'Recovery' refers to forward error handling (retrying a task or taking an alternate branch). 'Compensation' (Undo / Compensate Event) cancels committed state. Our model utilizes forward recovery for disbursement retries and data archival on applicant withdrawal.",
         PURPLE_ACCENT),
    ]

    for i, (p_title, icon, p_desc, acc_c) in enumerate(pillars):
        top_pos = Inches(1.5) + i * Inches(1.35)
        c = add_card(s10, Inches(0.8), top_pos, Inches(11.7), Inches(1.2), BG_CARD, BORDER_CARD)
        tf = c.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = f"{icon}  {p_title}"
        p0.font.size = Pt(11.5)
        p0.font.bold = True
        p0.font.color.rgb = acc_c
        p0.space_after = Pt(3)

        p1 = tf.add_paragraph()
        p1.text = p_desc
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = TEXT_WHITE

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 highlights how our model maintains enterprise-grade robustness and governance. "
        "In production workflows, failure handling must satisfy four critical architectural pillars: "
        "First, Loop Control: infinite loops are a fatal modelling flaw. In our model, every document correction and API retry loop has an explicit limit, "
        "after which the application either lapses or escalates. "
        "Second, SLA Timers: both interrupting and non-interrupting timers prevent silent application stagnation. "
        "Third, Human-in-the-Loop Fallbacks: when automated microservices fail—such as an identity API outage—the workflow gracefully routes to a human officer. "
        "Fourth, a vital theoretical point often tested in vivas: the difference between Error Recovery and Compensation. "
        "Recovery is forward-looking error resolution, such as retrying a failed transfer. "
        "Compensation is backward-looking rollback of already-committed business transactions. Our model properly uses forward error recovery."
    )

    # ==========================================================
    # SLIDE 11: Design Decisions and Validation
    # ==========================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s11)
    add_header(s11, "Design Decisions, Validation & Limitations", "MODEL GOVERNANCE")

    # Left: Modelling Decisions & Schema Validation (5.7 in)
    c_val = add_card(s11, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_v = c_val.text_frame
    tf_v.word_wrap = True

    p = tf_v.paragraphs[0]
    p.text = "CORE MODELLING DECISIONS & RIGOR"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    val_points = [
        ("Strict Pool vs. Lane Boundary Discipline: ", "In BPMN 2.0, Sequence Flows can NEVER cross Pool boundaries. Because the Credit Bureau is an external legal entity, it was modelled as a separate Pool. All communication occurs strictly via Message Flows, preserving formal inter-organizational boundaries."),
        ("Deterministic Parallel Split & Synchronized Join: ", "Avoided race conditions and token leaks by pairing the Parallel Split with an explicit Parallel Join prior to manual income verification."),
        ("BPMN 2.0 Schema & Linter Validation: ", "The `.bpmn` XML was validated against the official OMG BPMN 2.0 XML Schema Definition (XSD). Diagram parsed and rendered cleanly in Camunda Modeler 5.49 and bpmn-js without syntax or containment errors."),
        ("Granular Failure Typology: ", "All 12 failure modes have dedicated recovery paths or distinct terminal end states, ensuring full auditability."),
    ]
    for t, desc in val_points:
        p_row = tf_v.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = "✔ " + t
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = TEXT_MUTED

    # Right: Limitations & Proposed Enhancements (5.7 in)
    c_lim = add_card(s11, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_l = c_lim.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "HONEST LIMITATIONS & FUTURE ENHANCEMENTS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p.space_after = Pt(8)

    lim_points = [
        ("DMN Decision Table Integration: ", "Current Limitation: Eligibility and DTI scoring logic are executed inside Service Tasks.\nProposed Improvement: Extract scoring rules into standalone Decision Model and Notation (DMN) tables linked via Business Rule Tasks for business-user modifiability."),
        ("Event Sub-Process for Global Cancellation: ", "Current Limitation: Applicant withdrawal is modelled via conditional gateway after offer review.\nProposed Improvement: Implement an Interrupting Event Sub-Process with a Message Start Event to permit applicant withdrawal at ANY active stage of the lifecycle."),
        ("Transactional Sub-Process for Disbursement: ", "Current Limitation: Disbursement failure uses an Error Boundary Event.\nProposed Improvement: Encapsulate disbursement, ledger reservation, and notification in a Transactional Sub-Process with automated compensation."),
    ]
    for t, desc in lim_points:
        p_row = tf_l.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = "🔍 " + t
        r1.font.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = TEXT_MUTED

    s11.notes_slide.notes_text_frame.text = (
        "Slide 11 addresses Design Decisions, Validation, and Academic Honesty regarding limitations. "
        "A major technical achievement of this project is strict BPMN 2.0 semantic compliance: sequence flows never cross pool boundaries. "
        "The external Credit Bureau is connected solely via message flows. We tested and validated the model XML in Camunda Modeler 5.49, "
        "confirming that all shapes, DI coordinates, and boundary events parse without error. "
        "Equally important in an academic presentation is discussing limitations and future improvements. "
        "We candidly identify three enhancements: "
        "First, migrating the hard-coded scoring logic in Service Tasks to DMN decision tables using Business Rule Tasks. "
        "Second, adding an Event Sub-Process to allow applicant withdrawal at any active point in the lifecycle. "
        "And third, adopting Transactional Sub-Processes with automated compensation handlers for multi-step fund reservation."
    )

    # ==========================================================
    # SLIDE 12: Conclusion & Questions
    # ==========================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s12)
    add_header(s12, "Conclusion & Academic Summary", "PROJECT SYNTHESIS")

    # Left: Summary Card (7.0 in)
    c_sum = add_card(s12, Inches(0.8), Inches(1.5), Inches(7.0), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_s = c_sum.text_frame
    tf_s.word_wrap = True

    p = tf_s.paragraphs[0]
    p.text = "KEY ACADEMIC & PRACTICAL TAKEAWAYS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(10)

    summary_bullets = [
        ("Comprehensive Process Coverage: ", "Successfully modelled the full retail loan origination lifecycle across 7 participants, transitioning from initial portal submission to core banking disbursement."),
        ("Engineering for Real-World Failure: ", "Incorporated 12 distinct failure paths (L1–L12) spanning data validation, compliance, external API latency, underwriter deliberation, and transaction faults."),
        ("Advanced BPMN 2.0 Semantics: ", "Demonstrated rigorous application of Parallel Gateways (deterministic concurrency), Exclusive Gateways (mutually exclusive routing), and both Interrupting and Non-Interrupting Boundary Events."),
        ("Production-Ready Governance: ", "Delivered an auditable, executable BPMN 2.0 XML specification supported by detailed Failure Path Registers and Task Type Justification documentation."),
    ]
    for t, desc in summary_bullets:
        bp = tf_s.add_paragraph()
        bp.space_after = Pt(10)
        r1 = bp.add_run()
        r1.text = "✔ " + t
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = bp.add_run()
        r2.text = desc
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_MUTED

    # Right: Thank You & Q&A Box (4.4 in)
    c_qa = add_card(s12, Inches(8.1), Inches(1.5), Inches(4.4), Inches(5.4), BG_CARD_ALT, CYAN_ACCENT)
    tf_q = c_qa.text_frame
    tf_q.word_wrap = True

    pq = tf_q.paragraphs[0]
    pq.alignment = PP_ALIGN.CENTER
    pq.text = "\n\nTHANK YOU!"
    pq.font.size = Pt(28)
    pq.font.bold = True
    pq.font.color.rgb = CYAN_ACCENT
    pq.space_after = Pt(14)

    pq_sub = tf_q.add_paragraph()
    pq_sub.alignment = PP_ALIGN.CENTER
    pq_sub.text = "Questions & Academic Discussion"
    pq_sub.font.size = Pt(16)
    pq_sub.font.bold = True
    pq_sub.font.color.rgb = TEXT_WHITE
    pq_sub.space_after = Pt(20)

    pq_meta = tf_q.add_paragraph()
    pq_meta.alignment = PP_ALIGN.CENTER
    pq_meta.text = "Presenter: Mayank Singh\nReg. No: RA2411003010116\nCourse: Workflow Automation\nSRMIST"
    pq_meta.font.size = Pt(12)
    pq_meta.font.color.rgb = TEXT_MUTED

    s12.notes_slide.notes_text_frame.text = (
        "In conclusion, our BPMN 2.0 model provides an enterprise-grade blueprint for retail loan origination that balances customer experience, "
        "operational efficiency, and regulatory compliance. "
        "By moving beyond standard happy-path diagrams to incorporate deterministic parallel concurrency, asynchronous external collaboration, "
        "and 12 resilient failure handling mechanisms, the model proves the real power of BPMN 2.0 as an executable engineering standard. "
        "Thank you, Professor and classmates, for your time and attention. I am now ready to answer any questions regarding our modeling choices, "
        "gateway semantics, or exception architectures."
    )

    out_pptx = r"d:\BPMN\October\Presentation\BPMN_Project_Presentation.pptx"
    prs.save(out_pptx)
    print(f"PowerPoint saved successfully to: {out_pptx}")

if __name__ == "__main__":
    create_presentation()
