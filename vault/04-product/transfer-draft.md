# Transfer Draft - BA Review

Project: Warehouse & Smart Inventory Management
Flow Owner: Ly Na
Flow: Transfer
Status: DRAFT / NEEDS HUMAN REVIEW

This draft applies BA review feedback for Transfer. It does not create a canonical User Story, Acceptance Criteria, Business Rule, technical design, API, data model, or implementation.

## PLAN FIRST

1. Use only reviewed Vault context and research evidence related to Transfer.
2. Keep `CAND-REQ-004` as `DRAFT`; the latest human review did not approve functional Movement tracking.
3. Treat recording/querying Movement as `PROPOSED / TBD`, not confirmed behavior.
4. Keep unresolved behavior as `TBD` or `OPEN QUESTION`.
5. Do not infer permission, stock update, transaction, approval, validation, or technology.

## 1. Requirement/Business Rule liên quan Transfer

- `REQ-002`: Transfer is a required workflow area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`.
- `REQ-004`: Transfer, Movement, Stock, and Warehouse are related core domain concepts.
- `CAND-REQ-003`: `APPROVED — HUMAN PRODUCT DECISION`; the MVP supports recording and looking up inventory information related to area-level internal locations `Backroom` and `Sales Shelf`, and one SKU may be recorded at multiple internal locations in the same Warehouse.
- `CAND-REQ-004` - `DRAFT / cho human review`: The team should evaluate support for tracking movement between backroom and sales shelf within product scope.
- `DEC-005`, `DEC-007`, `DEC-009`: the MVP has one Warehouse; Transfer is modeled only as subsequent relocation between tracked internal locations in that Warehouse; Physical movement remains distinct from a Movement system record.
- No approved Business Rule directly defines Transfer behavior.
- Evidence: `EVD-010`, `EVD-011`.

The Transfer boundary is a HUMAN PRODUCT DECISION, not a research finding. It does not approve a system Transfer transaction, Movement system record, Stock effect, automatic location update, or functional Transfer requirement.

## 2. User Story đề xuất

**DRAFT-US-TRF-001 - Đánh giá hỗ trợ Transfer/Movement giữa backroom và sales shelf** *(draft ID đã được human-approved để theo dõi; story vẫn DRAFT và chưa canonical)*

As a **person involved in Transfer** *(role/authority is still `OQ-020`)*, I want the product team to evaluate what system behavior, if any, should support subsequent relocation between the tracked **Backroom** and **Sales Shelf** internal locations, so that the team can decide whether recording or query behavior belongs in the Transfer flow.

Rationale/proposal: Current location knowledge depends on physical arrangement and staff/operator experience, but this is not a confirmed product requirement by itself.

Traceability proposal: `REQ-002`, `REQ-004`, `CAND-REQ-003`, `CAND-REQ-004`, `DEC-005`, `DEC-006`, `DEC-007`, `DEC-009`, `EVD-010`, `EVD-011`.

## 3. Acceptance Criteria đề xuất

- **AC-TRF-001 - Scope-level Transfer confirmation:** Given the reviewed workflow areas, when checking workflow scope, then Transfer is identified as a required area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`.

Source: `REQ-002`.

This AC only confirms scope. It does not prove functional Transfer behavior.

Functional AC are not ready for approval yet:

- Recording movement is `PROPOSED / TBD`.
- Querying movement is `PROPOSED / TBD`.
- Storing source/destination is `PROPOSED / TBD`.
- Backroom-to-sales-shelf and sales-shelf-to-backroom behavior are `PROPOSED / TBD`.
- Stock update, Movement transaction, approval, permission, validation, completion state, and rollback are `TBD`.

Possible future AC only if BA/human approves the behavior:

- Given movement between backroom and sales shelf is approved as product behavior, when a Transfer is handled, then the approved specification defines whether the system records that movement.
- Given movement recording is approved, when BA defines the Transfer data to keep, then the specification defines whether source and destination are required fields.
- Given movement querying is approved, when BA defines the Transfer lookup behavior, then the specification defines what information can be queried and by whom.

