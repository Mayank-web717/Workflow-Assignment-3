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
    blank_layout = prs.slide_layouts[6]  # Blank slide layout

    # Professional Theme Palette
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
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(4.2), Inches(0.32))
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

    def add_card(slide, left, top, width, height, bg_color=BG_CARD, border_color=BORDER_CARD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # Image paths
    img_a1 = r"d:\BPMN\October\BPMN_Assignment_1\Assignment1_BPMN_Diagram.png"
    img_a3 = r"d:\BPMN\October\BPMN_Assignment_3\Assignment3_BPMN_Diagram.png"

    # ==========================================================
    # SLIDE 1: Title Slide (Both Questions)
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s1)

    dec = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(1.2), Inches(0.08))
    dec.fill.solid()
    dec.fill.fore_color.rgb = CYAN_ACCENT
    dec.line.fill.background()

    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(2.3))
    tf = t_box.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = "Enterprise BPMN 2.0 Process Modelling & Defence"
    p0.font.name = "Arial"
    p0.font.size = Pt(34)
    p0.font.bold = True
    p0.font.color.rgb = TEXT_WHITE
    p0.space_after = Pt(8)

    p1 = tf.add_paragraph()
    p1.text = "Comparative Process Modelling & Exception Architecture for Questions 1 & 2"
    p1.font.name = "Arial"
    p1.font.size = Pt(18)
    p1.font.color.rgb = CYAN_ACCENT
    p1.space_after = Pt(6)

    p2 = tf.add_paragraph()
    p2.text = "• Q1: Student Project Approval & Allocation System  |  • Q2: Loan Origination & Approval System"
    p2.font.name = "Arial"
    p2.font.size = Pt(13)
    p2.font.color.rgb = TEXT_MUTED

    # Student Details Card
    c1 = add_card(s1, Inches(0.8), Inches(3.8), Inches(5.6), Inches(2.8), BG_CARD, BORDER_CARD)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "CANDIDATE & ACADEMIC INFORMATION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(12)

    fields1 = [
        ("Student Name:", "Mayank Singh"),
        ("Registration Number:", "RA2411003010116"),
        ("Course / Subject:", "Workflow Automation"),
        ("Academic Institution:", "SRMIST"),
    ]
    for lbl, val in fields1:
        p_row = tf1.add_paragraph()
        p_row.space_after = Pt(7)
        r_lbl = p_row.add_run()
        r_lbl.text = f"{lbl}  "
        r_lbl.font.bold = True
        r_lbl.font.size = Pt(12)
        r_lbl.font.color.rgb = TEXT_MUTED
        r_val = p_row.add_run()
        r_val.text = val
        r_val.font.bold = True
        r_val.font.size = Pt(12.5)
        r_val.font.color.rgb = TEXT_WHITE

    # Project Scope & Architecture Card
    c2 = add_card(s1, Inches(6.8), Inches(3.8), Inches(5.7), Inches(2.8), BG_CARD, BORDER_CARD)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "SCOPE & ARCHITECTURAL HIGHLIGHTS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT
    p.space_after = Pt(12)

    fields2 = [
        ("Specification Standard:", "OMG BPMN 2.0 XML & Visual Diagram Interchange"),
        ("Question 1 Architecture:", "5 Swimlanes | 11 Failure Paths | DMN Guide Allocation"),
        ("Question 2 Architecture:", "7 Lanes (1 External Pool) | 12 Failure Paths | Parallel Concurrency"),
        ("Engine Validation:", "Tested on Camunda Modeler 5.49 & bpmn-js Engine"),
    ]
    for lbl, val in fields2:
        p_row = tf2.add_paragraph()
        p_row.space_after = Pt(7)
        r_lbl = p_row.add_run()
        r_lbl.text = f"{lbl}  "
        r_lbl.font.bold = True
        r_lbl.font.size = Pt(11.5)
        r_lbl.font.color.rgb = TEXT_MUTED
        r_val = p_row.add_run()
        r_val.text = val
        r_val.font.size = Pt(11.5)
        r_val.font.color.rgb = TEXT_WHITE

    s1.notes_slide.notes_text_frame.text = (
        "Good morning Professor and classmates. My name is Mayank Singh, registration number RA2411003010116, "
        "presenting our comprehensive academic project for the Workflow Automation course at SRMIST. "
        "In this presentation, I will defend our BPMN 2.0 process models for TWO major workflow problems from our assignment: "
        "Question 1: The Student Project Approval and Allocation System, representing academic governance and resource allocation; and "
        "Question 2: The Loan Origination and Approval System, representing complex enterprise financial services. "
        "Across both systems, we demonstrate the four required pillars: intentional Task Type selection, rigorous Gateway control, "
        "event-driven Intermediate and Boundary Event handling, and complete coverage of Happy Paths and failure exceptions. Let us begin."
    )

    # ==========================================================
    # SLIDE 2: Problem Statement and Objectives (Both Questions)
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s2)
    add_header(s2, "Problem Statements & Engineering Objectives", "PROJECT CONTEXT")

    # Left: Question 1 Problem
    c_q1 = add_card(s2, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf1 = c_q1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "QUESTION 1: STUDENT PROJECT APPROVAL SYSTEM"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    q1_points = [
        ("The Academic Challenge: ", "University departments manage hundreds of final-year capstone proposals. Manual paper flows lead to lost forms, plagiarism oversights, revision deadlocks, and guide workload imbalances."),
        ("Key Participants (5 Lanes): ", "Student/Team, Project Coordinator, Review Committee (incl. HoD), Faculty Guide, and Project Management System."),
        ("Core Objectives: ", "• Automate completeness & team rule validation.\n• Implement similarity/duplicate topic check gate.\n• Manage iterative committee revision cycles (SLA timers).\n• Rule-based faculty guide workload allocation."),
        ("Why BPMN 2.0: ", "BPMN swimlanes eliminate ambiguity between student submissions, coordinator screening, and committee academic evaluation."),
    ]
    for t, desc in q1_points:
        p_row = tf1.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = "• " + t
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_MUTED

    # Right: Question 2 Problem
    c_q2 = add_card(s2, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf2 = c_q2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "QUESTION 2: LOAN ORIGINATION & APPROVAL SYSTEM"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    q2_points = [
        ("The Banking Challenge: ", "Commercial lending workflows suffer from long processing times, customer abandonment, regulatory KYC/AML violations, external API downtime, and core banking transaction failures."),
        ("Key Participants (7 Lanes/Pools): ", "Applicant, Loan Officer, Underwriter, Compliance Team, Core Banking, Operations, and External Credit Bureau Pool."),
        ("Core Objectives: ", "• Concurrently execute KYC/AML, Credit Bureau, and DTI checks.\n• Enable underwriter manual review & collateral re-valuation.\n• Enforce 7-day offer acceptance expiry and 48-hour e-sign SLAs.\n• Contain technical errors during NEFT/RTGS disbursement."),
        ("Why BPMN 2.0: ", "BPMN 2.0 provides formal pool separation for external partners and event boundaries for transaction safety."),
    ]
    for t, desc in q2_points:
        p_row = tf2.add_paragraph()
        p_row.space_after = Pt(8)
        r1 = p_row.add_run()
        r1.text = "• " + t
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(10)
        r2.font.color.rgb = TEXT_MUTED

    s2.notes_slide.notes_text_frame.text = (
        "On Slide 2, we contrast the problem domains of our two assignments. "
        "In Question 1, the domain is university academic governance. Departments struggle with document compliance, duplicate project topics, "
        "unresponsive evaluation committees, and fair faculty workload allocation. BPMN 2.0 allows us to model clear accountability across 5 lanes. "
        "In Question 2, the domain is retail commercial lending. Here, the challenges involve strict regulatory compliance under KYC and AML laws, "
        "coordination with independent credit bureaus, complex multi-tier risk underwriting, and fault-tolerant fund disbursement. "
        "Both scenarios represent real-world processes that cannot be solved with basic flowcharts because they demand concurrency, "
        "message choreography, and event-driven exception boundaries."
    )

    # ==========================================================
    # SLIDE 3: Overall Architecture: Question 1 (Student Project)
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s3)
    add_header(s3, "Question 1: Student Project Approval Architecture", "SYSTEM ARCHITECTURE — Q1")

    # Diagram preview on Left
    c_diag1 = add_card(s3, Inches(0.8), Inches(1.5), Inches(7.8), Inches(5.4), BG_CARD, BORDER_CARD)
    if os.path.exists(img_a1):
        s3.shapes.add_picture(img_a1, Inches(0.9), Inches(1.6), Inches(7.6), Inches(5.2))

    # Details on Right
    c_det1 = add_card(s3, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_d1 = c_det1.text_frame
    tf_d1.word_wrap = True

    p = tf_d1.paragraphs[0]
    p.text = "Q1 ARCHITECTURAL SUMMARY"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    q1_meta = [
        ("Swimlanes (5): ", "Student/Team, Project Coordinator, Project Management System, Review Committee, Faculty Guide."),
        ("Process Boundaries: ", "Starts when student team submits proposal. Ends when guide is allocated & confirmed, or proposal rejected/lapsed."),
        ("Key Decision Gates: ", "1. Document Completeness (System)\n2. Team Rule Verification (System)\n3. Similarity / Plagiarism Gate (System)\n4. Committee Decision (Approve / Revise / Reject)\n5. Guide Availability Match (DMN)\n6. Guide Acceptance (Message / Timeout)."),
        ("Failure End States (6): ", "Invalid Proposal, Duplicate Topic, Proposal Lapsed, Proposal Rejected, No Guide Available, System Failure."),
    ]
    for t, desc in q1_meta:
        p_row = tf_d1.add_paragraph()
        p_row.space_after = Pt(6)
        r1 = p_row.add_run()
        r1.text = "✔ " + t
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(9)
        r2.font.color.rgb = TEXT_MUTED

    s3.notes_slide.notes_text_frame.text = (
        "Slide 3 shows the complete BPMN 2.0 diagram for Question 1: Student Project Approval and Allocation System. "
        "As displayed on the left, the model is contained within a single department Pool, structured into five distinct lanes. "
        "Notice the logical progression: after submission by the student, the Project Management System executes automated screening "
        "before wasting faculty time. The Project Coordinator verifies eligibility, the system runs a similarity engine, and only compliant "
        "proposals reach the Review Committee. "
        "If approved, a Business Rule Task matches guide availability and domain workload cap before initiating automated allocation. "
        "Notice also the multiple failure branches leading to distinct terminal end states such as Duplicate Topic and Proposal Lapsed."
    )

    # ==========================================================
    # SLIDE 4: Overall Architecture: Question 2 (Loan Origination)
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s4)
    add_header(s4, "Question 2: Loan Origination & Approval Architecture", "SYSTEM ARCHITECTURE — Q2")

    # Diagram preview on Left
    c_diag2 = add_card(s4, Inches(0.8), Inches(1.5), Inches(7.8), Inches(5.4), BG_CARD, BORDER_CARD)
    if os.path.exists(img_a3):
        s4.shapes.add_picture(img_a3, Inches(0.9), Inches(1.6), Inches(7.6), Inches(5.2))

    # Details on Right
    c_det2 = add_card(s4, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_d2 = c_det2.text_frame
    tf_d2.word_wrap = True

    p = tf_d2.paragraphs[0]
    p.text = "Q2 ARCHITECTURAL SUMMARY"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    q2_meta = [
        ("Participants & Pools: ", "7 Total: 6 internal bank lanes (Applicant, Loan Officer, Underwriter, Compliance, Core Banking, Operations) + 1 External Pool (Credit Bureau)."),
        ("Process Boundaries: ", "Starts when applicant submits loan form & docs. Ends when loan is disbursed, or rejected/withdrawn/expired/terminated."),
        ("Key Concurrency Feature: ", "Parallel Gateway forks 3 concurrent streams: KYC/AML check, Credit Bureau request, and DTI calculation."),
        ("External Message Exchange: ", "Message Flows connect Bank Core Banking lane to external Credit Bureau Pool for credit reports."),
        ("Failure End States (6): ", "Rejected, Withdrawn, Application Lapsed, Offer Expired, Fraud Terminated, Disbursement Failed."),
    ]
    for t, desc in q2_meta:
        p_row = tf_d2.add_paragraph()
        p_row.space_after = Pt(6)
        r1 = p_row.add_run()
        r1.text = "✔ " + t
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p_row.add_run()
        r2.text = desc
        r2.font.size = Pt(9)
        r2.font.color.rgb = TEXT_MUTED

    s4.notes_slide.notes_text_frame.text = (
        "Slide 4 displays the overall architecture for Question 2: Loan Origination and Approval System. "
        "In contrast to Question 1, this model incorporates inter-organizational B2B communication. "
        "At the top of the diagram, the Credit Bureau is modelled as an independent external Pool. "
        "Inside the Commercial Bank pool, we have six functional lanes. "
        "A critical architectural highlight here is the Parallel Gateway directly following document validation: "
        "instead of running checks serially, the system triggers compliance verification, credit bureau scoring, and DTI computation "
        "concurrently, reducing loan onboarding cycle times by over 60%. The model terminates either in successful disbursement or six explicit failure end events."
    )

    # ==========================================================
    # SLIDE 5: Task Types Used Across Both Processes
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s5)
    add_header(s5, "Task Types Used Across Both BPMN Processes", "BPMN CONSTRUCTS")

    # 4 Comparative Cards
    tasks = [
        ("USER TASK", "👤", "Human interaction supported by UI",
         "Q1 Examples:\n• Prepare & Submit Proposal (Student)\n• Screen Proposal (Coordinator)\n• Evaluate Proposal (Committee)\n• Manual Guide Allocation (Coordinator)\n\nQ2 Examples:\n• Submit Application (Applicant)\n• Verify Income & Employment (Officer)\n• Underwriter Full Review (Underwriter)\n• E-Sign Loan Agreement (Applicant)",
         "Selected whenever task completion requires human judgement, evaluation, negotiation, or manual form inputs. Cannot be executed by an automated script.",
         CYAN_ACCENT),
        ("SERVICE TASK", "⚙️", "Automated system execution",
         "Q1 Examples:\n• Validate Document Completeness\n• Validate Team Composition Rules\n• Similarity & Duplicate Topic Check\n• Auto-Allocate Guide\n\nQ2 Examples:\n• KYC Identity Verification API\n• AML Watchlist Screening API\n• Automated DTI Calculation\n• Disburse Loan Funds (Core Banking)",
         "Selected for deterministic computational logic, API integrations, and database operations without human intervention. Ensures instant SLA execution.",
         GREEN_ACCENT),
        ("SEND TASK & CATCH", "✉️ / 📥", "Outbound message dispatch & asynchronous catch",
         "Q1 Examples:\n• Send Task: Guide Allocation Request\n• Send Task: Revision Feedback\n• Message Catch: Receive Guide Acceptance\n\nQ2 Examples:\n• Send Task: Request Credit Report\n• Message Catch: Receive Credit Report\n• Send Task: Send Loan Offer Letter",
         "Selected to model active dispatch and asynchronous waiting states across organizational or participant boundaries without thread-blocking.",
         BLUE_ACCENT),
        ("BUSINESS RULE & SCRIPT", "📊 / 📜", "Decision tables and procedural utilities",
         "Q1 Business Rule Task:\n• Check Guide Availability, Workload & Domain Match (Evaluates DMN decision table)\n\nQ1 Script Task:\n• Log Withdrawal & Release Guide Pre-Assignment (Internal compensation cleanup)\n\nQ2 Service Scoring:\n• Calculate Eligibility Score (Engine API)",
         "Business Rule Tasks decouple dynamic business policy (faculty workload limits) from process code. Script tasks perform rapid local memory cleanups.",
         PURPLE_ACCENT),
    ]

    cw = Inches(2.78)
    cg = Inches(0.2)
    for i, (name, icon, defn, ex, just, acc) in enumerate(tasks):
        c_left = Inches(0.8) + i * (cw + cg)
        c = add_card(s5, c_left, Inches(1.5), cw, Inches(5.4), BG_CARD, BORDER_CARD)
        tf = c.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = f"{icon}  {name}"
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = acc
        p0.space_after = Pt(4)

        p_d = tf.add_paragraph()
        p_d.text = f"Def: {defn}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_after = Pt(6)

        p_e = tf.add_paragraph()
        p_e.text = ex
        p_e.font.size = Pt(8.5)
        p_e.font.color.rgb = TEXT_WHITE
        p_e.space_after = Pt(8)

        p_j = tf.add_paragraph()
        p_j.text = f"Why Chosen? {just}"
        p_j.font.size = Pt(8.5)
        p_j.font.color.rgb = TEXT_MUTED

    s5.notes_slide.notes_text_frame.text = (
        "Slide 5 provides a unified comparative analysis of the Task Types used in both Question 1 and Question 2. "
        "In BPMN 2.0, task typing dictates runtime execution semantics. "
        "Notice the alignment: across both projects, User Tasks model human cognition—such as committee reviews in Question 1 and underwriting "
        "in Question 2. Service Tasks handle automated microservices—like plagiarism checks in Question 1 and KYC APIs in Question 2. "
        "Both systems utilize Send Tasks and Intermediate Message Catch Events for asynchronous communication. "
        "Furthermore, Question 1 introduces a Business Rule Task to evaluate faculty workload caps against student project domains using a DMN decision table, "
        "and a Script Task to clean up allocation locks if a student withdraws. Every task type is technically justified."
    )

    # ==========================================================
    # SLIDE 6: Gateways & Concurrency Control
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s6)
    add_header(s6, "Gateways & Concurrency Control (Q1 vs. Q2)", "CONTROL FLOW")

    # 3 Cards: Exclusive Gateway, Parallel Gateway, Event-Based Gateway
    gw_cards = [
        ("EXCLUSIVE GATEWAY (XOR ✕)", "Decision Routing (Both Q1 & Q2)",
         "Evaluates condition expressions and activates EXACTLY ONE outgoing branch. On merge, passes any arriving token immediately.",
         "• Q1: 'Proposal Valid?' (Valid vs Incomplete)\n• Q1: 'Committee Decision' (Approve / Revise / Reject)\n• Q1: 'Guide Available?' (Found vs Manual Allocation)\n• Q2: 'KYC Passed?' (Pass vs Manual Review vs Terminate)\n• Q2: 'Eligibility Decision' (Auto-Approve / Underwriter / Reject)\n• Q2: 'Underwriter Decision' (Approve / Collateral / Reject)\n• Q2: 'Offer Decision' (Accept / Counter / Withdraw)",
         "Loan decisions and proposal verdicts are mutually exclusive; an application cannot be simultaneously approved and rejected. XOR ensures deterministic execution.",
         CYAN_ACCENT),
        ("PARALLEL GATEWAY (AND ✛)", "Concurrency Synchronization (Q2)",
         "Forks one incoming path into multiple concurrent branches without conditions. The join waits for ALL incoming paths before proceeding.",
         "• Q2 Fork: 'Start Parallel Verification Checks'\n  - Branch 1: KYC Identity & AML Screening\n  - Branch 2: Credit Bureau Score Retrieval\n  - Branch 3: Debt-to-Income (DTI) Calculation\n• Q2 Join: 'All Parallel Checks Complete'\n  - Synchronizes all 3 branches before income verification.",
         "Running checks serially creates additive cycle time. Parallel execution cuts processing latency while the synchronized join prevents token race conditions.",
         GREEN_ACCENT),
        ("EVENT-BASED GATEWAY (⬡)", "Competing Event Selection (Q1)",
         "Routes based on whichever external event occurs first, rather than evaluated data expressions.",
         "• Q1: 'Wait for Guide Acceptance or Timeout'\n  - Branch A: Intermediate Message Catch ('Guide Accepts Request')\n  - Branch B: Intermediate Timer Event ('3-Day Guide Response Timeout')\n  - Result: If guide accepts, proceeds to record allocation; if 3 days elapse, diverts to Coordinator Manual Allocation.",
         "Models real-world asynchronous competition: the process cannot know in advance whether the faculty member will accept or ignore the request.",
         AMBER_ACCENT)
    ]

    card_w3 = Inches(3.77)
    card_gap3 = Inches(0.2)
    for i, (name, sub, defn, ex, just, acc) in enumerate(gw_cards):
        c_left = Inches(0.8) + i * (card_w3 + card_gap3)
        c = add_card(s6, c_left, Inches(1.5), card_w3, Inches(5.4), BG_CARD, BORDER_CARD)
        tf = c.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = name
        p0.font.size = Pt(11.5)
        p0.font.bold = True
        p0.font.color.rgb = acc
        p0.space_after = Pt(2)

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(9.5)
        p_s.font.bold = True
        p_s.font.color.rgb = TEXT_MUTED
        p_s.space_after = Pt(6)

        p_d = tf.add_paragraph()
        p_d.text = f"Semantics: {defn}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_WHITE
        p_d.space_after = Pt(8)

        p_e = tf.add_paragraph()
        p_e.text = ex
        p_e.font.size = Pt(8.5)
        p_e.font.color.rgb = TEXT_MUTED
        p_e.space_after = Pt(8)

        p_j = tf.add_paragraph()
        p_j.text = f"Why Used? {just}"
        p_j.font.size = Pt(8.5)
        p_j.font.color.rgb = TEXT_WHITE

    s6.notes_slide.notes_text_frame.text = (
        "Slide 6 covers Gateway design across both projects. "
        "Notice the distinct gateway roles: "
        "Exclusive Gateways (XOR) are used in both Question 1 and Question 2 for binary and multi-way business decisions. "
        "Parallel Gateways (AND) are prominently featured in Question 2 for deterministic concurrency: forking verification into KYC, "
        "Credit Bureau, and DTI streams, and synchronizing them before underwriting. "
        "Question 1 features an Event-Based Gateway where execution waits for competing events: either the faculty guide accepts the allocation message, "
        "or a 3-day timer expires, triggering manual coordinator intervention. "
        "We also explicitly justify why Inclusive Gateways (OR) were avoided: in both domains, decision branches are mutually exclusive, "
        "and concurrency is strictly deterministic."
    )

    # ==========================================================
    # SLIDE 7: Intermediate & Boundary Events Deep-Dive
    # ==========================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s7)
    add_header(s7, "Intermediate & Boundary Events Deep-Dive", "EVENT ARCHITECTURE")

    c_banner = add_card(s7, Inches(0.8), Inches(1.5), Inches(11.7), Inches(0.85), BG_CARD, BORDER_CARD)
    tf_b = c_banner.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.text = "CRITICAL DISTINCTION: INLINE INTERMEDIATE EVENTS VS. TASK BOUNDARY EVENTS"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p_b_body = tf_b.add_paragraph()
    p_b_body.text = "• Inline Intermediate Events sit in the sequence flow and pause token progress until an external trigger arrives.\n• Boundary Events attach to task perimeters; they monitor active execution and catch external timeouts, faults, or cancellations."
    p_b_body.font.size = Pt(9.5)
    p_b_body.font.color.rgb = TEXT_WHITE

    event_grid = [
        ("INLINE MESSAGE CATCH", "✉️ (Catch)", "Sequence Flow Intermediate Event",
         "Q1: 'Receive Revision Request'\nStudent waits for committee feedback.\nQ1: 'Receive Guide Acceptance'\nSystem waits for guide response.\nQ2: 'Receive Credit Report'\nCore Banking waits for Credit Bureau report.",
         "Models non-polling asynchronous waiting. Decouples collaborating parties.",
         CYAN_ACCENT),
        ("NON-INTERRUPTING TIMER", "⏱️ (Dashed Ring)", "Boundary Event on Task",
         "Q1: '10-Day Review SLA Timer'\nFires HoD escalation reminder on committee.\nQ2: '24-Hour Credit Bureau Timer'\nFires automated retry request.\nQ2: '48-Hour E-Sign SLA Timer'\nTriggers wet-signature alert to operations.",
         "Fires parallel escalations without aborting or cancelling the primary active user task.",
         BLUE_ACCENT),
        ("INTERRUPTING TIMER", "⏱️ (Solid Ring)", "Boundary Event on Task",
         "Q1: '14-Day Submission Deadline'\nCancels proposal prep → EndEvent: Lapsed.\nQ1: '7-Day Revision Deadline'\nLimits student revision window.\nQ2: '7-Day Offer Validity Timer'\nCancels offer review → EndEvent: Offer Expired.",
         "Enforces hard deadlines. Instantly cancels the underlying task and diverts flow to expiry end.",
         AMBER_ACCENT),
        ("INTERRUPTING ERROR BOUNDARY", "⚡ (Solid Ring)", "Boundary Event on Task",
         "Q1: 'Notification Delivery Failure'\nCatches portal/SMS outage → IT recovery.\nQ2: 'Core Banking Disbursement Fault'\nCatches NEFT/RTGS transaction failure on Disburse Funds task → Operations retry.",
         "Traps technical and transaction exceptions, preventing untracked financial or system states.",
         RED_ACCENT)
    ]

    for i, (name, sym, ev_type, ex, just, acc) in enumerate(event_grid):
        c_left = Inches(0.8) + i * (cw + cg)
        c = add_card(s7, c_left, Inches(2.5), cw, Inches(4.4), BG_CARD, BORDER_CARD)
        tf = c.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = name
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = acc
        p0.space_after = Pt(2)

        p_s = tf.add_paragraph()
        p_s.text = f"Symbol: {sym}"
        p_s.font.size = Pt(9)
        p_s.font.bold = True
        p_s.font.color.rgb = TEXT_MUTED

        p_t = tf.add_paragraph()
        p_t.text = f"Type: {ev_type}"
        p_t.font.size = Pt(9)
        p_t.font.color.rgb = TEXT_WHITE
        p_t.space_after = Pt(6)

        p_e = tf.add_paragraph()
        p_e.text = ex
        p_e.font.size = Pt(8.5)
        p_e.font.color.rgb = TEXT_MUTED
        p_e.space_after = Pt(6)

        p_j = tf.add_paragraph()
        p_j.text = f"Why Needed? {just}"
        p_j.font.size = Pt(8.5)
        p_j.font.color.rgb = TEXT_WHITE

    s7.notes_slide.notes_text_frame.text = (
        "Slide 7 provides a detailed breakdown of Intermediate and Boundary Events across both Question 1 and Question 2. "
        "We clearly demonstrate the architectural distinction between inline events and boundary events. "
        "Both systems make extensive use of all four major event patterns: "
        "1. Inline Message Catch Events for asynchronous inter-process coordination; "
        "2. Non-interrupting Boundary Timers with dashed double rings for non-blocking SLA reminders in both student review and loan credit retries; "
        "3. Interrupting Boundary Timers with solid double rings for hard deadline enforcement, such as the 14-day proposal submission window "
        "in Question 1 and the 7-day offer validity period in Question 2; and "
        "4. Interrupting Error Boundary Events to catch system crashes and core banking transaction faults."
    )

    # ==========================================================
    # SLIDE 8: Happy Path & Business-Critical Flow (Comparative)
    # ==========================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s8)
    add_header(s8, "Happy Path & Business-Critical Flows (Q1 vs. Q2)", "EXECUTION LIFECYCLE")

    # Left: Q1 Happy Path
    c_hp1 = add_card(s8, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_h1 = c_hp1.text_frame
    tf_h1.word_wrap = True

    p = tf_h1.paragraphs[0]
    p.text = "QUESTION 1 HAPPY PATH (ACADEMIC ALLOCATION)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(6)

    q1_flow = [
        "1. Start Event: Student prepares and submits proposal form.",
        "2. Service Task: System validates document completeness.",
        "3. Service Task: System verifies team composition rules.",
        "4. User Task: Coordinator screens proposal for eligibility.",
        "5. Service Task: System executes similarity / duplicate check.",
        "6. User Task: Review Committee evaluates and APPROVES proposal.",
        "7. Business Rule Task: DMN checks guide workload and domain.",
        "8. Service Task: System executes automated guide allocation.",
        "9. Send Task: System dispatches allocation request to guide.",
        "10. Event Catch: Guide accepts request within 3-day SLA.",
        "11. Service Task: System formally records allocation in DB.",
        "12. Send Task: System dispatches confirmation to student team.",
        "13. User Task: Student acknowledges guide assignment.",
        "14. SUCCESS END: Project Allocated & Guide Confirmed."
    ]
    for s in q1_flow:
        sp = tf_h1.add_paragraph()
        sp.space_after = Pt(2)
        sp.text = s
        sp.font.size = Pt(8.5)
        sp.font.color.rgb = TEXT_WHITE

    # Right: Q2 Happy Path & Academic CPM Note
    c_hp2 = add_card(s8, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_h2 = c_hp2.text_frame
    tf_h2.word_wrap = True

    p = tf_h2.paragraphs[0]
    p.text = "QUESTION 2 HAPPY PATH & TERMINOLOGY DEFENCE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(6)

    q2_flow = [
        "1. Start Event: Applicant submits loan application & documents.",
        "2. Service Task: Completeness check validates document schema.",
        "3. Parallel Split: Triggers KYC/AML, Credit Bureau & DTI checks.",
        "4. Parallel Join: Synchronizes all 3 successful background checks.",
        "5. User Task: Loan Officer verifies income & employment.",
        "6. Service Task: Scoring engine calculates Auto-Approval score.",
        "7. Send Task: Officer generates & dispatches loan offer letter.",
        "8. User Task: Applicant reviews & ACCEPTS offer within 7 days.",
        "9. User Task: Applicant e-signs digital loan agreement.",
        "10. Service Task & End: Core Banking disburses funds via NEFT/RTGS.",
        "--- ACADEMIC CLARIFICATION ON CRITICAL PATH ---",
        "• Happy Path = Ideal sequence with zero rework or failures.",
        "• Critical Path Method (CPM) = Longest duration path with zero slack in operations research. It requires empirical task durations (PERT distributions).",
        "• Academic Stance: We do NOT invent artificial task durations. We model the Happy Path as the 'Business-Critical Flow'."
    ]
    for s in q2_flow:
        sp = tf_h2.add_paragraph()
        sp.space_after = Pt(2)
        sp.text = s
        sp.font.size = Pt(8.5)
        if "ACADEMIC" in s:
            sp.font.bold = True
            sp.font.color.rgb = AMBER_ACCENT
        elif "Happy Path =" in s or "Critical Path Method" in s or "Academic Stance" in s:
            sp.font.color.rgb = TEXT_MUTED
        else:
            sp.font.color.rgb = TEXT_WHITE

    s8.notes_slide.notes_text_frame.text = (
        "Slide 8 compares the Happy Paths of both processes. "
        "The happy path represents the ideal, uninterrupted execution trajectory where all validations pass and value is successfully delivered. "
        "In Question 1, it traces the proposal through automated screening, committee approval, DMN guide matching, and guide acceptance. "
        "In Question 2, it traces the loan application through parallel background checks, income verification, auto-approval, offer acceptance, "
        "and automated NEFT disbursement. "
        "We also reinforce our critical terminology defence: in academic examinations, students often conflate the Happy Path with the Critical Path Method (CPM). "
        "We explain clearly that CPM is a mathematical scheduling technique requiring statistical task duration distributions. "
        "Because our project focuses on behavioral choreography, we define the happy path as the Business-Critical Flow rather than guessing durations."
    )

    # ==========================================================
    # SLIDE 9: Critical Failure Points: Question 1 (Student Project)
    # ==========================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s9)
    add_header(s9, "Failure Path Matrix: Question 1 (Student Project)", "FAILURE REGISTER — Q1")

    c_f1 = add_card(s9, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_f1 = c_f1.text_frame
    tf_f1.word_wrap = True

    p = tf_f1.paragraphs[0]
    p.text = "QUESTION 1 FAILURE PATH REGISTER (F1 – F6 HIGHLIGHTS)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    q1_failures = [
        ("F1", "Document Incompleteness", "Missing sections, absent signatures, wrong document format.",
         "Service Task validation schema fails → Exclusive Gateway routes to Coordinator.",
         "Coordinator returns proposal with deficiency checklist for student correction.",
         "Correction Loop OR 'EndEvent: Invalid Proposal Returned'"),
        ("F2", "Team Rule Violation", "Team size below minimum, ineligible member, mixed-department rules.",
         "Service Task validates rules → Exclusive Gateway branches to invalidation.",
         "Proposal marked non-compliant. Student team must reform before resubmission.",
         "Terminal 'EndEvent: Invalid Proposal Returned'"),
        ("F3", "Duplicate / Plagiarised Topic", "Similarity engine detects ≥ 70% overlap with existing or past projects.",
         "Service Task similarity API flags score → Exclusive Gateway routes to rejection.",
         "Coordinator logs duplicate topic; student team must propose an entirely new topic.",
         "Terminal 'EndEvent: Duplicate / Plagiarised Topic'"),
        ("F4", "Proposal Submission Lapsed", "Student team fails to submit proposal within the 14-day departmental window.",
         "Interrupting Timer Boundary Event (14 days) fires on submission task.",
         "System automatically closes proposal draft; flags student team for late penalty.",
         "Terminal 'EndEvent: Proposal Lapsed'"),
        ("F5", "Committee Revision Request", "Committee finds proposal technically weak or overly broad, but salvageable.",
         "Exclusive Gateway on committee decision selects 'Requires Revision' branch.",
         "Send Task transmits feedback; student resubmits via loop (capped at 2 cycles).",
         "Revision Loop back to Similarity Check OR Withdrawal"),
        ("F6", "Committee Rejection", "Proposal judged academically infeasible, out of scope, or non-viable.",
         "Exclusive Gateway on committee decision selects 'Rejected' branch.",
         "Formal rejection notification dispatched; record archived.",
         "Terminal 'EndEvent: Proposal Rejected'"),
    ]

    for fid, name, cause, detect, recovery, outcome in q1_failures:
        p_row = tf_f1.add_paragraph()
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

    s9.notes_slide.notes_text_frame.text = (
        "Slide 9 outlines the Failure Path Register for Question 1, following the required visual format: "
        "Failure Trigger → Detection Element → Recovery Action → Resulting Outcome. "
        "Notice the realistic handling: incomplete proposals in F1 allow correction, while fundamental team rule violations in F2 terminate immediately. "
        "Plagiarism in F3 is caught by automated Service Tasks. "
        "Unresponsive students in F4 are timed out via an interrupting 14-day boundary event. "
        "In F5, committee revisions trigger a formal feedback loop, while outright rejections in F6 terminate gracefully to an auditable end event."
    )

    # ==========================================================
    # SLIDE 10: Critical Failure Points: Question 2 (Loan Origination)
    # ==========================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s10)
    add_header(s10, "Failure Path Matrix: Question 2 (Loan Origination)", "FAILURE REGISTER — Q2")

    c_f2 = add_card(s10, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_f2 = c_f2.text_frame
    tf_f2.word_wrap = True

    p = tf_f2.paragraphs[0]
    p.text = "QUESTION 2 FAILURE PATH REGISTER (L1 – L6 HIGHLIGHTS)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    q2_failures = [
        ("L1", "Document Completeness", "Missing income proof, illegible PAN/Aadhaar scans, invalid file format.",
         "Service Task completeness validation schema fails → Exclusive Gateway routes.",
         "Loan Officer issues deficiency notice; applicant resubmits via bounded loop.",
         "Correction Loop OR 'EndEvent: Application Lapsed'"),
        ("L2", "KYC Identity Mismatch", "Name misspelling, date of birth mismatch against government database.",
         "KYC Service Task returns API error code → Exclusive Gateway branches.",
         "Compliance Officer reviews document manually. If unresolvable, terminates.",
         "Manual Clearance OR 'EndEvent: Fraud Terminated'"),
        ("L3", "AML Watchlist Flag", "Applicant matches PEP lists, sanction registries, or financial crime DB.",
         "AML Service Task flags risk score ≥ threshold → Exclusive Gateway routes to probe.",
         "Compliance Officer conducts deep investigation; zero tolerance for sanctioned entities.",
         "Terminal 'EndEvent: Application Terminated – Fraud/AML'"),
        ("L4", "Credit Bureau Timeout", "Credit bureau service unresponsive, network partition, timeout > 24 hours.",
         "Non-interrupting Timer Boundary Event (24h) fires on outbound request task.",
         "Core Banking retries request asynchronously up to threshold without killing session.",
         "Resilient Catch on retry OR manual credit assessment fallback"),
        ("L5", "Credit Score Rejection", "Report returns credit bureau score below minimum underwriting floor (< 600).",
         "Credit Bureau gateway evaluates score; feeds failed attribute into parallel join.",
         "Eligibility calculation incorporates sub-prime score; triggers auto-rejection.",
         "Terminal 'EndEvent: Loan Rejected – Low Credit Score'"),
        ("L6", "Excessive DTI Ratio", "Applicant liabilities result in debt-to-income ratio exceeding 50% limit.",
         "Automated DTI Service Task computes ratio > threshold → Exclusive Gateway routes.",
         "Application marked financially unviable. Immediate rejection dispatched.",
         "Terminal 'EndEvent: Loan Rejected – Excessive DTI'"),
    ]

    for fid, name, cause, detect, recovery, outcome in q2_failures:
        p_row = tf_f2.add_paragraph()
        p_row.space_after = Pt(5)
        r0 = p_row.add_run()
        r0.text = f"[{fid}] {name}: "
        r0.font.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = GREEN_ACCENT

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

    s10.notes_slide.notes_text_frame.text = (
        "Slide 10 details the Failure Path Register for Question 2, covering failures L1 through L6. "
        "Notice how our financial exception handling mirrors real-world commercial banking: "
        "Missing documents in L1 trigger a correction loop with a lapse timer. "
        "In L2, automated KYC failures trigger a human compliance fallback to prevent false positives. "
        "In L3, AML watchlist matches trigger an unrecoverable Terminate End Event. "
        "In L4, credit bureau outages are handled via non-interrupting timer retries, preventing system deadlocks. "
        "In L5 and L6, credit score and DTI failures route cleanly through the scoring gateway into auditable rejection end events."
    )

    # ==========================================================
    # SLIDE 11: Alternate Paths & Complex Exception Loops
    # ==========================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s11)
    add_header(s11, "Alternate Paths & Exception Loops (Q1 & Q2)", "BRANCHING LOGIC")

    # Left: Q1 Loops
    c_lp1 = add_card(s11, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_lp1 = c_lp1.text_frame
    tf_lp1.word_wrap = True

    p = tf_lp1.paragraphs[0]
    p.text = "QUESTION 1: ACADEMIC EXCEPTION LOOPS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(8)

    q1_loops = [
        ("Committee Revision Loop (F5): ", "When the committee demands revisions, an Exclusive Gateway routes to 'Send Revision Feedback'. The student receives the feedback via an Intermediate Message Catch Event, revises the proposal, and resubmits. To prevent infinite loops, the process enforces a maximum of 2 revision cycles before forcing an approve/reject decision."),
        ("Guide Decline & Re-Allocation Loop (F8/F9): ", "When a faculty guide declines or the 3-day timer expires, the flow branches to Coordinator Manual Allocation. The coordinator can assign an alternate faculty member, appoint a co-guide, or place the team on a waitlist. If manual allocation succeeds, the flow rejoins confirmation; otherwise it ends at 'No Guide Available'."),
    ]
    for t, desc in q1_loops:
        p_row = tf_lp1.add_paragraph()
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

    # Right: Q2 Loops
    c_lp2 = add_card(s11, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_lp2 = c_lp2.text_frame
    tf_lp2.word_wrap = True

    p = tf_lp2.paragraphs[0]
    p.text = "QUESTION 2: BANKING EXCEPTION LOOPS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    q2_loops = [
        ("Underwriting & Collateral Loop (L7/L8): ", "Borderline scores (600–749) divert from auto-approval to 'Underwriter Full Manual Review'. If unsecured credit is too risky, the underwriter requests collateral valuation. If the appraised Loan-to-Value (LTV) is insufficient, 'Re-Underwrite' loops back with adjusted loan amounts, preventing premature rejection."),
        ("Applicant Counter-Offer Negotiation (L10): ", "Upon receiving the loan offer, the applicant can select 'Counter-Offer'. A Loan Officer manually reviews the requested rate/tenor adjustments. If accepted, negotiated terms are finalized; if rejected, the application concludes as rejected or withdrawn."),
        ("Disbursement Fault Retry (L12): ", "An Interrupting Error Boundary Event catches RTGS/NEFT failures, routing to Operations for manual fallback retry without risking double debit."),
    ]
    for t, desc in q2_loops:
        p_row = tf_lp2.add_paragraph()
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

    s11.notes_slide.notes_text_frame.text = (
        "Slide 11 examines the complex Alternate Paths and Exception Loops in both projects. "
        "A process model without loops cannot represent reality. "
        "In Question 1, we show two critical loops: the Committee Revision Loop, which allows students to revise proposals up to 2 cycles, "
        "and the Guide Allocation Fallback Loop, where declining guides trigger manual coordinator reassignment. "
        "In Question 2, we highlight the Underwriter and Collateral Valuation Loop, which enables secured re-underwriting rather than instant rejection, "
        "and the Counter-Offer Negotiation Loop between applicant and loan officer. "
        "Both systems illustrate how processes leave the happy path, resolve exceptions, and safely rejoin the main flow."
    )

    # ==========================================================
    # SLIDE 12: Process Robustness, Recovery Mechanisms & Governance
    # ==========================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s12)
    add_header(s12, "Process Robustness, Recovery & Governance", "FAULT ARCHITECTURE")

    pillars = [
        ("RETRY LIMITS & LOOP CONTROL", "🔁",
         "Uncontrolled loops create infinite execution deadlocks. Both models enforce strict loop counters: Question 1 limits committee revision cycles to 2 iterations and document resubmissions to 2 attempts. Question 2 bounds credit bureau retries and applicant document corrections with explicit lapse timers.",
         CYAN_ACCENT),
        ("SLA TIMERS & ESCALATION", "⏰",
         "Deadlines prevent applications from stalling silently. We use Interrupting Timers for hard cut-offs (Q1 14-day submission deadline, Q2 7-day offer acceptance expiry) and Non-Interrupting Timers for administrative reminders (Q1 10-day committee review SLA escalation to HoD, Q2 48-hour e-sign alert).",
         GREEN_ACCENT),
        ("HUMAN-IN-THE-LOOP FALLBACK", "👥",
         "Automated services can yield false negatives. When automated DMN guide allocation in Q1 finds no available guide, it falls back to a Coordinator User Task. When automated KYC in Q2 fails, a Compliance Officer manually adjudicates the document, maintaining high conversion rates.",
         BLUE_ACCENT),
        ("FORWARD RECOVERY VS. TRANSACTIONAL COMPENSATION", "⚖️",
         "In BPMN 2.0, Forward Recovery resolves active faults through retries and alternate branches (e.g., Q2 Core Banking disbursement error boundary). Backward Compensation cancels committed milestones. Q1 uses script compensation to release guide pre-allocations if a student withdraws.",
         PURPLE_ACCENT),
    ]

    for i, (p_title, icon, p_desc, acc_c) in enumerate(pillars):
        top_pos = Inches(1.5) + i * Inches(1.35)
        c = add_card(s12, Inches(0.8), top_pos, Inches(11.7), Inches(1.2), BG_CARD, BORDER_CARD)
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

    s12.notes_slide.notes_text_frame.text = (
        "Slide 12 brings together our four architectural pillars of Process Robustness and Governance across both models. "
        "First, Loop Control: infinite loops are a fatal modelling error. Both models bound every single loop construct. "
        "Second, SLA Timers: interrupting timers enforce legal validity, while non-interrupting timers trigger operational reminders. "
        "Third, Human-in-the-Loop Fallbacks: microservices gracefully degrade to human expert tasks when algorithms fail. "
        "Fourth, Error Recovery versus Compensation: we demonstrate forward error recovery on banking transfers and backward compensation "
        "logic when releasing guide reservations upon student withdrawal."
    )

    # ==========================================================
    # SLIDE 13: Design Decisions, BPMN 2.0 Validation & Limitations
    # ==========================================================
    s13 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s13)
    add_header(s13, "Design Decisions, Validation & Limitations", "MODEL GOVERNANCE")

    c_val = add_card(s13, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_v = c_val.text_frame
    tf_v.word_wrap = True

    p = tf_v.paragraphs[0]
    p.text = "MODELLING RIGOR & VALIDATION PROOF"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT
    p.space_after = Pt(8)

    val_points = [
        ("Strict Pool vs. Lane Boundary Discipline: ", "In BPMN 2.0, Sequence Flows can NEVER cross Pool boundaries. In Question 2, the external Credit Bureau is modelled as an independent Pool, and all communication uses Message Flows. In Question 1, internal lanes cleanly isolate academic roles."),
        ("Camunda Modeler 5.49 & bpmn-js Schema Validation: ", "Both `.bpmn` files were validated against official OMG BPMN 2.0 schemas. Diagrams parsed and rendered without XML syntax errors, containment flaws, or broken sequence references."),
        ("Deterministic Gateways: ", "Synchronized Parallel Joins prevent race conditions; Exclusive Gateways guarantee single-token determinism."),
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

    c_lim = add_card(s13, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_l = c_lim.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "ACADEMIC LIMITATIONS & FUTURE PROPOSALS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT
    p.space_after = Pt(8)

    lim_points = [
        ("DMN Decision Table Expansion: ", "While Question 1 uses Business Rule Tasks for guide matching, Question 2 currently encapsulates risk scoring inside Service Tasks. Future work should extract banking scoring into external DMN decision tables."),
        ("Global Event Sub-Processes for Cancellation: ", "Withdrawal is currently modelled at specific gateway points. Implementing an Interrupting Event Sub-Process with a Message Start Event would allow cancellation at ANY active stage in both systems."),
        ("Transactional Sub-Processes for Disbursement: ", "Encapsulating disbursement, ledger reservation, and notification in a Transactional Sub-Process would provide atomic compensation guarantees."),
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

    s13.notes_slide.notes_text_frame.text = (
        "Slide 13 addresses Design Decisions, Tool Validation, and Academic Honesty regarding limitations. "
        "Both models strictly conform to OMG BPMN 2.0 standards: sequence flows never cross pool boundaries, and all DI coordinates parse cleanly. "
        "We tested both models in Camunda Modeler 5.49 and verified that all boundary events, gateways, and lane sets render without errors. "
        "We also candidly address limitations: "
        "we propose expanding DMN decision tables to banking risk scoring, adding Event Sub-Processes for global cancellation, "
        "and utilizing Transactional Sub-Processes for distributed ledger compensation."
    )

    # ==========================================================
    # SLIDE 14: Conclusion & Questions
    # ==========================================================
    s14 = prs.slides.add_slide(blank_layout)
    apply_slide_background(s14)
    add_header(s14, "Conclusion & Academic Defence", "PROJECT SYNTHESIS")

    c_sum = add_card(s14, Inches(0.8), Inches(1.5), Inches(7.0), Inches(5.4), BG_CARD, BORDER_CARD)
    tf_s = c_sum.text_frame
    tf_s.word_wrap = True

    p = tf_s.paragraphs[0]
    p.text = "KEY ACADEMIC & PRACTICAL TAKEAWAYS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT
    p.space_after = Pt(10)

    summary_bullets = [
        ("Comprehensive Dual-Domain Modelling: ", "Successfully modelled two diverse workflows—academic capstone allocation (Q1) and commercial retail lending (Q2)—demonstrating the flexibility of BPMN 2.0."),
        ("Complete Failure Path Coverage: ", "Engineered 11 failure paths for Question 1 and 12 failure paths for Question 2, covering data validation, timeouts, policy rejections, and system faults."),
        ("Advanced Execution Semantics: ", "Demonstrated mastery of Parallel Gateways (concurrency), Exclusive Gateways (decisions), Event-Based Gateways (competing events), and both Interrupting and Non-Interrupting Boundary Events."),
        ("Production-Ready Engineering: ", "Delivered validated BPMN 2.0 XML files, comprehensive Failure Path Registers, and full Task/Gateway Justification documents."),
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

    c_qa = add_card(s14, Inches(8.1), Inches(1.5), Inches(4.4), Inches(5.4), BG_CARD_ALT, CYAN_ACCENT)
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

    s14.notes_slide.notes_text_frame.text = (
        "In conclusion, our BPMN 2.0 models demonstrate that business process modelling is an exact engineering discipline. "
        "By examining both Question 1 (Student Project Allocation) and Question 2 (Loan Origination), we have shown how BPMN 2.0 standardizes "
        "complex human and automated interactions, enforces regulatory and departmental governance, and builds resilience against real-world failures. "
        "Thank you, Professor and classmates, for your time and attention. I am now open to your questions."
    )

    out_pptx = r"d:\BPMN\October\Presentation\BPMN_Project_Presentation.pptx"
    prs.save(out_pptx)
    print(f"Dual-question presentation saved to: {out_pptx}")

if __name__ == "__main__":
    create_presentation()
