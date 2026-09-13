# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Lê Phan Việt Cường 
> **Mã Sinh Viên / Mã Học viên:** 2A202602641
> **Chủ đề Lựa chọn:** *Trợ lý Nhân sự VinFast (HR Assistant):* Tra cứu ngày phép còn lại, chính sách bảo hiểm và tạo đơn xin nghỉ phép.

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | **4/5** | Yêu cầu có thể gồm nhiều bước liên tiếp: xác định nhân viên → tra số ngày phép → kiểm tra điều kiện nghỉ → đối chiếu chính sách → chuẩn bị hoặc tạo đơn nghỉ phép. |
| **2. Tool Interaction** | **5/5** | Cần kết nối với nhiều tool như HR Database để tra ngày phép, Knowledge Base để tra chính sách bảo hiểm/nghỉ phép và Leave Management System để tạo đơn. |
| **3. Dynamic Decision** | **5/5** | Bước tiếp theo phụ thuộc vào kết quả trước. Ví dụ nếu còn đủ ngày phép thì tiếp tục tạo đơn; nếu không đủ thì thông báo và dừng quy trình. |
| **4. Long Horizon Goal** | **4/5** | Agent phải duy trì mục tiêu qua nhiều bước và có thể qua nhiều lượt hội thoại: kiểm tra ngày phép → chọn ngày → xác nhận → tạo đơn → trả kết quả. |
| **TỔNG ĐIỂM AGENTIC FIT** | **18/20** | **Rất phù hợp để triển khai Agentic System**, vì có multi-step reasoning, tool calling, dynamic decision và khả năng thực hiện hành động thay cho người dùng. |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tôi là nhân viên VF2026001, hãy tạo đơn xin nghỉ phép 2 ngày từ 20/09/2026 đến 21/09/2026",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "create_leave_request",
    "thought": "Gemini quyết định gọi công cụ 'create_leave_request' với tham số: {\"employee_id\": \"VF2026001\", \"end_date\": \"21/09/2026\", \"start_date\": \"20/09/2026\"}",
    "arguments": {
      "employee_id": "VF2026001",
      "end_date": "21/09/2026",
      "start_date": "20/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "request_id": "LV-VF2026001-001",
      "employee_id": "VF2026001",
      "employee_name": "Nguyễn Văn An",
      "start_date": "20/09/2026",
      "end_date": "21/09/2026",
      "reason": "Nghỉ phép",
      "message": "Tạo đơn nghỉ phép thành công cho Nguyễn Văn An."
    },
    "latency_ms": 3762.86
  },
  {
    "step": 2,
    "query": "Tôi là nhân viên VF2026001, hãy tạo đơn xin nghỉ phép 2 ngày từ 20/09/2026 đến 21/09/2026",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Tạo đơn nghỉ phép thành công cho Nguyễn Văn An.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 1 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