## 4. User Flow cấp cao

```text
[TBD: Transfer trigger]
        |
[Transfer workflow area - CONFIRMED by REQ-002]
        |
[Evidence context - movement exists between backroom and sales shelf: EVD-010]
        |
[APPROVED MODELING BOUNDARY - subsequent relocation between tracked internal locations: DEC-007 / DEC-009]
        |
[PROPOSED / TBD - decide whether the product records movement]
        |
[PROPOSED / TBD - decide whether the product supports querying movement]
        |
[TBD - completion state, stock impact, Movement behavior, and handoff]
```

This flow does not assert source/destination fields, transaction behavior, automatic stock update, approval, partial Transfer, negative stock behavior, scanner usage, or permissions.

## 5. Edge cases có evidence

- Current operation includes movement between the backroom storage area and the sales shelf area (`EVD-010`).
- It is not confirmed whether these internal movements are recorded as separate transactions in KiotViet (`EVD-011`).

Multiple internal locations per SKU and the exclusion of cross-Warehouse Transfer are HUMAN PRODUCT DECISIONS (`DEC-005`, `DEC-006`, `DEC-007`), not research findings. No evidence or approved functional rule is sufficient to define edge cases for invalid location, missing stock, barcode error, offline mode, partial quantity, permission denial, approval rejection, rollback, Stock effect, automatic location update, or Movement system record creation.

## 6. Open Questions còn thiếu

- `OQ-011`: `PARTIALLY DECIDED / OPEN`; the MVP uses `system stock quantity`, while location granularity, Warehouse aggregation, workflow effect, and change timing remain unresolved.
- `OQ-012`: Are lot/batch, serial number, expiry date, unit of measure, or unit conversion in scope?
- `OQ-013`: What are the trigger, precondition, success outcome, exceptions, and completion state of Transfer?
- `OQ-014`: Is partial Transfer supported?
- `OQ-020`: Which roles can perform, record, or view Transfer?

Important BA/human decision:

Should subsequent relocation between tracked internal locations create a system Transfer transaction, support recording/querying behavior, affect `system stock quantity` or location information, or create a Movement system record?

Resolved scope context: `OQ-010` and `OQ-016` are `RESOLVED — HUMAN PRODUCT DECISION`. The MVP has one Warehouse and Transfer is limited to subsequent relocation between tracked internal locations in that Warehouse. Functional Transfer capability remains unapproved.

## 7. Files cần update sau human review

Canonical artifacts should be created only after human approval:

- `C:\warehouse-smart-inventory\vault\04-product\stories\<stable-story-id>.md` - User Story + AC.
- `C:\warehouse-smart-inventory\vault\04-product\user-flows\<stable-flow-id>.md` - Transfer flow.

Indexes/traceability to update after approval:

- `C:\warehouse-smart-inventory\docs\04-backlog\user-stories.md`
- `C:\warehouse-smart-inventory\docs\03-product\user-flow.md`
- `C:\warehouse-smart-inventory\docs\TRACEABILITY.md`

Do not update Taiga, story spec, API, data model, code, technical design, or test artifacts before User Story/AC approval.

## Review notes applied

- The phrase "record or query movement" is kept as `PROPOSED / TBD`, not confirmed behavior.
- The rationale about reducing reliance on physical arrangement and experience is kept as proposal/rationale, not confirmed requirement.
- `AC-TRF-001` is explicitly scope-level.
- Functional behavior for source/destination, recording, and querying remains `TBD`.
- `OQ-016` is resolved by HUMAN PRODUCT DECISION; functional Transfer behavior remains blocked by `OQ-013`, `OQ-014`, `OQ-015`, `OQ-020` and the missing decisions about transaction, Stock/location effect, and Movement system record creation.
