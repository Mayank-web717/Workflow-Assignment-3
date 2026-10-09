# Assignment 3 – Failure Path Register
## Loan Origination & Approval System

---

| ID | Failure Point | Cause / Trigger | Solution (BPMN Action) | BPMN Construct | Final Outcome |
|----|--------------|-----------------|------------------------|---------------|---------------|
| **L1** | Document Completeness Check | Applicant submits application with missing documents (ID proof, income proof, bank statements, etc.) or wrong file format | Service Task checks completeness; Exclusive Gateway: if incomplete → Loan Officer returns application with document checklist; applicant corrects and resubmits (loop); if no response within lapse period → End Event | Service Task + Exclusive Gateway + User Task (return) + Retry Loop + Timer-driven lapse | **Retry Loop** (correction) OR **EndEvent: Application Lapsed** |
| **L2** | KYC Verification Failure | Applicant identity cannot be automatically verified (name/DOB mismatch, expired ID, foreign national rules) | Service Task (KYC API); Exclusive Gateway: if KYC fails → Manual KYC by Compliance Officer; if still unresolvable → Fraud Terminated end; if resolved → proceed to AML | Service Task + Exclusive Gateway + User Task (manual KYC) | Manual resolution → continues OR **EndEvent: Fraud Terminated** |
| **L3** | Fraud / AML Screening Flag | Applicant or related parties appear on AML watchlists, PEP lists, or fraud databases | Service Task (AML API); Exclusive Gateway: flagged → Fraud Investigation User Task → Application Terminated | Service Task + Exclusive Gateway + User Task (fraud investigation) + Terminate End Event | **EndEvent: Application Terminated – Fraud/AML Violation** |
| **L4** | Credit Bureau Failure / Timeout | Credit Bureau system is unresponsive, returns error, or times out within 24 hours | Send Task to Credit Bureau; Non-interrupting Timer Boundary Event fires at 24 hours → retry request; Intermediate Message Catch Event waits for response; retry loop up to limit | Send Task + Boundary Timer Event (non-interrupting) + Intermediate Message Catch Event + Retry Loop | On successful response → continues; persistent failure → manual credit assessment fallback |
| **L5** | Credit Score / Risk Failure | Credit Bureau returns report showing score below minimum threshold (e.g., < 650) | Exclusive Gateway after credit score check: low score → feeds into parallel join; eligibility calculator uses score to determine manual review or reject; Exclusive Gateway on eligibility: reject path | Exclusive Gateway + Parallel Join + Exclusive Gateway (eligibility) | **EndEvent: Loan Rejected** (via eligibility scoring) |
| **L6** | Income / DTI Ratio Failure | Applicant's debt-to-income ratio exceeds policy limits (e.g., > 50%) or income is insufficient for requested loan amount | Service Task (automated DTI calculation) as parallel check; Exclusive Gateway: if DTI too high → terminate (reject); parallel join collects results | Service Task + Exclusive Gateway (DTI fail → Reject end) + Parallel Gateway | **EndEvent: Loan Rejected** |
| **L7** | High-Value / Borderline Case – Manual Review | Application score falls in the borderline range or loan amount exceeds auto-approval threshold | Exclusive Gateway on eligibility score: "Manual Review" branch → Underwriter Review User Task; Exclusive Gateway on underwriter decision: Approve / Require Collateral / Reject | Exclusive Gateway + User Task (underwriter) + Exclusive Gateway (decision) | Approve → continues; Collateral required → L8 path; Reject → **EndEvent: Rejected** |
| **L8** | Collateral Valuation Failure | Collateral provided by applicant does not meet minimum LTV (loan-to-value) ratio or valuation is disputed | User Task: Request Collateral Valuation; Exclusive Gateway: if insufficient → Re-underwrite task which loops back to Underwriter Review; if acceptable → approve | User Task + Exclusive Gateway + User Task (re-underwrite) + Loop | On satisfactory collateral → approval; if still insufficient after re-underwrite → **EndEvent: Rejected** |
| **L9** | Offer Acceptance Timeout | Applicant does not respond to the loan offer within 7 days | Interrupting Timer Boundary Event on "Review Offer" task fires at 7 days → EndEvent: Offer Expired | Interrupting Boundary Timer Event + End Event | **EndEvent: Loan Offer Expired – No Response** |
| **L10** | Withdrawal at Any Stage | Applicant decides to withdraw the application before disbursement (after offer review or at any active stage) | Exclusive Gateway on offer decision: "Withdraw" branch → User Task "Submit Withdrawal Request" → EndEvent Withdrawn; process includes compensation/archive of all collected data | Exclusive Gateway + User Task + End Event | **EndEvent: Application Withdrawn by Applicant** |
| **L11** | E-Signature Failure / Timeout | Applicant fails to e-sign within 48 hours, e-signature platform is unavailable, or signature is rejected | Non-interrupting Timer Boundary Event on e-sign task at 48 hours → triggers manual intervention path (Operations prepares disbursement manually with wet signature option) | Non-interrupting Boundary Timer Event + User Task (manual intervention) | Manual agreement finalization → continues to disbursement |
| **L12** | Disbursement Failure | Core banking system error, recipient account frozen/invalid, NEFT/RTGS failure, or daily transaction limit exceeded | Interrupting Error Boundary Event on "Disburse Funds" task captures system error → Retry Disbursement User Task (fallback channel, alternate bank route); Exclusive Gateway: retry success → continue; retry failure → EndEvent | Interrupting Error Boundary Event + User Task (retry) + Exclusive Gateway + Error End Event | Retry → continues; persistent failure → **EndEvent: Disbursement Failed – Manual Intervention Required** |

---

### Additional Realistic Failure Paths Identified

| Additional Risk | Absorbed Into | BPMN Solution |
|----------------|---------------|---------------|
| Income document forgery detected | L3 (Fraud Screening) | AML/fraud flag path handles document fraud |
| Guarantor verification failure | L2 (KYC) | Manual KYC path covers guarantor verification |
| Collateral insurance lapse | L8 (Collateral) | Re-underwriting addresses insurance requirements |
| Applicant deceased during processing | L10 (Withdrawal) | Process treated as withdrawal with special end event |
| Regulatory hold (RBI directive) | L3 (Compliance) | Compliance team investigation path covers regulatory blocks |

---
*Generated for Academic BPMN 2.0 Assignment – Assignment 3*
