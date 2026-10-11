import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_viva_document():
    doc = Document()

    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Document Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_t = p_title.add_run("BPMN 2.0 Comprehensive Viva Voce Guide")
    run_t.font.name = "Arial"
    run_t.font.size = Pt(24)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(11, 25, 44)

    # Subtitle
    p_sub = doc.add_paragraph()
    run_s = p_sub.add_run("Academic Examination & Defence Guide: Loan Origination & Approval System")
    run_s.font.name = "Arial"
    run_s.font.size = Pt(14)
    run_s.font.color.rgb = RGBColor(0, 150, 180)
    p_sub.paragraph_format.space_after = Pt(16)

    # Metadata Card (Table)
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Candidate Name:", "Mayank Singh"),
        ("Registration Number:", "RA2411003010116"),
        ("Course / Subject:", "Workflow Automation"),
        ("Academic Institution:", "SRMIST")
    ]
    for row_idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[row_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "F8FAFC")
        set_cell_margins(c0, 100, 100, 140, 140)
        set_cell_margins(c1, 100, 100, 140, 140)

        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name = "Arial"
        r0.font.size = Pt(10)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(51, 65, 85)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name = "Arial"
        r1.font.size = Pt(10)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Overview box
    box_t = doc.add_table(rows=1, cols=1)
    box_t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = box_t.rows[0].cells[0]
    c.width = Inches(6.5)
    set_cell_background(c, "E0F2FE")
    set_cell_margins(c, 140, 140, 180, 180)
    p_box = c.paragraphs[0]
    r_box = p_box.add_run("PURPOSE OF THIS VIVA GUIDE: ")
    r_box.font.name = "Arial"
    r_box.font.bold = True
    r_box.font.size = Pt(10)
    r_box.font.color.rgb = RGBColor(3, 105, 161)
    r_box_text = p_box.add_run(
        "This document prepares the candidate for comprehensive academic questioning on BPMN 2.0 principles, "
        "modelling decisions, gateway semantics, event-driven failure containment, and project-specific execution "
        "in the Loan Origination & Approval System. Answers are structured with theoretical rigor and grounded directly in the project diagram."
    )
    r_box_text.font.name = "Arial"
    r_box_text.font.size = Pt(9.5)
    r_box_text.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Viva Questions and Detailed Answers
    viva_qas = [
        {
            "num": "Q1",
            "category": "BPMN Task Types",
            "question": "Why did you choose specific task types (User, Service, Send, Receive) rather than generic unadorned tasks?",
            "answer": (
                "In BPMN 2.0, an unadorned, generic task carries no execution semantics—it does not indicate whether it is executed by a human, "
                "a script, a web service, or an asynchronous message. In an executable workflow engine like Camunda 8 (Zeebe), each task type triggers "
                "different engine handlers:\n\n"
                "• User Tasks (e.g., 'Submit Loan Application', 'Underwriter Full Manual Review', 'E-Sign Loan Agreement'): represent work that requires "
                "human cognition, subjective assessment, or physical form input. The engine generates a task in a human task list.\n"
                "• Service Tasks (e.g., 'KYC Identity Verification', 'AML Watchlist Screening', 'Disburse Loan Funds'): represent automated software execution. "
                "They invoke REST APIs, microservices, or external database queries without human intervention.\n"
                "• Send Tasks (e.g., 'Request Credit Report', 'Send Loan Offer'): model active dispatch of asynchronous messages across participant or pool boundaries.\n"
                "• Intermediate Message Catch Events / Receive Tasks (e.g., 'Receive Credit Report'): pause token execution until a correlated message payload arrives from an independent system.\n\n"
                "We explicitly rejected Script Tasks for core scoring because complex risk models and KYC checks rely on enterprise SOA infrastructure rather than in-engine Groovy scripts."
            )
        },
        {
            "num": "Q2",
            "category": "Gateways & Concurrency",
            "question": "What is the exact functional and semantic difference between Exclusive (XOR) and Parallel (AND) Gateways in your model?",
            "answer": (
                "Gateways in BPMN 2.0 govern token routing, synchronization, and decision branching:\n\n"
                "• Parallel Gateway (AND): Evaluates NO conditions. Upon splitting ('Start Parallel Verification Checks'), it replicates incoming tokens across ALL "
                "outgoing branches simultaneously (in our project: 1. KYC/AML screening, 2. Credit Bureau request, 3. DTI calculation). Upon joining ('All Parallel Checks Complete'), "
                "it acts as a synchronizer: it halts progression until a token arrives from every single concurrent incoming branch. This guarantees zero race conditions.\n\n"
                "• Exclusive Gateway (XOR): Evaluates mutually exclusive sequence flow condition expressions and passes exactly ONE token along the first branch whose condition evaluates to true. "
                "Upon joining, it passes any arriving token immediately without synchronization.\n\n"
                "In our model, Parallel Gateways handle independent background checks to reduce turnaround time, while Exclusive Gateways enforce business decisions "
                "(e.g., Approve vs. Reject vs. Revise)."
            )
        },
        {
            "num": "Q3",
            "category": "Intermediate vs Boundary Events",
            "question": "What is an intermediate event, and what is the crucial architectural difference between an intermediate event in the normal flow and a boundary event?",
            "answer": (
                "An Intermediate Event is an event that occurs between the start and end of a process lifecycle, affecting the flow of the process without starting or ending it directly.\n\n"
                "The fundamental architectural distinction is:\n"
                "1. Inline Intermediate Events: Sit directly on a sequence flow (connected by incoming and outgoing sequence flows). When a token arrives, it enters a waiting state "
                "until the specified trigger occurs (e.g., our 'Receive Credit Report' message catch event). The process simply halts at that point in the normal path.\n\n"
                "2. Boundary Events: Attach directly to the outer perimeter/boundary of an activity (a Task or Sub-Process). They monitor the activity WHILE it is active. "
                "If the trigger occurs while the activity is executing:\n"
                "   - An Interrupting Boundary Event (solid double border) immediately cancels the activity and diverts the token down the exception path.\n"
                "   - A Non-Interrupting Boundary Event (dashed double border) spawns a parallel token down the exception branch while keeping the underlying activity running."
            )
        },
        {
            "num": "Q4",
            "category": "Timer Boundary Events",
            "question": "Why are timer events useful, and where did you employ interrupting vs. non-interrupting timer boundary events?",
            "answer": (
                "Timer events prevent workflows from stalling indefinitely due to unresponsive human actors or external service latency. In our project, we intentionally implemented both types:\n\n"
                "• Interrupting Timer Boundary Event (7-Day Offer Expiry): Attached to 'Review Loan Offer'. If the applicant does not accept or respond within 7 days, the offer legally expires. "
                "The task is instantly aborted, preventing stale credit terms from being executed, and the process routes to 'EndEvent: Loan Offer Expired'.\n\n"
                "• Non-Interrupting Timer Boundary Event (24-Hour Credit Bureau SLA & 48-Hour E-Sign SLA): Attached to 'Request Credit Report' and 'E-Sign Loan Agreement'. "
                "If the credit bureau does not reply within 24 hours, a parallel retry is dispatched without cancelling the original request. "
                "If e-signing takes longer than 48 hours, a parallel administrative alert notifies operations to prepare physical wet-signature documents while keeping the digital portal active."
            )
        },
        {
            "num": "Q5",
            "category": "Process Flow Definitions",
            "question": "What is the 'Happy Path', and why is it academically inaccurate to automatically call it the 'Critical Path'?",
            "answer": (
                "The 'Happy Path' (or default success path) is the sequence of activities that executes when everything proceeds under ideal conditions with zero exceptions, data validation errors, "
                "or rejections (in our model: Submission → Completeness Check → Parallel KYC/Credit/DTI Checks → Income Verification → Auto-Approval → Offer Dispatch → Acceptance → E-Sign → NEFT Disbursement).\n\n"
                "Why it is NOT necessarily the 'Critical Path':\n"
                "In formal project management and operations research, the Critical Path Method (CPM) requires quantitative duration data (mean activity durations, variance, earliest/latest start and finish times). "
                "The Critical Path is the longest duration path with zero total float/slack. "
                "BPMN models describe behavioral control flow and choreography, not duration mathematics. Calling the happy path the 'critical path' without empiric timing data confuses business priority with mathematical CPM. "
                "In our defence, we clarify that the Happy Path represents the 'Business-Critical Flow'."
            )
        },
        {
            "num": "Q6",
            "category": "Alternate Paths & Recovery",
            "question": "How is an alternate path handled in your BPMN model? Give a concrete example.",
            "answer": (
                "An alternate path represents a legitimate business variation that diverges from the standard auto-approval route but does not represent a catastrophic failure.\n\n"
                "Concrete Example: Underwriter Manual Review & Collateral Re-valuation (L7 & L8):\n"
                "When the scoring engine evaluates a borderline credit profile (score 600–749), an Exclusive Gateway branches away from the Happy Path to the Underwriter lane for manual review. "
                "The underwriter can require collateral. An appraiser inspects the asset. If the Loan-to-Value (LTV) ratio is insufficient, a 'Re-Underwrite' task loops back with adjusted loan amounts. "
                "Once satisfactory collateral is secured, the underwriter issues an approval, and the token seamlessly rejoins the Happy Path at 'Generate Loan Offer Letter'."
            )
        },
        {
            "num": "Q7",
            "category": "Failure Handling & Deadlocks",
            "question": "What happens when retry limits are exhausted in your loop constructs?",
            "answer": (
                "Unbounded loops are a severe anti-pattern in BPMN because they risk infinite execution deadlocks and resource exhaustion. In our model:\n\n"
                "1. Document Correction Loop (L1): When incomplete documents are submitted, the applicant is given an opportunity to resubmit. This loop is bounded by a maximum retry limit and a lapse timer. "
                "If the applicant fails to provide correct documents within the limit, the loop terminates to 'EndEvent: Application Lapsed'.\n\n"
                "2. Credit Bureau Retry Loop (L4): The non-interrupting timer triggers automated retry requests. If retries hit the maximum threshold without an API response, "
                "the process escapes to a manual credit assessment fallback by the Loan Officer.\n\n"
                "Every loop in our model has an explicit escape condition leading to an auditable terminal end state."
            )
        },
        {
            "num": "Q8",
            "category": "Error Handling vs Compensation",
            "question": "Why is Transactional Compensation fundamentally different from ordinary Error Handling in BPMN 2.0?",
            "answer": (
                "This is a common theoretical trap during viva examinations:\n\n"
                "• Error Handling (Forward Recovery): Traps a fault during execution (e.g., our Interrupting Error Boundary Event on 'Disburse Loan Funds'). "
                "The active task failed, was interrupted, and the process routes forward to a retry or administrative resolution task. No previous completed tasks need their effects reversed.\n\n"
                "• Compensation (Backward Rollback / Undo): Triggered by a Compensation Intermediate/End Event. It cancels or undoes the business effects of already-completed, committed tasks. "
                "For example, if funds had already been debited from a reserve pool and the loan was subsequently aborted, a compensation handler would credit the reserve pool back.\n\n"
                "Our disbursement failure uses Error Handling because the transfer API failed before commitment, requiring forward retry rather than retrospective rollback."
            )
        },
        {
            "num": "Q9",
            "category": "Project-Specific Architecture",
            "question": "Why is the Credit Bureau modelled as an external Pool rather than another Lane inside the Bank Pool?",
            "answer": (
                "In BPMN 2.0 specification standards, Pools represent independent participants or separate legal entities/organizations with distinct governance boundaries. "
                "Lanes, conversely, represent sub-partitions within a single organization (such as departments or software systems).\n\n"
                "The Credit Bureau (e.g., CIBIL, Experian) is an autonomous external entity with its own internal processes and databases. "
                "According to BPMN 2.0 rules, Sequence Flows CANNOT cross Pool boundaries. Only Message Flows (dashed arrows with open circles) are permitted between pools. "
                "Modelling the Credit Bureau as an external Pool accurately captures cross-organizational, asynchronous message choreography."
            )
        },
        {
            "num": "Q10",
            "category": "Compliance & Fraud Architecture",
            "question": "How does your model ensure zero-tolerance compliance for KYC and AML violations?",
            "answer": (
                "Regulatory banking frameworks (such as RBI and FATF guidelines) mandate strict compliance isolation:\n\n"
                "• In our model, KYC Identity Verification (L2) and AML Screening (L3) execute immediately after document completeness.\n"
                "• If automated KYC fails, it routes to a Compliance Officer User Task. If identity cannot be proven, the application routes to 'EndEvent: Fraud Terminated'.\n"
                "• For AML screening, if an applicant matches a sanctioned entity or fraud registry, the application is instantly halted, investigated, and diverted to "
                "'EndEvent: Application Terminated – Fraud/AML Violation'.\n"
                "• Because these checks are joined via the Parallel Gateway, an application with an unresolvable AML flag CAN NEVER bypass compliance or reach underwriting."
            )
        },
        {
            "num": "Q11",
            "category": "Technical Fault Isolation",
            "question": "How does the model prevent double-disbursement or untracked financial transactions when Core Banking fails?",
            "answer": (
                "Automated disbursement is executed by a Service Task ('Disburse Loan Funds') in the Core Banking lane. "
                "In financial systems, technical faults (network timeouts during NEFT/RTGS handshakes, database locks, or frozen beneficiary accounts) can cause catastrophic reconciliation errors if not trapped.\n\n"
                "We attached an Interrupting Error Boundary Event to this Service Task. If the core banking integration throws an exception, the boundary event catches it, "
                "cancels automated execution to prevent duplicate transactions, and diverts the token to Operations for manual reconciliation and retry ('Retry Disbursement'). "
                "If the retry succeeds, the loan account is created; if permanent failure occurs, the process terminates to 'EndEvent: Disbursement Failed – Manual Intervention Required'."
            )
        },
        {
            "num": "Q12",
            "category": "Validation & Tooling",
            "question": "What tools did you use to validate your BPMN 2.0 XML diagram, and how do you prove its syntactic correctness?",
            "answer": (
                "Our diagram was developed and validated using industry-standard BPMN tooling:\n\n"
                "1. Camunda Modeler (v5.49.0): Opened the generated XML to confirm that all flow node elements, BPMNDI visual coordinate bounds, lane containment sets, "
                "and boundary event attachments render cleanly without parse warnings.\n"
                "2. bpmn-js / bpmn-to-image Engine: Headless browser rendering validated complete DOM parsing and generated high-resolution PNG exports without any unparsable tag errors.\n"
                "3. OMG BPMN 2.0 Schema Conformance: Ensured strict namespace declarations (`http://www.omg.org/spec/BPMN/20100524/MODEL` and `http://www.omg.org/spec/BPMN/20100524/DI`), "
                "valid IDs for all flow elements, and correct directional sequence and message flow references."
            )
        }
    ]

    for q_data in viva_qas:
        # Question Header Box
        q_table = doc.add_table(rows=1, cols=1)
        q_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        q_cell = q_table.rows[0].cells[0]
        q_cell.width = Inches(6.5)
        set_cell_background(q_cell, "1E293B")
        set_cell_margins(q_cell, 120, 120, 160, 160)

        p_q = q_cell.paragraphs[0]
        r_q_badge = p_q.add_run(f"[{q_data['num']} — {q_data['category'].upper()}]\n")
        r_q_badge.font.name = "Arial"
        r_q_badge.font.bold = True
        r_q_badge.font.size = Pt(9.5)
        r_q_badge.font.color.rgb = RGBColor(56, 189, 248)

        r_q_txt = p_q.add_run(q_data['question'])
        r_q_txt.font.name = "Arial"
        r_q_txt.font.bold = True
        r_q_txt.font.size = Pt(11)
        r_q_txt.font.color.rgb = RGBColor(248, 250, 252)

        # Answer Box
        a_table = doc.add_table(rows=1, cols=1)
        a_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        a_cell = a_table.rows[0].cells[0]
        a_cell.width = Inches(6.5)
        set_cell_background(a_cell, "F8FAFC")
        set_cell_margins(a_cell, 140, 140, 160, 160)

        p_a = a_cell.paragraphs[0]
        r_a_lbl = p_a.add_run("SUGGESTED MODEL ANSWER & DEFENCE:\n")
        r_a_lbl.font.name = "Arial"
        r_a_lbl.font.bold = True
        r_a_lbl.font.size = Pt(10)
        r_a_lbl.font.color.rgb = RGBColor(14, 116, 144)

        r_a_txt = p_a.add_run(q_data['answer'])
        r_a_txt.font.name = "Arial"
        r_a_txt.font.size = Pt(10)
        r_a_txt.font.color.rgb = RGBColor(30, 41, 59)

        doc.add_paragraph().paragraph_format.space_after = Pt(12)

    out_docx = r"d:\BPMN\October\Presentation\BPMN_Viva_Questions_and_Answers.docx"
    doc.save(out_docx)
    print(f"Viva document saved successfully to: {out_docx}")

if __name__ == "__main__":
    create_viva_document()
