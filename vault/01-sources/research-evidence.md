# Research Evidence Index

## Status

This file is an evidence index for source ingestion only. It records human-confirmed research evidence from P1, P2, and P3 as captured in [`interview-notes.md`](interview-notes.md).

This file does not create Requirements, Business Rules, User Stories, or Acceptance Criteria. Unsupported information remains `TBD` or `OPEN QUESTION`.

## Evidence Items

### EVD-001

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Current tooling
- Evidence: Inventory quantity is tracked using KiotViet.
- Notes: The scope and permissions of KiotViet usage remain `OPEN QUESTION`.

### EVD-002

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Receive
- Evidence: When goods are received, the item is checked and the actual received quantity is counted.

### EVD-003

- Source: [`interview-notes.md`](interview-notes.md) / P1
- Topic: Receive
- Evidence: Actual received quantity is compared with expected quantity.

### EVD-004

- Source: [`interview-notes.md`](interview-notes.md) / P1
- Topic: Receive discrepancy
- Evidence: If the actual delivery is short or discrepant, only the actual received quantity is entered into the system, not the expected quantity.

### EVD-005

- Source: [`interview-notes.md`](interview-notes.md) / P1
- Topic: Receive discrepancy
- Evidence: If there is a receiving discrepancy, it is handled with the delivery party.
- Notes: Detailed discrepancy cause, frequency, evidence, and approval rules remain `OPEN QUESTION`.

### EVD-006

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Putaway / Physical location
- Evidence: The minimart has a backroom storage area and a sales shelf area.

### EVD-007

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Putaway / Physical location
- Evidence: After receiving, goods may be placed in the backroom storage area or moved to the sales shelf area.

### EVD-008

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Physical location knowledge
- Evidence: Current knowledge of where goods are located mainly depends on physical arrangement and operator/staff experience.
- Notes: How many physical locations one SKU may be managed in remains `OPEN QUESTION`.

### EVD-009

- Source: [`interview-notes.md`](interview-notes.md) / P1
- Topic: Pick
- Evidence: Staff know where goods are located in the backroom/shelf area mainly through physical arrangement and experience, while inventory quantity is tracked in KiotViet.

### EVD-010

- Source: [`interview-notes.md`](interview-notes.md) / P1
- Topic: Transfer / Movement
- Evidence: Current operation includes moving goods between the backroom storage area and the sales shelf area.

### EVD-011

- Source: [`interview-notes.md`](interview-notes.md) / P1
- Topic: Transfer / Movement unknown
- Evidence: It is not confirmed whether these internal movements are recorded as separate transactions in KiotViet.
- Notes: Whether the new system needs a separate Transfer/Movement record for backroom-to-shelf movement remains `OPEN QUESTION`.

### EVD-012

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Adjust
- Evidence: When actual stock differs from system data, the discrepancy must be checked again before adjustment handling.

### EVD-013

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Adjust ownership signal
- Evidence: P1, as manager, participates in checking/handling stock discrepancies; P2 and P3 confirmed that staff report/escalate actual-vs-system differences to the manager for handling.
- Notes: This is evidence of current minimart handling, not a confirmed permission model for the new system.

### EVD-014

- Source: [`interview-notes.md`](interview-notes.md) / P1
- Topic: Adjust permission unknown
- Evidence: It is not confirmed whether ordinary staff can directly adjust stock in KiotViet.
- Notes: Official permissions for Warehouse Staff, Manager, Purchasing, and Admin remain `OPEN QUESTION`.

### EVD-015

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Audit
- Evidence: The minimart performs inventory checking daily.

### EVD-016

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Audit
- Evidence: Inventory checking includes checking/counting physical goods and comparing them with inventory data in KiotViet.
- Notes: Whether Audit is cycle count, full stocktake, or both remains `OPEN QUESTION`.

### EVD-017

- Source: [`interview-notes.md`](interview-notes.md) / P1; P2 and P3 confirmation
- Topic: Discrepancy handling
- Evidence: When a discrepancy is found, it must be checked again before handling.
- Notes: Specific causes and frequency of inventory discrepancies remain `OPEN QUESTION`.

### EVD-018

- Source: [`interview-notes.md`](interview-notes.md) / P2 and P3
- Topic: Confirmation method
- Evidence: P2 and P3 confirmed a prepared workflow summary and reported no corrections.
- Notes: No transcript or direct quote is recorded for P2 or P3.

### EVD-019

- Source: [`interview-notes.md`](interview-notes.md) / Research Limitations
- Topic: Research limitation
- Evidence: P1, P2, and P3 all work at the same minimart, so evidence reflects current operation at that minimart and must not be generalized to every warehouse.

## Partially Informed Open Questions

- `OQ-009`: P1, P2, and P3 provide real participant evidence for research, but stakeholder access and usability testing remain unresolved.
- `OQ-013`: Current workflow evidence partially informs Receive, Putaway, Pick, Transfer, Adjust, and Audit, but detailed triggers, preconditions, exceptions, and completion states remain unresolved.
- `OQ-016`: Evidence shows movement between backroom and shelf, but the formal Transfer scope remains unresolved.
- `OQ-017`: Evidence shows re-checking discrepancies and manager involvement, but required reasons, evidence, and approvals remain unresolved.
- `OQ-018`: Evidence shows daily inventory checking, but whether Audit is cycle count, full stocktake, or both remains unresolved.
- `OQ-020`: Evidence shows staff escalation to manager for discrepancy handling, but official permissions remain unresolved.
- `OQ-028`: Evidence shows actual-vs-system discrepancy occurs, but anomaly definition, causes, frequency, and proof remain unresolved.

## Still Unresolved

- `OQ-001` to `OQ-008`
- `OQ-010` to `OQ-012`
- `OQ-014` to `OQ-015`
- `OQ-019`
- `OQ-021` to `OQ-027`
- `OQ-029` to `OQ-033`

See [`../02-requirements/open-questions.md`](../02-requirements/open-questions.md) for the canonical open question list.
