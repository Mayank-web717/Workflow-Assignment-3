# Presentation Content & Source Mapping Verification Report

**Project Title:** Loan Origination & Approval System  
**Course:** Workflow Automation (SRMIST)  
**Student Name:** Mayank Singh (RA2411003010116)  
**Standard:** OMG BPMN 2.0 (XML & Diagrammatic Interchange)  
**Primary Source Diagram:** `d:\BPMN\October\BPMN_Assignment_3\Assignment3_BPMN_Diagram.bpmn`  
**Rendered Source Visual:** `d:\BPMN\October\BPMN_Assignment_3\Assignment3_BPMN_Diagram.png`  
**Failure Path Register:** `d:\BPMN\October\BPMN_Assignment_3\Assignment3_Failure_Path_Register.md`  
**Justification Document:** `d:\BPMN\October\BPMN_Assignment_3\Assignment3_Justification.md`  

---

## 1. Executive Summary & Source of Truth Identification

In accordance with the project assignment document `BPMN_Project_Assignments.docx` and the workspace repository `Mayank-web717/Workflow-Assignment-3`, the source of truth for this academic presentation is **Assignment 3: Loan Origination & Approval System**.

The assignment requires modelling the full retail loan lifecycle across internal banking departments and external partners, capturing both the automated happy path and all 12 potential failure and exception scenarios (L1–L12). The presentation reflects the exact constructs, topology, IDs, and annotations implemented in the underlying BPMN 2.0 model.

---

## 2. Slide-by-Slide Content & Diagram Element Mapping

| Slide | Title | Primary Content | Mapped BPMN Elements in Diagram |
| :---: | :--- | :--- | :--- |
| **1** | Title Slide | Candidate details, institutional context, project scope, BPMN 2.0 validation badge. | Metadata mapping to Assignment 3 specification. |
| **2** | Problem Statement & Objectives | Retail loan onboarding drop-offs, regulatory KYC/AML compliance, departmental silos, API latency, BPMN 2.0 advantages. | High-level business rationale for lanes, boundaries, and parallel checks. |
| **3** | Overall BPMN 2.0 Architecture | High-res diagram render, breakdown of 7 participants (6 internal lanes + 1 external pool), process boundaries, metrics. | `Collaboration_LoanOrigination`, `Pool_Bank`, `LaneSet_Bank`, `Pool_CreditBureau`, `StartEvent_ApplyLoan`, `EndEvent_Disbursed`. |
| **4** | Task Types Used & Justification | 4 distinct task types used: User Task (human form/judgement), Service Task (automated API/computation), Send Task (outbound message), Receive Event (asynchronous incoming catch). | `Task_SubmitApplication`, `Task_KYCVerification`, `Task_RequestCreditReport`, `Catch_CreditReportResponse`, `Task_DisburseFunds`, etc. |
| **5** | Gateways & Concurrency Control | Parallel Gateway (AND split/join) for KYC, Credit Bureau & DTI checks; Exclusive Gateway (XOR) for binary/multi-tier decisions; rationale for avoiding Inclusive Gateway (OR). | `GW_SplitParallelChecks`, `GW_JoinParallelChecks`, `GW_DocsComplete`, `GW_KYCPass`, `GW_EligibilityDecision`, `GW_UnderwriterDecision`. |
| **6** | Intermediate & Boundary Events | Deep-dive into events: Inline Message Catch vs. Task Boundary Events; Non-interrupting Timers (24h SLA retry, 48h e-sign); Interrupting Timer (7d offer expiry); Interrupting Error Boundary (disbursement fault). | `Catch_CreditReportResponse`, `BoundaryTimer_CreditBureau`, `BoundaryTimer_OfferAcceptance`, `BoundaryTimer_ESign`, `BoundaryError_Disbursement`. |
| **7** | The Happy Path / Business-Critical Flow | 15-step sequential journey from application submission to NEFT/RTGS disbursement; academic clarification distinguishing Happy Path from mathematical CPM. | Sequence flow path: `SF_Start_Submit` → `Task_CheckDocCompleteness` → `GW_SplitParallelChecks` → (3 parallel branches) → `GW_JoinParallelChecks` → `Task_VerifyIncome` → `Task_CalculateEligibility` → `Task_GenerateOffer` → `Task_SendOffer` → `Task_ReviewOffer` → `Task_ESign` → `Task_PrepDisbursement` → `Task_DisburseFunds` → `EndEvent_Disbursed`. |
| **8** | Critical Failure Points (L1–L6) | Matrix of first 6 failure paths: Trigger → Detection Element → Recovery Action → Resulting Outcome (Document errors, KYC failure, AML flag, Credit timeout, Score rejection, DTI rejection). | `Task_ReturnIncompleteApp`, `Task_ManualKYC`, `Task_FraudInvestigation`, `Task_RetryCreditRequest`, `EndEvent_Lapsed`, `EndEvent_FraudTerminated`, `EndEvent_Rejected`. |
| **9** | Alternate & Exception Paths (L7–L12) | Underwriter borderline review & Collateral re-valuation loop (L7/L8); Offer expiry (L9); Counter-offer & withdrawal (L10); E-sign delay (L11); Core banking disbursement fault (L12). | `Task_UnderwriterReview`, `Task_RequestCollateralValuation`, `Task_ReUnderwrite`, `Task_ReviewCounterOffer`, `Task_RetryDisbursement`, `EndEvent_OfferExpired`, `EndEvent_Withdrawn`. |
| **10** | Robustness, Governance & Recovery | 4 pillars: Retry limits on loops, SLA timers & escalation, human-in-the-loop fallback, technical fault trapping; theoretical distinction between forward Error Recovery and backward Transactional Compensation. | Loop bounds on `Task_CorrectResubmit`, non-interrupting timers, `BoundaryError_Disbursement`, `EndEvent_DisbursementFailed`. |
| **11** | Design Decisions, Validation & Limitations | Strict pool/lane discipline (sequence flows never cross pools; message flows only); Camunda 5.49 schema validation pass; honest discussion of limitations (DMN extraction, Event Sub-Processes, Transactional Sub-Processes). | `MessageFlow_CreditRequest`, `MessageFlow_CreditResponse`, BPMNDI diagram interchange elements. |
| **12** | Conclusion & Academic Synthesis | Synthesis of enterprise loan workflow automation; value of executable BPMN 2.0 models; thank you and formal Q&A opening. | Concluding synthesis. |

