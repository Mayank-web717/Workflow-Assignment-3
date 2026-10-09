# Assignment 2 – Exception Path Register
## Logistics & Shipment Exception Management

---

| ID | Failure / Exception Point | Cause / Trigger | Solution (BPMN Action) | BPMN Construct | Final Outcome |
|----|--------------------------|-----------------|------------------------|---------------|---------------|
| **E1** | Pickup Failure | Shipper not available at pickup location, locked address, incorrect address, or vehicle breakdown | Exclusive Gateway after "Collect and Scan": if pickup fails → reschedule pickup (User Task); Retry loop back to collection; Timer Boundary Event after 3 failed attempts → End Event | Exclusive Gateway + User Task (reschedule) + Non-interrupting Timer Boundary Event + Retry Loop | **EndEvent: Pickup Failed After Max Attempts** OR proceeds to Hub on success |
| **E2** | Address Validation / Delivery Problem | Incomplete address, incorrect pincode, unserviceable zone, or weight/dimension exceeds service limits | Service Task validates address, weight, and service type; Exclusive Gateway: if invalid → loop back to "Book Shipment" task for correction by customer | Service Task + Exclusive Gateway + Retry Loop | Customer corrects and resubmits OR shipment is cancelled |
| **E3** | Damaged Parcel | Parcel visibly damaged at pickup OR found damaged during hub inspection | At Pickup: Exclusive Gateway after damage report → route to Claims Sub-Process. At Hub: Exclusive Gateway on inspection result → isolate parcel → Claims | Exclusive Gateways + User Task (damage report/isolate) + Claims Sub-Process path | **EndEvent: Claim Settled** (Claims Department processes) |
| **E4** | Lost Parcel | Scan gap with no location update for extended period; parcel not found at expected hub | Exclusive Gateway on scan check result: "Parcel Lost" branch → Control Tower opens trace case → escalates → Claims Department; Tracing Sub-Process | Exclusive Gateway + User Tasks (trace + escalate) + Claims Sub-Process | **EndEvent: Parcel Lost – Claims Initiated** |
| **E5** | Transit Delay | Carrier vehicle breakdown, weather, port congestion, or customs delays cause SLA breach | Non-interrupting Timer Boundary Event on "Track Shipment" task fires when transit SLA (e.g. 2 days) is breached → Control Tower updates ETA and notifies customer | Non-interrupting Boundary Timer Event + User Task (ETA update/notification) | Process continues; customer is notified; delivery rescheduled |
| **E6** | Customs Hold | Shipment flagged by customs for missing/incorrect documents, restricted goods, or duty assessment | Exclusive Gateway in Hub: if customs required → Hub places hold and sends document request to shipper → Shipper receives via Message Catch Event and provides docs → Intermediate Message Catch Event waits for customs clearance | Exclusive Gateway + Send Notification + Intermediate Message Catch Event + Loop | On clearance → continues to line haul; if repeatedly held → escalation |
| **E7** | Recipient Unavailable | Recipient not at delivery address, no one available to receive, or delivery to gated community fails | Exclusive Gateway: recipient unavailable → delivery agent returns to depot; Retry Delivery gateway: if retry → re-notify recipient and reattempt; if max attempts → Return to Sender; Non-interrupting Timer Boundary Event on delivery attempt | Exclusive Gateway + User Task (depot return) + Exclusive Gateway (retry/return) + Timer Boundary Event | **EndEvent: Returned to Sender** OR rescheduled delivery |
| **E8** | Refusal / COD Payment Failure | Recipient refuses package (wrong item, damaged appearance) or cannot/will not pay COD amount | Exclusive Gateway on "Recipient Available?": if COD issue → Gateway "COD Payment Made?": if refused → Return to Sender; also maps directly to EndEvent "Delivery Refused" | Exclusive Gateway + Send Task (refusal notice) + User Task (Return to Sender) | **EndEvent: Delivery Refused – Return to Sender** |
| **E9** | Tracking / Scan Failure | Scanner malfunction, connectivity failure at hub, or missing barcode prevents scan update | Service Task detects scan gap; Exclusive Gateway: scan gap → Manual Reconciliation User Task where hub staff manually verify parcel location; if resolved → continue tracking; if unresolved → Lost Parcel path (E4) | Service Task + Exclusive Gateway + User Task (manual reconciliation) | Resolved → continues to delivery; Unresolved → E4 (Lost Parcel) path |
| **E10** | Cancellation After Dispatch | Shipper requests cancellation after shipment has been picked up or already dispatched | Cancellation request triggers User Task → Control Tower checks feasibility (Exclusive Gateway); if pre-dispatch → issue refund; if post-dispatch → cannot cancel, continue delivery; refund/credit processed | User Task + Exclusive Gateway + Compensation (Refund) | **EndEvent: Cancelled + Refund Issued** (pre-dispatch) OR continues (post-dispatch) |

---

### Additional Exception Paths Identified and Modelled

| Additional Risk | Absorbed Into | BPMN Solution |
|----------------|---------------|---------------|
| Barcode unreadable / smudged | E9 (Scan Failure) | Manual reconciliation path handles barcode issues |
| Incorrect hub routing | E9 (Scan Gap) | Scan gap detection routes to reconciliation |
| Driver GPS failure | E5 (Transit Delay) | Timer SLA breach triggers same delay handling path |
| Duplicate AWB number | E2 (Validation) | Address/AWB validation service catches duplicates at booking |
| Insurance claim denial | E3/E4 (Claims) | Claims sub-process includes settlement decision gateway |

---
*Generated for Academic BPMN 2.0 Assignment – Assignment 2*
