Nguồn/trigger chênh lệch, detailed recheck, completion state, exception handling, adjustment mechanism, reason/evidence/approval, role/permission, quantity definition, negative-stock handling và anomaly/discrepancy definition vẫn là `TBD` / `OPEN QUESTION`.

Trace này không xác nhận Audit là trigger/dependency bắt buộc, automatic stock update, hoặc behavior ngoài `CAND-BR-002`.

## Transfer DRAFT trace

```text
REQ-002
  (Transfer là khu vực quy trình bắt buộc)

  + REQ-004
    (Movement và Transfer thuộc core domain; hành vi chi tiết TBD)

  + CAND-REQ-004
    (DRAFT — đề xuất đánh giá hỗ trợ theo dõi movement)

  + EVD-010
    (có physical movement giữa backroom và sales shelf)

  + EVD-011
    (chưa xác nhận movement có phải transaction riêng hay không)

  + EVD-019
    (research limitation)

    -> DRAFT-US-TRA-001
    -> Acceptance Criteria: TBD
    -> Transfer cautious flow: DRAFT
    -> Taiga / Implementation / Test: Chưa bắt đầu