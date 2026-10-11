import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
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

    p_sub = doc.add_paragraph()
    run_s = p_sub.add_run("Academic Examination & Defence Guide: Questions 1 & 2 (Student Project & Loan Origination)")
    run_s.font.name = "Arial"
    run_s.font.size = Pt(13)
    run_s.font.color.rgb = RGBColor(0, 150, 180)
    p_sub.paragraph_format.space_after = Pt(14)

    # Metadata Card
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

    # Scope Box
    box_t = doc.add_table(rows=1, cols=1)
    box_t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = box_t.rows[0].cells[0]
    c.width = Inches(6.5)
    set_cell_background(c, "E0F2FE")
    set_cell_margins(c, 140, 140, 180, 180)
    p_box = c.paragraphs[0]
    r_box = p_box.add_run("SCOPE & COVERAGE OF THIS VIVA GUIDE: ")
    r_box.font.name = "Arial"
    r_box.font.bold = True
    r_box.font.size = Pt(10)
    r_box.font.color.rgb = RGBColor(3, 105, 161)
    r_box_text = p_box.add_run(
        "This guide prepares the candidate for comprehensive examination on BOTH modelled assignment workflows: "
        "(1) Question 1: Student Project Approval & Allocation System (academic governance, 5 lanes, DMN guide matching), and "
        "(2) Question 2: Loan Origination & Approval System (retail banking, 7 lanes/pools, parallel concurrency, financial error trapping). "
        "Answers provide theoretical depth, exact BPMN 2.0 semantics, and direct evidence from project models."
    )
    r_box_text.font.name = "Arial"
    r_box_text.font.size = Pt(9.5)
    r_box_text.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    viva_qas = [
        {
            "num": "Q1",
            "category": "BPMN Task Types Comparison",
            "question": "What task types did you use across Question 1 and Question 2, and why did you choose specific types rather than generic tasks?",
            "answer": (
                "In BPMN 2.0, unadorned generic tasks lack execution semantics—they fail to define whether work is performed by human agents, "
                "automated software microservices, or asynchronous message exchanges. In an enterprise BPMN engine like Camunda, task typing dictates runtime handler routing:\n\n"
                "• User Tasks (👤): Represent work requiring human cognition, subjective evaluation, or form entry.\n"
                "  - Q1 Examples: 'Prepare and Submit Proposal' (Student), 'Evaluate Proposal' (Committee), 'Manual Guide Allocation' (Coordinator).\n"
                "  - Q2 Examples: 'Submit Loan Application' (Applicant), 'Underwriter Full Manual Review' (Underwriter), 'E-Sign Agreement' (Applicant).\n\n"
                "• Service Tasks (⚙️): Represent automated software execution invoking REST/SOAP APIs, internal algorithms, or database queries without human intervention.\n"
                "  - Q1 Examples: 'Validate Completeness', 'Validate Team Rules', 'Similarity & Duplicate Check', 'Auto-Allocate Guide'.\n"
                "  - Q2 Examples: 'KYC Identity Verification API', 'AML Screening API', 'Automated DTI Calculation', 'Disburse Loan Funds'.\n\n"
                "• Send Tasks & Receive/Message Catch (✉️ / 📥): Model active outbound message dispatch and passive waiting across participant boundaries.\n"
                "  - Q1: Send Task 'Send Guide Allocation Request' paired with Catch 'Receive Guide Acceptance'.\n"
                "  - Q2: Send Task 'Request Credit Report' paired with Catch 'Receive Credit Report' from external Credit Bureau.\n\n"
                "• Business Rule Task (📊) & Script Task (📜) in Q1:\n"
                "  - 'Check Guide Availability, Workload & Domain Match' uses a Business Rule Task to execute a DMN decision table.\n"
                "  - 'Log Withdrawal & Release Guide Pre-Assignment' uses a Script Task to immediately free allocated resources in engine memory."
            )
        },
        {
            "num": "Q2",
            "category": "Gateways & Concurrency",
            "question": "How do gateways differ between Question 1 and Question 2? Explain why Parallel Gateways were used in Q2 and Event-Based Gateways in Q1.",
            "answer": (
                "Gateways control divergence and convergence of sequence flows:\n\n"
                "• Exclusive Gateway (XOR ✕): Used in BOTH models for mutually exclusive condition routing.\n"
                "  - Q1: 'Proposal Valid?', 'Committee Decision' (Approve / Revise / Reject), 'Guide Available?'.\n"
                "  - Q2: 'KYC Passed?', 'Eligibility Decision' (Auto-Approve / Manual Review / Reject), 'Offer Decision'.\n"
                "  - Justification: Outcomes are mutually exclusive; an application cannot be simultaneously approved and rejected.\n\n"
                "• Parallel Gateway (AND ✛) in Question 2:\n"
                "  - Used for deterministic concurrency: 'Start Parallel Verification Checks' splits flow concurrently into (1) KYC/AML screening, (2) Credit Bureau request, and (3) DTI calculation. "
                "The join ('All Parallel Checks Complete') synchronizes all three streams before income verification. This cuts cycle times by >60% while eliminating token race conditions.\n\n"
                "• Event-Based Gateway (⬡) in Question 1:\n"
                "  - Used for competing asynchronous events: after sending the allocation request to the faculty guide, an Event-Based Gateway waits for either: "
                "Branch A: Message Catch 'Guide Accepts Request', OR Branch B: 3-Day Timer Event 'Guide Response Timeout'. The first event to occur dictates the path."
            )
        },
        {
            "num": "Q3",
            "category": "Intermediate & Boundary Events",
            "question": "What is an intermediate event, and what is the crucial architectural difference between an inline intermediate event and a task boundary event?",
            "answer": (
                "An Intermediate Event occurs between the start and end of a process, affecting flow without directly creating or terminating the process instance.\n\n"
                "The fundamental architectural distinction:\n"
                "1. Inline Intermediate Events: Sit directly on a sequence flow. When a token arrives, execution halts in a waiting state until triggered.\n"
                "   - Q1: 'Receive Guide Acceptance' & 'Receive Revision Request'.\n"
                "   - Q2: 'Receive Credit Report' (pauses Core Banking until credit agency message payload arrives).\n\n"
                "2. Boundary Events: Attach directly to the outer border of an active Task or Sub-Process, monitoring execution in real-time:\n"
                "   - Interrupting Boundary Event (Solid Double Ring): Immediately aborts/cancels the active task and diverts the token down the exception path (e.g., Q1 14-day submission timeout, Q2 7-day offer validity expiry, Q2 disbursement error).\n"
                "   - Non-Interrupting Boundary Event (Dashed Double Ring): Spawns a parallel escalation token while leaving the underlying task active (e.g., Q1 10-day committee review SLA reminder to HoD, Q2 24-hour credit retry, Q2 48-hour e-sign alert)."
            )
        },
        {
            "num": "Q4",
            "category": "Timer Event Strategies",
            "question": "Compare the timer boundary event strategies between the academic system (Q1) and the banking system (Q2).",
            "answer": (
                "Timer boundary events prevent silent process stagnation. We used distinct temporal strategies suited to each domain:\n\n"
                "• Question 1 (Academic Deadlines & Escalations):\n"
                "  - 14-Day Interrupting Timer on proposal preparation: Hard departmental cut-off. If students fail to submit, the draft is cancelled, routing to 'EndEvent: Proposal Lapsed'.\n"
                "  - 10-Day Non-Interrupting Timer on committee evaluation: Academic SLA reminder. Does not abort faculty review; dispatches an escalation notification to the Head of Department (HoD).\n"
                "  - 3-Day Event Timer on guide response: Prompts reallocation if faculty remains silent.\n\n"
                "• Question 2 (Banking SLAs & Offer Expirations):\n"
                "  - 24-Hour Non-Interrupting Timer on credit request: Triggers asynchronous API retries without invalidating the customer session.\n"
                "  - 48-Hour Non-Interrupting Timer on e-signature: Triggers operations wet-signature preparation while leaving the customer digital signing portal open.\n"
                "  - 7-Day Interrupting Timer on loan offer review: Enforces financial interest rate validity; cancels offer and routes to 'EndEvent: Loan Offer Expired'."
            )
        },
        {
            "num": "Q5",
            "category": "Happy Path vs Critical Path",
            "question": "What is the 'Happy Path', and why is it academically inaccurate to automatically call it the 'Critical Path'?",
            "answer": (
                "The 'Happy Path' describes the optimal, uninterrupted business trajectory where all forms are complete, all criteria pass, and value is delivered with zero rework:\n\n"
                "• Q1 Happy Path: Student Submits → Completeness Check Passes → Team Rules Pass → Coordinator Screens → Similarity Passes → Committee Approves → DMN Matches Guide → Auto-Allocate → Guide Accepts → Student Acknowledges → Guide Confirmed End.\n"
                "• Q2 Happy Path: Applicant Submits → Completeness Passes → Parallel KYC/Credit/DTI Pass → Income Verified → Auto-Approval → Offer Dispatched → Accepted → E-Signed → Core Banking Disburses → Loan Disbursed End.\n\n"
                "Why it is NOT mathematically the 'Critical Path':\n"
                "In formal project scheduling (CPM/PERT), the Critical Path is the sequence of dependent tasks with zero total slack, determined strictly by quantitative duration data. "
                "BPMN models behavioral control-flow semantics. Calling the happy path the critical path without empiric duration log data is a methodology error. "
                "We define the happy path as the 'Business-Critical Flow'."
            )
        },
        {
            "num": "Q6",
            "category": "Alternate Paths: Question 1",
            "question": "How are alternate and exception paths handled in Question 1? Give concrete examples of revision and reallocation loops.",
            "answer": (
                "In Question 1, alternate paths resolve academic weaknesses and resource constraints without premature student failure:\n\n"
                "1. Committee Revision Loop (F5):\n"
                "   - When the Review Committee evaluates a proposal as scientifically salvageable but requiring modification, an Exclusive Gateway routes to 'Send Revision Feedback'.\n"
                "   - The student team receives feedback via an Intermediate Message Catch Event, updates the abstract/scope, and resubmits.\n"
                "   - The proposal re-enters similarity checking. To avoid endless loops, the engine caps revision cycles at 2 iterations before forcing approval or rejection.\n\n"
                "2. Guide Decline & Reallocation Loop (F8 & F9):\n"
                "   - If the automated DMN matching finds no available guide or the assigned faculty declines, an Exclusive Gateway diverts to 'Manual Guide Allocation' in the Coordinator lane.\n"
                "   - The coordinator can assign an alternate faculty member, appoint an external co-guide, or waitlist the team. If manual assignment succeeds, flow rejoins confirmation; if impossible, it ends at 'No Guide Available'."
            )
        },
        {
            "num": "Q7",
            "category": "Alternate Paths: Question 2",
            "question": "How are alternate paths handled in Question 2? Explain the Underwriter Collateral Loop and Counter-Offer Negotiation.",
            "answer": (
                "In Question 2, alternate paths manage credit risk and commercial terms:\n\n"
                "1. Underwriting & Collateral Re-valuation Loop (L7 & L8):\n"
                "   - When scoring produces a borderline risk tier (score 600–749), the Exclusive Gateway bypasses auto-approval to 'Underwriter Full Manual Review'.\n"
                "   - The underwriter can mandate collateral backing. A valuation task inspects the asset. If the appraised Loan-to-Value (LTV) is insufficient, 'Re-Underwrite' loops back with reduced loan limits or requires additional security. Once satisfied, the underwriter approves and rejoins offer generation.\n\n"
                "2. Counter-Offer Negotiation Loop (L10):\n"
                "   - Upon receiving the offer, the borrower can select 'Counter-Offer'. A Loan Officer evaluates requested interest rate/tenor adjustments. If accepted, modified terms are finalized; if rejected, the flow concludes as rejected or withdrawn."
            )
        },
        {
            "num": "Q8",
            "category": "Loop Control & Deadlocks",
            "question": "What happens when retry limits are exhausted in your loop constructs across both projects?",
            "answer": (
                "Unbounded loops are a severe anti-pattern in BPMN, causing infinite token circulation and resource exhaustion. Both our models enforce strict loop boundaries:\n\n"
                "• In Question 1:\n"
                "  - Proposal correction loop (F1) is capped at 2 attempts, after which the application is terminated.\n"
                "  - Committee revision loop (F5) is strictly capped at 2 cycles. On the third review, the committee must issue a final Approve or Reject decision.\n\n"
                "• In Question 2:\n"
                "  - Document correction (L1) has a 14-day lapse timer.\n"
                "  - Credit Bureau retry requests (L4) are capped at 3 attempts; if unfulfilled, the process falls back to manual credit assessment.\n\n"
                "Every loop in our models possesses a deterministic escape condition leading to an auditable terminal end event."
            )
        },
        {
            "num": "Q9",
            "category": "Error Recovery vs Compensation",
            "question": "Why is Transactional Compensation fundamentally different from Error Handling, and where is each used in your projects?",
            "answer": (
                "This is a common theoretical viva question:\n\n"
                "• Error Handling (Forward Recovery): Catches a fault during active execution and takes an alternate forward route to resolve or terminate the error.\n"
                "  - Q2 Example: Interrupting Error Boundary Event on 'Disburse Loan Funds'. The NEFT/RTGS API failed before transaction completion, so the token diverts to an Operations User Task for retry. No previous completed milestones need reversal.\n\n"
                "• Compensation (Backward Rollback / Undo): Triggered by a Compensation Event. It retroactively cancels the business effect of ALREADY COMPLETED and committed activities.\n"
                "  - Q1 Example: When a student withdraws after committee approval (F11), a Script Task triggers compensation logic that releases the pre-assigned faculty guide reservation and decrements their workload counter in the database."
            )
        },
        {
            "num": "Q10",
            "category": "Pools vs Lanes Discipline",
            "question": "Why is the Credit Bureau modelled as an external Pool in Question 2, whereas Question 1 is modelled entirely within a single Pool with 5 Lanes?",
            "answer": (
                "Under OMG BPMN 2.0 specification standards:\n\n"
                "• Pools represent independent participants or distinct legal/organizational entities.\n"
                "• Lanes represent sub-partitions within a single organization (departments, user roles, internal software components).\n\n"
                "In Question 1, the Student, Coordinator, Committee, Guide, and System all belong to the SAME university department. Sequence flows can freely pass tokens across lanes within the same pool.\n\n"
                "In Question 2, the Credit Bureau (e.g., CIBIL, Experian) is an autonomous commercial enterprise outside the bank's boundary. "
                "BPMN 2.0 strictly FORBIDS Sequence Flows from crossing Pool boundaries. Communication must occur exclusively via Message Flows (dashed arrows). "
                "Modelling the Credit Bureau as an external Pool correctly enforces B2B asynchronous message exchange."
            )
        },
        {
            "num": "Q11",
            "category": "Technical Fault Containment",
            "question": "How do your models contain technical infrastructure failures (notification delivery in Q1 and disbursement in Q2)?",
            "answer": (
                "Both models contain technical failures using Interrupting and Non-Interrupting Error Boundary Events:\n\n"
                "• In Question 1 (F10 - Notification Delivery Failure):\n"
                "  - An Error Boundary Event on 'Send Allocation Notification' catches email/portal server outages. It isolates the error, preventing the guide allocation from being corrupted, and routes to 'EndEvent: System Failure – Manual IT Recovery Required'.\n\n"
                "• In Question 2 (L12 - Core Banking Disbursement Failure):\n"
                "  - An Interrupting Error Boundary Event on 'Disburse Loan Funds' catches payment gateway timeouts, invalid account formats, or frozen accounts during NEFT/RTGS handshakes. "
                "Execution is immediately halted to prevent double transfers, and the token routes to Operations for manual investigation and fallback retry."
            )
        },
        {
            "num": "Q12",
            "category": "Validation & Tooling",
            "question": "What tools did you use to validate your BPMN 2.0 XML diagrams, and how do you prove syntactic and semantic compliance?",
            "answer": (
                "Both BPMN 2.0 diagrams were verified using industry-standard tooling:\n\n"
                "1. Camunda Modeler (v5.49.0): Opened both `.bpmn` files to confirm that all flow node elements, BPMNDI visual coordinate bounds, lane containment sets, "
                "and boundary event attachments render cleanly without parse warnings or broken connections.\n"
                "2. bpmn-js / bpmn-to-image Engine: Headless browser rendering validated DOM parsing and generated high-resolution PNG exports without XML tag errors.\n"
                "3. OMG BPMN 2.0 Schema Conformance: Verified namespace declarations (`http://www.omg.org/spec/BPMN/20100524/MODEL` and `http://www.omg.org/spec/BPMN/20100524/DI`), "
                "unique XML IDs, valid sequence and message flow references, and correct pool boundary encapsulation."
            )
        }
    ]

    for q_data in viva_qas:
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
    print(f"Updated viva document saved successfully to: {out_docx}")

if __name__ == "__main__":
    create_viva_document()
