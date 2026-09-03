# Transfer Draft - BA Review

Project: Warehouse & Smart Inventory Management
Flow Owner: Ly Na
Flow: Transfer
Status: DRAFT / NEEDS HUMAN REVIEW

This draft applies BA review feedback for Transfer. It does not create a canonical User Story, Acceptance Criteria, Business Rule, technical design, API, data model, or implementation.

## PLAN FIRST

1. Use only reviewed Vault context and research evidence related to Transfer.
2. Keep `CAND-REQ-004` as `DRAFT` until human review approves it.
3. Treat recording/querying Movement as `PROPOSED / TBD`, not confirmed behavior.
4. Keep unresolved behavior as `TBD` or `OPEN QUESTION`.
5. Do not infer permission, stock update, transaction, approval, validation, or technology.

## 1. Requirement/Business Rule liên quan Transfer

- `REQ-002`: Transfer is a required workflow area in `Receive -> Putaway -> Pick -> Transfer -> Adjust -> Audit`.
- `REQ-004`: Transfer, Movement, Stock, and Warehouse are related core domain concepts.
- `CAND-REQ-004` - `DRAFT / cho human review`: The team should evaluate support for tracking movement between backroom and sales shelf within product scope.
- No approved Business Rule directly defines Transfer behavior.
- Evidence: `EVD-010`, `EVD-011`.

## 2. User Story đề xuất

**DRAFT-US-TRF-001 - Đánh giá hỗ trợ Transfer/Movement giữa backroom và sales shelf** *(proposed; stable ID needs human review before canonicalizing)*

As a **person involved in Transfer** *(role/authority is still `OQ-020`)*, I want the product team to evaluate whether movement between the **backroom storage area** and the **sales shelf area** should be supported in the product, so that the team can decide whether any recording or query behavior belongs in the Transfer flow.

Rationale/proposal: Current location knowledge depends on physical arrangement and staff/operator experience, but this is not a confirmed product requirement by itself.

Traceability proposal: `REQ-002`, `REQ-004`, `CAND-REQ-004`, `EVD-010`, `EVD-011`.

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
[OPEN QUESTION - is this movement part of formal Transfer scope? OQ-016]
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

No evidence is sufficient to define edge cases for invalid location, missing stock, damaged goods, barcode error, offline mode, partial quantity, multiple SKU/location behavior, permission denial, approval rejection, rollback, or multi-Warehouse Transfer.

## 6. Open Questions còn thiếu

- `OQ-016`: Is Transfer between locations, between Warehouses, or both?
- `OQ-010`: Does the system cover one Warehouse or multiple Warehouses?
- `OQ-011`: How are stock on-hand, available, reserved, damaged, and in-transit defined, if applicable?
- `OQ-012`: Are lot/batch, serial number, expiry date, unit of measure, or unit conversion in scope?
- `OQ-013`: What are the trigger, precondition, success outcome, exceptions, and completion state of Transfer?
- `OQ-014`: Is partial Transfer supported?
- `OQ-020`: Which roles can perform, record, or view Transfer?

Important BA/human decision:

Should movement between backroom and sales shelf become a supported Transfer behavior in the product, or should it remain only research context until Transfer scope is resolved?

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
- `OQ-016` must be resolved before formal Transfer scope is approved.
