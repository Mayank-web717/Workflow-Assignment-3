# BPMN 2.0 Process Modelling Assignments

This repository contains submission-ready BPMN 2.0 models, failure/exception path registers, task/gateway justifications, and high-resolution diagram renders for all three academic assignments.

---

## 📂 Repository Structure

### 1. [Assignment 1 – Student Project Approval & Allocation System](./BPMN_Assignment_1/)
* **BPMN 2.0 Diagram:** [Assignment1_BPMN_Diagram.bpmn](./BPMN_Assignment_1/Assignment1_BPMN_Diagram.bpmn)
* **Diagram Preview:** ![Assignment 1 Preview](./BPMN_Assignment_1/Assignment1_BPMN_Diagram.png)
* **Failure Path Register (F1–F11):** [Assignment1_Failure_Path_Register.md](./BPMN_Assignment_1/Assignment1_Failure_Path_Register.md)
* **Task & Gateway Justification:** [Assignment1_Justification.md](./BPMN_Assignment_1/Assignment1_Justification.md)
* **Key Features:** 5 Lanes (*Student/Team, Project Coordinator, Project Management System, Review Committee, Faculty Guide*), automated document/similarity checks, manual/auto guide allocation, revision loops, and timeout boundary events.

---

### 2. [Assignment 2 – Logistics & Shipment Exception Management](./BPMN_Assignment_2/)
* **BPMN 2.0 Diagram:** [Assignment2_BPMN_Diagram.bpmn](./BPMN_Assignment_2/Assignment2_BPMN_Diagram.bpmn)
* **Diagram Preview:** ![Assignment 2 Preview](./BPMN_Assignment_2/Assignment2_BPMN_Diagram.png)
* **Exception Path Register (E1–E10):** [Assignment2_Failure_Path_Register.md](./BPMN_Assignment_2/Assignment2_Failure_Path_Register.md)
* **Task & Gateway Justification:** [Assignment2_Justification.md](./BPMN_Assignment_2/Assignment2_Justification.md)
* **Key Features:** 7 Lanes (*Shipper, Control Tower, Pickup Agent, Hub/Warehouse, Delivery Agent, Recipient, Claims Department*), pickup failure retry loops, customs hold message exchange, non-interrupting transit SLA timer, and damage claims sub-process.

---

### 3. [Assignment 3 – Loan Origination & Approval System](./BPMN_Assignment_3/)
* **BPMN 2.0 Diagram:** [Assignment3_BPMN_Diagram.bpmn](./BPMN_Assignment_3/Assignment3_BPMN_Diagram.bpmn)
* **Diagram Preview:** ![Assignment 3 Preview](./BPMN_Assignment_3/Assignment3_BPMN_Diagram.png)
* **Failure Path Register (L1–L12):** [Assignment3_Failure_Path_Register.md](./BPMN_Assignment_3/Assignment3_Failure_Path_Register.md)
* **Task & Gateway Justification:** [Assignment3_Justification.md](./BPMN_Assignment_3/Assignment3_Justification.md)
* **Key Features:** 7 Lanes (*Applicant, Loan Officer, Underwriter, Fraud & Compliance, Core Banking System, Operations/Disbursement, External Credit Bureau Pool*), parallel gateway check splitting (KYC + Credit Bureau + DTI), message flows with Credit Bureau, counter-offer handling, collateral re-underwriting loop, and core banking disbursement error boundary event.

---

### 📑 [Unified Final Submission Deliverable](./Final_Submission/)
* **Master Document:** [Complete_BPMN_Assignments.md](./Final_Submission/Complete_BPMN_Assignments.md) containing all documentation, diagrams, failure tables, justifications, and validation reports.
* Includes standalone `.bpmn` and `.png` diagram exports for all three systems.

---

## 🛠 Tools & Compatibility
* **Camunda Modeler** (v5.x+)
* **bpmn.io**
* Standard **BPMN 2.0 XML** compliance