---

## 3. Ground-Truth Construct Inventory (Extracted from Diagram XML)

### 3.1 Task Types Actually Present
* **User Task (👤):**
  * `Task_SubmitApplication` (Applicant)
  * `Task_CorrectResubmit` (Applicant)
  * `Task_ReturnIncompleteApp` (Loan Officer)
  * `Task_ManualKYC` (Fraud & Compliance)
  * `Task_FraudInvestigation` (Fraud & Compliance)
  * `Task_VerifyIncome` (Loan Officer)
  * `Task_UnderwriterReview` (Underwriter)
  * `Task_RequestCollateralValuation` (Underwriter)
  * `Task_ReUnderwrite` (Underwriter)
  * `Task_GenerateOffer` (Loan Officer)
  * `Task_ReviewOffer` (Applicant)
  * `Task_ESign` (Applicant)
  * `Task_ReviewCounterOffer` (Loan Officer)
  * `Task_FinalizeNegotiatedTerms` (Loan Officer)
  * `Task_SubmitWithdrawal` (Applicant)
  * `Task_PrepDisbursement` (Operations)
  * `Task_RetryDisbursement` (Operations)
* **Service Task (⚙️):**
  * `Task_CheckDocCompleteness` (Core Banking)
  * `Task_KYCVerification` (Fraud & Compliance)
  * `Task_AMLScreening` (Fraud & Compliance)
  * `Task_DTIAutomatedCheck` (Core Banking)
  * `Task_CalculateEligibility` (Core Banking)
  * `Task_DisburseFunds` (Core Banking)
  * `Task_CreateLoanAccount` (Core Banking)
  * `Task_CB_GenerateReport` (Credit Bureau External Pool)
