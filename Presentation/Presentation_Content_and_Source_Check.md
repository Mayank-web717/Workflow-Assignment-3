# Presentation Content & Source Mapping Verification Report (Dual Questions)

**Project Title:** Enterprise BPMN 2.0 Process Modelling & Defence  
**Course:** Workflow Automation (SRMIST)  
**Student Name:** Mayank Singh (RA2411003010116)  
**Standard:** OMG BPMN 2.0 (XML & Diagrammatic Interchange)  

**Primary Source Documents:**
* **Question 1:**
  * Diagram XML: [`d:\BPMN\October\BPMN_Assignment_1\Assignment1_BPMN_Diagram.bpmn`](file:///d:/BPMN/October/BPMN_Assignment_1/Assignment1_BPMN_Diagram.bpmn)
  * Diagram Visual: [`d:\BPMN\October\BPMN_Assignment_1\Assignment1_BPMN_Diagram.png`](file:///d:/BPMN/October/BPMN_Assignment_1/Assignment1_BPMN_Diagram.png)
  * Failure Register: [`d:\BPMN\October\BPMN_Assignment_1\Assignment1_Failure_Path_Register.md`](file:///d:/BPMN/October/BPMN_Assignment_1/Assignment1_Failure_Path_Register.md)
  * Justification: [`d:\BPMN\October\BPMN_Assignment_1\Assignment1_Justification.md`](file:///d:/BPMN/October/BPMN_Assignment_1/Assignment1_Justification.md)
* **Question 2:**
  * Diagram XML: [`d:\BPMN\October\BPMN_Assignment_3\Assignment3_BPMN_Diagram.bpmn`](file:///d:/BPMN/October/BPMN_Assignment_3/Assignment3_BPMN_Diagram.bpmn)
  * Diagram Visual: [`d:\BPMN\October\BPMN_Assignment_3\Assignment3_BPMN_Diagram.png`](file:///d:/BPMN/October/BPMN_Assignment_3/Assignment3_BPMN_Diagram.png)
  * Failure Register: [`d:\BPMN\October\BPMN_Assignment_3\Assignment3_Failure_Path_Register.md`](file:///d:/BPMN/October/BPMN_Assignment_3/Assignment3_Failure_Path_Register.md)
  * Justification: [`d:\BPMN\October\BPMN_Assignment_3\Assignment3_Justification.md`](file:///d:/BPMN/October/BPMN_Assignment_3/Assignment3_Justification.md)

---

## 1. Executive Summary

This academic presentation covers **TWO distinct assignments** from the course assignment document `BPMN_Project_Assignments.docx`:
1. **Question 1 (Assignment 1): Student Project Approval & Allocation System** — Academic capstone governance, 5 departmental swimlanes, committee evaluations, automated similarity/plagiarism gate, and DMN faculty guide workload allocation.
2. **Question 2 (Assignment 3): Loan Origination & Approval System** — Retail banking loan onboarding, 7 participants across internal lanes and an external Credit Bureau pool, parallel verification concurrency (KYC/AML + Credit Bureau + DTI), and fault-tolerant disbursement.

---

## 2. 14-Slide Content & Source Mapping Matrix

| Slide | Title | Primary Content Covered | Mapped Diagram Elements in Source XML |
| :---: | :--- | :--- | :--- |
| **1** | Title Slide | Dual-question title, student info (Mayank Singh, RA2411003010116), course (Workflow Automation), institution (SRMIST), validation badge. | Project metadata mapping to Q1 & Q2. |
| **2** | Problem Statements & Objectives | Academic capstone allocation problems (Q1) vs. Retail banking loan onboarding drop-offs and KYC/AML mandates (Q2); BPMN 2.0 justification. | Business context justifying 5 lanes (Q1) and 7 lanes/pools (Q2). |
| **3** | Architecture: Question 1 | Embedded high-res render of Assignment 1 diagram; 5 lanes breakdown; process boundaries; 6 failure end states. | `Process_ProjectAllocation`, `Lane_Student`, `Lane_Coordinator`, `Lane_System`, `Lane_Committee`, `Lane_Guide`. |
| **4** | Architecture: Question 2 | Embedded high-res render of Assignment 3 diagram; 7 lanes/pools; external Credit Bureau pool; parallel verification topology; 6 failure end states. | `Collaboration_LoanOrigination`, `Pool_Bank`, `Pool_CreditBureau`, `StartEvent_ApplyLoan`, `EndEvent_Disbursed`. |
| **5** | Task Types Used Across Both | 4 comparative task categories: User Task (human form/deliberation), Service Task (automated API/computation), Send/Catch (messaging), Business Rule Task & Script Task (Q1). | Q1: `Task_SubmitProposal`, `Task_ValidateCompleteness`, `Task_CheckGuideWorkload`; Q2: `Task_KYCVerification`, `Task_DisburseFunds`, etc. |
| **6** | Gateways & Concurrency Control | Exclusive Gateway (XOR) in both Q1 & Q2; Parallel Gateway (AND Split/Join) for concurrent checks in Q2; Event-Based Gateway for guide acceptance in Q1; rationale against Inclusive Gateway (OR). | Q1: `GW_ProposalValid`, `GW_CommitteeDecision`, `GW_EventBasedGuideAccept`; Q2: `GW_SplitParallelChecks`, `GW_JoinParallelChecks`, `GW_EligibilityDecision`. |
| **7** | Intermediate & Boundary Events | Categorization: Inline Message Catch vs Task Boundary Events; Non-interrupting Timers (SLA reminders); Interrupting Timers (hard deadlines); Interrupting Error Boundaries (fault trapping). | Q1: `BoundaryTimer_SubmissionDeadline`, `BoundaryTimer_ReviewSLA`, `BoundaryError_Notification`; Q2: `BoundaryTimer_OfferAcceptance`, `BoundaryError_Disbursement`. |
| **8** | Happy Path & Business-Critical Flows | Step-by-step 14-step Q1 happy path vs. 10-step Q2 happy path; critical academic clarification distinguishing Happy Path from mathematical Critical Path Method (CPM). | Q1 & Q2 default sequence flows terminating in `EndEvent_GuideAllocated` (Q1) and `EndEvent_Disbursed` (Q2). |
| **9** | Failure Path Matrix: Question 1 | Matrix of Q1 failures (F1 to F6): Trigger → Detection Element → Recovery Action → Resulting Outcome (Docs, Team rules, Plagiarism, Lapsed, Revision, Rejection). | Q1: `Task_ReturnInvalidProposal`, `Task_CoordinatorScreening`, `Task_RunSimilarityCheck`, `EndEvent_DuplicateTopic`, `EndEvent_Lapsed`. |
| **10** | Failure Path Matrix: Question 2 | Matrix of Q2 failures (L1 to L6): Trigger → Detection Element → Recovery Action → Resulting Outcome (Docs, KYC mismatch, AML flag, Credit timeout, Score reject, DTI reject). | Q2: `Task_ReturnIncompleteApp`, `Task_ManualKYC`, `Task_FraudInvestigation`, `Task_RetryCreditRequest`, `EndEvent_FraudTerminated`, `EndEvent_Rejected`. |
| **11** | Alternate Paths & Exception Loops | Visual branching: Q1 Committee Revision Loop (max 2 cycles) & Guide Decline Re-allocation; Q2 Underwriting & Collateral Re-valuation Loop (L7/L8), Counter-Offer Negotiation. | Q1: `SF_ReviseResubmit`, `Task_ManualGuideAllocation`; Q2: `Task_UnderwriterReview`, `Task_RequestCollateralValuation`, `Task_ReUnderwrite`. |
| **12** | Robustness, Recovery & Governance | 4 enterprise governance pillars: Retry limits on loops, SLA timers & escalation, human-in-the-loop fallback, Forward Error Recovery vs Backward Compensation. | Bounded loops in Q1 & Q2, non-interrupting timers, script compensation for guide release in Q1, disbursement error boundary in Q2. |
| **13** | Design Decisions, Validation & Limitations | Strict pool/lane discipline; Camunda Modeler 5.49 schema validation pass; academic limitations (DMN expansion in Q2, global Event Sub-Processes, Transactional Sub-Processes). | `MessageFlow_CreditRequest`, `MessageFlow_CreditResponse`, BPMNDI visual coordinate trees. |
| **14** | Conclusion & Academic Defence | Dual-domain synthesis (academic capstone vs. retail banking); production-ready workflow automation; formal Q&A opening. | Concluding synthesis. |

---

## 3. Ground-Truth Construct Inventory (Extracted from Both XML Files)

### 3.1 Task Types Present
* **User Tasks (👤):**
  * *Question 1:* `Task_SubmitProposal`, `Task_CoordinatorScreening`, `Task_CommitteeEvaluation`, `Task_ManualGuideAllocation`, `Task_AcknowledgeAllocation`.
  * *Question 2:* `Task_SubmitApplication`, `Task_CorrectResubmit`, `Task_ReturnIncompleteApp`, `Task_ManualKYC`, `Task_FraudInvestigation`, `Task_VerifyIncome`, `Task_UnderwriterReview`, `Task_RequestCollateralValuation`, `Task_ReUnderwrite`, `Task_GenerateOffer`, `Task_ReviewOffer`, `Task_ESign`, `Task_ReviewCounterOffer`, `Task_PrepDisbursement`, `Task_RetryDisbursement`.
* **Service Tasks (⚙️):**
  * *Question 1:* `Task_ValidateCompleteness`, `Task_ValidateTeamRules`, `Task_RunSimilarityCheck`, `Task_AutoAllocateGuide`, `Task_RecordAllocation`.
  * *Question 2:* `Task_CheckDocCompleteness`, `Task_KYCVerification`, `Task_AMLScreening`, `Task_DTIAutomatedCheck`, `Task_CalculateEligibility`, `Task_DisburseFunds`, `Task_CreateLoanAccount`, `Task_CB_GenerateReport`.
* **Send Tasks (✉️):**
  * *Question 1:* `Task_SendRevisionFeedback`, `Task_SendGuideRequest`, `Task_SendAllocationNotification`.
  * *Question 2:* `Task_RequestCreditReport`, `Task_SendOffer`, `Task_NotifyDisbursement`.
* **Intermediate Message Catch Events (📥):**
  * *Question 1:* `Catch_RevisionRequest`, `Catch_GuideAcceptance`.
  * *Question 2:* `Catch_CreditReportResponse`.
* **Business Rule Task (📊):**
  * *Question 1:* `Task_CheckGuideWorkload` (evaluates DMN guide decision table).
* **Script Task (📜):**
  * *Question 1:* `Task_LogWithdrawal` (internal rollback and allocation release).

---

### 3.2 Gateway Types Present
* **Exclusive Gateways (XOR ✕):**
  * *Question 1:* `GW_CompletenessPassed`, `GW_TeamRulesPassed`, `GW_SimilarityPassed`, `GW_CommitteeDecision`, `GW_GuideFound`, `GW_ManualAllocationSuccess`.
  * *Question 2:* `GW_DocsComplete`, `GW_KYCPass`, `GW_ManualKYCResolution`, `GW_AMLPass`, `GW_CreditScoreAcceptable`, `GW_DTIAcceptable`, `GW_EligibilityDecision`, `GW_UnderwriterDecision`, `GW_CollateralValuation`, `GW_OfferDecision`, `GW_CounterOfferAcceptance`, `GW_DisbursementRetry`.
* **Parallel Gateways (AND ✛):**
  * *Question 2:* `GW_SplitParallelChecks` (forks 3 concurrent checks) and `GW_JoinParallelChecks` (synchronizes all 3 checks).
* **Event-Based Gateway (⬡):**
  * *Question 1:* `GW_EventBasedGuideAccept` (competes guide acceptance message vs 3-day timer).

---

### 3.3 Intermediate & Boundary Events Present
* **Boundary Timers (Non-Interrupting):**
  * *Question 1:* `BoundaryTimer_ReviewSLA` (10-day committee review escalation).
  * *Question 2:* `BoundaryTimer_CreditBureau` (24h API retry), `BoundaryTimer_ESign` (48h wet-signature alert).
* **Boundary Timers (Interrupting):**
  * *Question 1:* `BoundaryTimer_SubmissionDeadline` (14-day student submission cutoff).
  * *Question 2:* `BoundaryTimer_OfferAcceptance` (7-day loan offer expiry).
* **Boundary Errors (Interrupting & Non-Interrupting):**
  * *Question 1:* `BoundaryError_Notification` (catches email/SMS server outage).
  * *Question 2:* `BoundaryError_Disbursement` (catches core banking transfer failure).

---

## 4. Verification Checklist Status

- [x] **Both Questions Included:** Question 1 (Student Project Approval) and Question 2 (Loan Origination System).
- [x] **Both Diagrams Inspected:** XML elements and visual bounds mapped from `Assignment1_BPMN_Diagram.bpmn` and `Assignment3_BPMN_Diagram.bpmn`.
- [x] **Task Types Verified:** User, Service, Send, Catch, Business Rule, Script tasks accurately categorized.
- [x] **Gateway Types Verified:** Exclusive (XOR), Parallel (AND), and Event-Based Gateways documented.
- [x] **Intermediate Events Verified:** Inline Catch vs Boundary Events (Interrupting & Non-Interrupting timers and errors).
- [x] **Happy Paths Traced:** Step-by-step journeys for both processes documented without guessing CPM durations.
- [x] **Failure Path Registers Mapped:** All failure points from F1–F11 (Q1) and L1–L12 (Q2) documented.
- [x] **Collegiate Speaker Notes Included:** Full, professional notes on all 14 slides of the `.pptx`.
- [x] **Viva Questions Guide Updated:** Formatted Word `.docx` covering both questions in depth.
- [x] **PowerPoint & PDF Generated:** Clean, tested, and verified on your system.
- [x] **Pushed to GitHub:** Synced with remote repository `Mayank-web717/Workflow-Assignment-3`.
