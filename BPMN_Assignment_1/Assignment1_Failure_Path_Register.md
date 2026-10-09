# Assignment 1 – Failure Path Register
## Student Project Approval & Allocation System

---

| ID | Failure Point | Cause / Trigger | Solution (BPMN Action) | BPMN Construct | Final Outcome |
|----|--------------|-----------------|------------------------|---------------|---------------|
| **F1** | Proposal Validation – Document Completeness | Student submits a proposal with missing sections, absent signatures, or incomplete forms | Service Task checks completeness; if incomplete, Exclusive Gateway routes to Coordinator's "Return Proposal as Invalid" task; student notified | Service Task + Exclusive Gateway + Send Notification | Process ends at **EndEvent: Invalid Proposal Returned** |
| **F2** | Proposal Validation – Team Rule Violation | Team size below minimum, mixed-batch composition, duplicate team member registration, or ineligible member | After completeness check passes, a second Service Task validates team rules; failure routes to same "Return Proposal" task | Service Task + Exclusive Gateway | Process ends at **EndEvent: Invalid Proposal Returned** |
| **F3** | Duplicate / Plagiarised Topic | System's similarity engine finds ≥ 70% match with an existing or approved project topic | Service Task runs similarity check; Exclusive Gateway: if duplicate → route to **EndEvent: Duplicate Topic** | Service Task + Exclusive Gateway | Process ends at **EndEvent: Duplicate / Plagiarised Topic** |
| **F4** | Proposal Submission Deadline Expired | Student starts preparing the proposal but does not submit within the 14-day window | Non-interrupting Timer Boundary Event on "Prepare and Submit Proposal" task fires at 14 days → routes to **EndEvent: Proposal Lapsed** | Boundary Timer Event (interrupting) | Process ends at **EndEvent: Proposal Lapsed** |
| **F5** | Committee Requests Revision | Review Committee finds the proposal scientifically or structurally weak but not outright rejectable | Exclusive Gateway in Committee decision: "Requires Revision" → Send Task sends revision feedback to student → Student receives via Intermediate Message Catch Event → Revises and resubmits through similarity check loop | Exclusive Gateway + Send Task + Intermediate Message Catch Event + Loop | Process loops back to Similarity Check (retry path) or student withdraws |
| **F6** | Proposal Rejected by Committee | Proposal fails to meet academic or institutional criteria | Exclusive Gateway: "Rejected" branch → EndEvent | Exclusive Gateway + Terminate End Event | Process ends at **EndEvent: Proposal Rejected** |
| **F7** | Review Delay – Committee SLA Exceeded | Committee does not complete evaluation within 10 days (SLA) | Non-interrupting Timer Boundary Event on "Evaluate Proposal" task fires at 10 days → Coordinator escalates to HoD → HoD triggers re-evaluation | Non-interrupting Boundary Timer + Escalation User Task | Re-evaluation starts; if approved → continue; if still delayed → coordinator escalates again |
| **F8** | No Guide Available | Business Rule check finds no guide with matching domain, acceptable workload, or availability | Exclusive Gateway "Suitable Guide Found?": No → Coordinator performs Manual Guide Allocation; Exclusive Gateway "Manual Allocation Successful?": No → EndEvent | Business Rule Task + Exclusive Gateway + User Task + Exclusive Gateway | Process ends at **EndEvent: No Guide Available After All Attempts** OR recovers via manual allocation |
| **F9** | Guide Declines or Remains Silent | Guide does not respond within 3 days or explicitly declines the allocation request | Non-interrupting Timer Boundary Event on Send Allocation Request fires at 3 days; also Event-Based Gateway waits for Accept message or timeout → fallback to Manual Guide Allocation | Boundary Timer Event + Event-Based Gateway + Intermediate Message Catch + User Task | Falls back to Manual Allocation (F8 fallback); if successful → continue; else → EndEvent |
| **F10** | Notification / System Failure | The system cannot deliver the allocation notification to the student (email/SMS/portal failure) | Non-interrupting Error Boundary Event on Send Notification task captures system errors → routes to **EndEvent: System Failure – Manual Recovery Required** | Non-interrupting Error Boundary Event + Error End Event | Process ends at **EndEvent: System Failure** (manual recovery by IT/Coordinator required) |
| **F11** | Withdrawal After Approval | After the Committee approves but before guide confirmation is finalised, the student/team decides to withdraw | Student selects "Withdraw" on revision gateway (or initiates withdrawal independently) → Script Task logs withdrawal and triggers compensation to release any guide pre-assignment → EndEvent | Exclusive Gateway + Script Task (with Compensation logic) + End Event | Process ends at **EndEvent: Proposal Withdrawn** |

---

### Notes on Additional Realistic Failures Considered but Absorbed into Existing Categories

| Additional Risk | Absorbed Into | Rationale |
|----------------|---------------|-----------|
| Guide rejects due to conflict of interest | F9 (Guide Declines) | Same trigger and BPMN path |
| System crash during similarity check | F10 (System Failure) | Error boundary pattern applies |
| HoD unavailable during escalation | F7 (Review Delay) | Timer re-fires; escalation path repeats |
| Student submits wrong file format | F1 (Completeness Check) | Completeness validation catches format errors |

---
*Generated for Academic BPMN 2.0 Assignment – Assignment 1*
