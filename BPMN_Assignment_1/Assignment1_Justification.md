# Assignment 1 – Task Type & Gateway Justification
## Student Project Approval & Allocation System

## Process Diagram Preview

![Assignment 1 - Student Project Approval & Allocation System Diagram](Assignment1_BPMN_Diagram.png)

---

## Task Type Justifications

| Task Name | Task Type | Justification |
|-----------|-----------|---------------|
| Prepare and Submit Project Proposal | **User Task** | Requires direct student interaction — the student fills out and submits the proposal form manually through the portal. A User Task correctly models human-driven work. |
| Validate Document Completeness | **Service Task** | Automated system check: the Project Management System compares submitted documents against a required checklist without human intervention. Service Task represents automated system execution. |
| Validate Team Composition Rules | **Service Task** | Rule-based automated check performed by the system (e.g., minimum members, eligibility, batch restrictions). No human decision involved. |
| Screen Proposal | **User Task** | The Project Coordinator manually reviews the proposal for eligibility, coherence, and compliance. Requires human judgement — User Task is appropriate. |
| Run Similarity and Duplicate Topic Check | **Service Task** | The system automatically invokes a plagiarism / similarity API or internal engine. This is fully automated and externally triggered — Service Task is correct. |
| Evaluate Project Proposal (Committee) | **User Task** | Committee members collectively read, discuss, and evaluate proposals. This requires human deliberation and produces a human decision — User Task. |
| Send Revision Feedback to Student | **Send Task** | The Committee triggers a message (email / portal notification) to the student. The process sends and moves on. Send Task correctly models outbound message dispatch. |
| Receive Revision Request (Student) | **Intermediate Message Catch Event** | The student's lane must wait for the incoming revision message before the student can act. An Intermediate Message Catch Event models waiting for an external trigger. |
| Check Guide Availability, Workload and Domain Match | **Business Rule Task** | This evaluation is driven by a decision table (DMN): guide availability, student domain, and guide workload cap. Business Rule Task is the correct type when a DMN/rule engine drives the decision. |
| Auto-Allocate Guide | **Service Task** | The system automatically selects and assigns the guide based on business rule output. No human action required — Service Task. |
| Send Guide Allocation Request | **Send Task** | The system dispatches a message to the prospective guide requesting acceptance. Outbound message dispatch = Send Task. |
| Guide Accepts Allocation | **Intermediate Message Catch Event** | The process waits in the Guide lane for a message (response) from the faculty guide. Intermediate Message Catch Event models this wait. |
| Manually Assign Available Guide (F8 Fallback) | **User Task** | The Coordinator manually identifies and assigns a guide when automated allocation fails. Human judgement and manual database query — User Task. |
| Record Guide Allocation | **Service Task** | System automatically persists the allocation record in the database after guide acceptance. Automated — Service Task. |
| Send Allocation Notification to Student | **Send Task** | System dispatches an automated notification to the student. Outbound message — Send Task. |
| Log Withdrawal and Trigger Compensation | **Script Task** | A scripted operation: the system logs the withdrawal event and triggers compensation handlers to release the guide pre-assignment. Script Task correctly models automated scripted logic. |
| Escalate Review Delay to HoD | **User Task** | The Coordinator manually escalates via email or phone to the Head of Department. Human action — User Task. |

---

## Gateway Justifications

| Gateway | Type | Justification |
|---------|------|---------------|
| Documents Complete? | **Exclusive Gateway (XOR)** | Exactly one outcome: either documents are complete (proceed) or incomplete (return). XOR because only one path can be taken. |
| Team Rules Satisfied? | **Exclusive Gateway (XOR)** | Same logic: team is either valid or invalid — one path only. |
| Screening Passed? | **Exclusive Gateway (XOR)** | Coordinator's screening yields a single pass or fail decision. |
| Topic Unique? (F3) | **Exclusive Gateway (XOR)** | The topic either passes the similarity threshold or it doesn't — binary decision, one path. |
| Committee Decision: Approve / Revise / Reject? | **Exclusive Gateway (XOR)** | Three mutually exclusive outcomes. Only one of Approve, Revise, or Reject is chosen. XOR correctly models mutually exclusive multi-path decisions. |
| Proceed with Revision or Withdraw? | **Exclusive Gateway (XOR)** | Student chooses exactly one: proceed with the revised proposal or withdraw. |
| Suitable Guide Found? | **Exclusive Gateway (XOR)** | Either a suitable guide exists in the system or it doesn't. One path. |
| Awaiting Guide Response (F9) | **Event-Based Gateway** | The process does not know which event will arrive first — the guide's acceptance message or a timeout event. Event-Based Gateway correctly models the process waiting for one of several competing events. |
| Manual Allocation Successful? | **Exclusive Gateway (XOR)** | After manual search, either the coordinator found a guide (proceed) or not (end process). One of two outcomes. |

---

## Boundary Event Justifications

| Event | Type | Justification |
|-------|------|---------------|
| Submission Deadline Expired (F4) | **Interrupting Timer Boundary Event** | If the student does not submit within 14 days, the process must terminate that path permanently. Interrupting boundary correctly cancels the task and redirects. |
| Guide Response Timeout – 3 Days (F9) | **Non-interrupting Timer Boundary Event** | The timeout triggers fallback (manual allocation) but the original send task can still complete if the guide responds simultaneously. Non-interrupting preserves the original flow. |
| Review SLA Exceeded – 10 Days (F7) | **Non-interrupting Timer Boundary Event** | Review continues (the committee may still finish) but escalation is triggered in parallel. Non-interrupting allows both paths to remain active. |
| Notification System Failure (F10) | **Non-interrupting Error Boundary Event** | System errors during notification trigger manual recovery, but the original notification attempt need not be cancelled immediately. Non-interrupting preserves the flow context. |

---

## Sub-Process Justifications

No collapsed sub-processes were used in the final flat layout to ensure maximum readability for grading. Instead, committee review and guide allocation steps are modelled as explicit sequential tasks within their respective lanes. This keeps gateway labels and failure paths visible without needing to open sub-process containers.

---

## Message Flow Justification

| Message | Between | Justification |
|---------|---------|---------------|
| Revision Request | Committee → Student | Models the asynchronous communication where the committee sends and the student receives at a later point. |
| Guide Acceptance | Guide → System | Models the asynchronous guide response to the allocation request. |

---

*Generated for Academic BPMN 2.0 Assignment – Assignment 1*
