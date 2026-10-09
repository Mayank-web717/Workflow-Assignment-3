# Assignment 3 – Task Type & Gateway Justification
## Loan Origination & Approval System

## Process Diagram Preview

![Assignment 3 - Loan Origination & Approval System Diagram](Assignment3_BPMN_Diagram.png)

---

## Task Type Justifications

| Task Name | Task Type | Justification |
|-----------|-----------|---------------|
| Submit Loan Application and Upload Documents | **User Task** | Applicant manually fills the form and uploads supporting documents through the portal. Direct human action — User Task. |
| Correct and Resubmit Documents (L1) | **User Task** | Applicant manually corrects errors and resubmits after receiving feedback. Human action — User Task. |
| Check Document Completeness (L1) | **Service Task** | System automatically checks document presence, format, and minimum content rules against a predefined schema. Fully automated — Service Task. |
| Return Application – Request Missing Documents | **User Task** | Loan Officer manually communicates with applicant, specifying which documents are missing. Human interaction — User Task. |
| KYC Identity Verification (L2) | **Service Task** | System integrates with a KYC API (CKYC/UIDAI/government database) to automatically verify identity. Automated external service call — Service Task. |
| Manual KYC Verification (L2) | **User Task** | Compliance Officer manually reviews identity documents when automated KYC fails. Human adjudication — User Task. |
| AML and Fraud Screening (L3) | **Service Task** | System automatically calls AML/watchlist APIs (OFAC, UN sanctions, internal fraud DB). Automated — Service Task. |
| Fraud Investigation (L3) | **User Task** | Compliance team manually investigates flagged cases, reviews transaction history, contacts applicant. Human investigation — User Task. |
| Request Credit Report from Credit Bureau (L4) | **Send Task** | System sends a structured credit report request message to the external Credit Bureau pool. Outbound message — Send Task. |
| Receive Credit Report (L4) | **Intermediate Message Catch Event** | System waits for the Credit Bureau's asynchronous response. Message-based waiting — Intermediate Message Catch Event. |
| Income and DTI Automated Check (L6) | **Service Task** | System calculates DTI from submitted income and liability data. Automated computation — Service Task. |
| Verify Income, Employment and Bank Statements (L6) | **User Task** | Loan Officer manually verifies income documents, calls employers, and cross-checks bank statements. Human verification — User Task. |
| Calculate Eligibility and Risk Score | **Service Task** | System applies risk scoring model (decision table/rules engine) to combined verification results. Automated — Service Task. |
| Underwriter Full Manual Review (L7) | **User Task** | Underwriter manually reviews the complete application, financials, and risk profile for borderline cases. Expert human judgement — User Task. |
| Request Collateral Valuation (L8) | **User Task** | Underwriter/Officer requests a valuation report from an appraiser. Human coordination — User Task. |
| Re-Underwrite with Revised Data (L8) | **User Task** | Underwriter re-evaluates with revised collateral data. Human re-assessment — User Task. |
| Generate Loan Offer Letter | **User Task** | Loan Officer generates the offer letter using system template but reviews terms before sending. Human oversight — User Task. |
| Send Loan Offer to Applicant (L9) | **Send Task** | System automatically dispatches the offer letter to applicant via email/portal. Outbound message — Send Task. |
| Review Loan Offer (L9) | **User Task** | Applicant reads and evaluates the offer terms. Direct human decision — User Task. |
| E-Sign Loan Agreement (L11) | **User Task** | Applicant digitally signs via an e-signature platform. Human action with digital tool — User Task. |
| Review Counter-Offer Request | **User Task** | Loan Officer manually evaluates the applicant's counter-offer request and negotiates. Human negotiation — User Task. |
| Finalize Agreement with Negotiated Terms | **User Task** | Loan Officer finalizes the revised agreement document. Human action — User Task. |
| Submit Withdrawal Request (L10) | **User Task** | Applicant manually submits withdrawal through the portal or in writing. Human action — User Task. |
| Prepare Disbursement Instructions | **User Task** | Operations staff verify account details and prepare disbursement instructions. Human verification — User Task. |
| Disburse Loan Funds (L12) | **Service Task** | Core banking system automatically initiates NEFT/RTGS transfer. Fully automated — Service Task. |
| Retry Disbursement (L12) | **User Task** | Operations manually retries via alternative channel or contacts IT support. Human fallback — User Task. |
| Create Loan Account | **Service Task** | Core banking system automatically creates the loan account record. Automated — Service Task. |
| Notify Applicant of Successful Disbursement | **Send Task** | System sends automated SMS/email confirmation to applicant. Outbound message — Send Task. |
| Credit Bureau: Generate Credit Report | **Service Task** | Credit Bureau's internal system generates the report from its database. Automated — Service Task. |