* **Send Task (✉️):**
  * `Task_RequestCreditReport` (Core Banking)
  * `Task_SendOffer` (Core Banking)
  * `Task_NotifyDisbursement` (Core Banking)
* **Intermediate Message Catch Event / Receive Task (📥):**
  * `Catch_CreditReportResponse` (Core Banking)

*(Note: Script Tasks and Manual Tasks are not present in the model; their absence is justified because business logic relies on enterprise microservices, and physical activities are formally tracked via User Tasks).*

---

### 3.2 Gateway Types Actually Present
* **Parallel Gateway (AND ✛):**
  * `GW_SplitParallelChecks`: Forks single flow into 3 concurrent verification checks (KYC/AML, Credit Bureau, DTI).
  * `GW_JoinParallelChecks`: Synchronizes and waits for all 3 concurrent checks before advancing to income verification.
* **Exclusive Gateway (XOR ✕):**
  * `GW_DocsComplete`: Binary branch (Complete vs. Incomplete).
  * `GW_KYCPass`: Mutually exclusive branch (Pass vs. Fail).
  * `GW_ManualKYCResolution`: Mutually exclusive branch (Resolved vs. Unresolvable).
  * `GW_AMLPass`: Mutually exclusive branch (Pass vs. Flagged).
  * `GW_CreditScoreAcceptable`: Mutually exclusive branch (Pass vs. Fail).
  * `GW_DTIAcceptable`: Mutually exclusive branch (Pass vs. Fail).
  * `GW_EligibilityDecision`: Three-way exclusive branch (Auto-Approve vs. Manual Review vs. Reject).
  * `GW_UnderwriterDecision`: Three-way exclusive branch (Approve vs. Require Collateral vs. Reject).
  * `GW_CollateralValuation`: Binary branch (Sufficient LTV vs. Insufficient LTV).
  * `GW_OfferDecision`: Three-way exclusive branch (Accept vs. Counter-Offer vs. Withdraw).
  * `GW_CounterOfferAcceptance`: Binary branch (Bank Accepts vs. Bank Rejects).
  * `GW_DisbursementRetry`: Binary branch (Retry Successful vs. Permanent Failure).

*(Note: Inclusive Gateways (OR) are intentionally absent because loan decisions are mutually exclusive; an application cannot be simultaneously approved and rejected).*

---

### 3.3 Intermediate & Boundary Events Actually Present
* **Intermediate Message Catch Event:**
  * `Catch_CreditReportResponse`: Inline intermediate event in Core Banking lane, waiting for asynchronous credit report from Credit Bureau pool.
* **Non-Interrupting Boundary Timer Event:**
  * `BoundaryTimer_CreditBureau`: Attached to `Task_RequestCreditReport` (24h timeout); triggers parallel retry request without aborting the wait.
  * `BoundaryTimer_ESign`: Attached to `Task_ESign` (48h timeout); triggers parallel manual wet-signature alert to operations without cancelling digital signing capability.
* **Interrupting Boundary Timer Event:**
  * `BoundaryTimer_OfferAcceptance`: Attached to `Task_ReviewOffer` (7d timeout); cancels active offer review and diverts token to `EndEvent_OfferExpired`.
* **Interrupting Boundary Error Event:**
  * `BoundaryError_Disbursement`: Attached to `Task_DisburseFunds` Service Task; catches core banking / RTGS transaction exceptions and diverts token to `Task_RetryDisbursement`.

---

## 4. Alternate & Exception Paths Verified

