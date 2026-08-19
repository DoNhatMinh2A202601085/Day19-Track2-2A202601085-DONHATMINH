# Reflection — Lab 19

**Tên:** Đỗ Nhật Minh
**Cohort:** 2A202601085
**Path đã chạy:** lite

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

- **Exact**: Keyword (BM25) và Hybrid đồng hạng nhất (96.7%). BM25 rất mạnh do từ khóa trùng khớp chính xác.
- **Mixed**: Hybrid thắng tuyệt đối (100%) nhờ kết hợp ưu điểm của cả lexical và semantic search.
- **Paraphrase**: Keyword (33.3%) lại thắng Semantic (24.0%). Lý do là model mặc định (`bge-small-en-v1.5`) của path Lite tối ưu cho tiếng Anh, nên bắt ý tiếng Việt diễn đạt lại rất kém.

**Khi nào KHÔNG dùng Hybrid:**
1. Khi chỉ tìm chính xác mã lỗi, ID sản phẩm, hoặc từ khóa đặc thù (pure BM25 là đủ, tiết kiệm tài nguyên).
2. Khi hệ thống yêu cầu độ trễ (latency) cực kỳ thấp, việc tính toán thêm RRF overhead và embedding model là không khả thi.

---

## Điều ngạc nhiên nhất khi làm lab này

Mô hình vector không phải lúc nào cũng tốt hơn, đặc biệt nếu chọn sai ngôn ngữ model cho tập dữ liệu (dùng model tiếng Anh cho corpus tiếng Việt).

---

## Bonus challenge

- [ ] Đã làm bonus (xem `bonus/`)
- [ ] Pair work với: _Không_