---

## Gateway Justifications

| Gateway | Type | Justification |
|---------|------|---------------|
| Start Parallel Verification Checks | **Parallel Gateway (AND Split)** | KYC, Credit Bureau request, and DTI check are all independent and can run simultaneously. Parallel Gateway is mandatory here — all three must complete before proceeding. This is the key justification for Parallel Gateway over any other type. |
| All Parallel Checks Complete | **Parallel Gateway (AND Join)** | Must wait for ALL three parallel branches (KYC/AML, Credit Bureau, DTI) to complete before proceeding to income verification and eligibility scoring. Parallel Join ensures synchronisation. |
| Documents Complete? | **Exclusive Gateway (XOR)** | Binary: either complete (proceed) or not (return). One path only. |
| KYC Passed? (L2) | **Exclusive Gateway (XOR)** | Three branches but mutually exclusive: pass → AML; fail → manual KYC; unresolvable → terminate. |
| AML / Fraud Passed? (L3) | **Exclusive Gateway (XOR)** | Pass or flag — one outcome. |
| Credit Score Acceptable? (L5) | **Exclusive Gateway (XOR)** | Pass or fail — feeds into parallel join. The score result contributes to the eligibility calculation. |
| DTI Ratio Acceptable? (L6) | **Exclusive Gateway (XOR)** | Pass → parallel join; fail → immediate reject. Binary outcome. |
| Eligibility Decision (L5/L6/L7) | **Exclusive Gateway (XOR)** | Three mutually exclusive outcomes: auto-approve (high score), manual review (borderline), reject (low score). XOR with three branches is appropriate. |
| Underwriter Decision (L7/L8) | **Exclusive Gateway (XOR)** | Three mutually exclusive outcomes: approve, require collateral, reject. |
| Collateral Valuation OK? (L8) | **Exclusive Gateway (XOR)** | Collateral either meets LTV requirement (approve) or doesn't (re-underwrite). |
| Applicant Decision (Accept/Counter/Withdraw) | **Exclusive Gateway (XOR)** | Three mutually exclusive choices: accept, counter-offer, or withdraw. |
| Counter-Offer Accepted by Bank? | **Exclusive Gateway (XOR)** | Bank either accepts (new offer) or rejects (application rejected). |
| Retry Disbursement Successful? (L12) | **Exclusive Gateway (XOR)** | After retry, either success (create account) or permanent failure (error end event). |

---

## Boundary Event Justifications

| Event | Type | Justification |
|-------|------|---------------|
| Offer Acceptance Timeout – 7 Days (L9) | **Interrupting Timer Boundary** | If the applicant does not respond within 7 days, the offer is legally expired. Interrupting boundary cancels the waiting task and permanently terminates this path. |
| E-Signature Timeout – 48 Hours (L11) | **Non-interrupting Timer Boundary** | E-signature continues to be available, but the timeout triggers parallel manual intervention path. Non-interrupting preserves both paths. |
| Credit Bureau Response Timeout – 24 Hours (L4) | **Non-interrupting Timer Boundary** | The credit bureau request may still succeed; the timeout triggers a retry without cancelling the original request context. Non-interrupting is correct. |
| Disbursement System Error (L12) | **Interrupting Error Boundary** | When a critical system error occurs during disbursement, the task must be cancelled and the error must be handled. Interrupting Error Boundary is the correct BPMN 2.0 construct for catching thrown errors. |

---

## External Pool / Message Flow Justification

| Element | Justification |
|---------|---------------|
| Credit Bureau (External Pool) | The Credit Bureau is an external organisation with its own independent process. BPMN 2.0 requires external participants to be modelled as separate Pools connected via Message Flows (not Sequence Flows). This correctly represents the asynchronous, cross-organisational communication. |
| Message Flow: Loan → Credit Bureau | Models the outbound credit report request crossing organisational boundaries. |
| Message Flow: Credit Bureau → Loan | Models the asynchronous credit report response received by the bank's Core Banking System. |

---

## Inclusive Gateway Note

The eligibility scoring gateway uses an **Exclusive Gateway** (not Inclusive) because exactly one of the three outcomes (auto-approve, manual review, reject) is selected based on a defined score range. An Inclusive Gateway would apply if multiple optional checks could be triggered simultaneously (e.g., if both KYC and income checks could optionally be performed based on risk profile). In this model, the parallel gateway before the checks correctly handles the multi-check simultaneity, making the eligibility gateway strictly exclusive.

---

*Generated for Academic BPMN 2.0 Assignment – Assignment 3*