| ID | Exception Case | Mechanism | Terminal / Rejoining State |
| :---: | :--- | :--- | :--- |
| **L1** | Document Incompleteness | XOR GW → `Task_ReturnIncompleteApp` → Loop back to `Task_CorrectResubmit` | Re-enters completeness check OR `EndEvent_Lapsed` |
| **L2** | KYC Identity Mismatch | XOR GW → `Task_ManualKYC` → XOR GW | Rejoins AML flow OR `EndEvent_FraudTerminated` |
| **L3** | AML / Watchlist Flag | XOR GW → `Task_FraudInvestigation` | Terminal `EndEvent_FraudTerminated` |
| **L4** | Credit Bureau Timeout | Non-interrupting timer → Retry Loop | Successful report unblocks catch OR manual assessment |
| **L5** | Credit Score Rejection | XOR GW feeds subprime score into Parallel Join | Eligibility gateway routes to `EndEvent_Rejected` |
| **L6** | Excessive DTI Ratio | Automated DTI check fails → XOR GW | Terminal `EndEvent_Rejected` |
| **L7** | Borderline Risk Underwriting | Eligibility GW routes to `Task_UnderwriterReview` | Overrides to Offer OR routes to Collateral (L8) OR `EndEvent_Rejected` |
| **L8** | Collateral Valuation Loop | Appraiser valuation → XOR GW → `Task_ReUnderwrite` loop | Satisfactory LTV re-enters approval OR `EndEvent_Rejected` |
| **L9** | Offer Acceptance Expiry | Interrupting Timer Boundary (7 days) on `Task_ReviewOffer` | Terminal `EndEvent_OfferExpired` |
| **L10** | Applicant Negotiation / Withdrawal | Applicant selects 'Counter-Offer' or 'Withdraw' | Counter-offer negotiation OR Terminal `EndEvent_Withdrawn` |
| **L11** | E-Signature Latency | Non-interrupting Timer Boundary (48 hours) | Triggers Operations wet-signature prep; digital signing remains open |
| **L12** | Core Banking Disbursement Fault | Interrupting Error Boundary on `Task_DisburseFunds` | Operations retry channel OR Terminal `EndEvent_DisbursementFailed` |

---

## 5. Modelling Limitations Discovered & Academic Reflection

1. **Service Task Hardcoding vs. DMN Decision Tables:**
   * *Observation:* Risk scoring and DTI threshold calculations are currently modelled as Service Tasks executing internal code/APIs.
   * *Improvement:* In an enterprise production deployment, these should be separated into Decision Model and Notation (DMN) decision tables invoked via **Business Rule Tasks**, enabling credit risk officers to adjust score cut-offs without redeploying code.
2. **Ad-Hoc Withdrawal vs. Global Event Sub-Processes:**
   * *Observation:* Applicant withdrawal is currently modelled via an Exclusive Gateway following offer review.
   * *Improvement:* If an applicant wishes to withdraw earlier (e.g., during underwriting), the current model does not show an explicit escape branch. Implementing an **Interrupting Event Sub-Process** with a Message Start Event would allow global withdrawal across all active stages.
3. **Forward Error Recovery vs. Transactional Compensation:**
   * *Observation:* The disbursement failure uses an Error Boundary Event for forward recovery.
   * *Improvement:* If loan booking involves debiting credit reserves, reserving funds, and issuing promissory notes across distributed ledgers, a **Transactional Sub-Process** with explicit Cancel and Compensation Intermediate Events would provide atomic rollback guarantees.

---

## 6. Verification Checklist Status

- [x] Identified correct assignment: **Assignment 3: Loan Origination & Approval System**
- [x] Inspected actual BPMN 2.0 XML and diagram visual
- [x] Accurately catalogued all Task Types actually present (User, Service, Send, Receive Catch)
- [x] Accurately catalogued all Gateway Types (Parallel AND Split/Join, Exclusive XOR)
- [x] Accurately classified Intermediate Events vs. Task Boundary Events
- [x] Distinguished Interrupting vs. Non-Interrupting boundary timers
- [x] Traced 15-step sequential Happy Path without inventing artificial CPM durations
- [x] Mapped all 12 failure triggers, detection mechanisms, and recovery actions
- [x] Included concise collegiate speaker notes on every PowerPoint slide
- [x] Created project-specific viva questions and model answers in Word `.docx` format
- [x] Verified PPTX open and successful conversion to PDF
- [x] Output cleanly organized in `d:\BPMN\October\Presentation\`
