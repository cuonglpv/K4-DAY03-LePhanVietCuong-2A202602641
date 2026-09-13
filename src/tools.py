"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
VinFast HR Assistant - Tool Schemas & Execution Layer
"""

import json
from typing import Dict, Any


# ==============================================================================
# 1. TOOL SCHEMAS
# ==============================================================================

TOOLS_SCHEMA = [

    # --------------------------------------------------------------------------
    # Tool 1: Tra cứu số ngày phép còn lại
    # --------------------------------------------------------------------------
    {
        "name": "get_leave_balance",
        "description": "Tra cứu số ngày phép còn lại của nhân viên VinFast bằng mã nhân viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên cần tra cứu, ví dụ: 'VF2026001'"
                }
            },
            "required": ["employee_id"]
        }
    },

    # --------------------------------------------------------------------------
    # Tool 2: Tra cứu chính sách HR
    # --------------------------------------------------------------------------
    {
        "name": "search_hr_policy",
        "description": "Tra cứu chính sách nhân sự VinFast như nghỉ phép, bảo hiểm và các quyền lợi nhân viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "policy_topic": {
                    "type": "string",
                    "description": "Chủ đề chính sách cần tra cứu, ví dụ: 'nghỉ phép', 'bảo hiểm'"
                }
            },
            "required": ["policy_topic"]
        }
    },

    # --------------------------------------------------------------------------
    # Tool 3: Tạo đơn xin nghỉ phép
    # --------------------------------------------------------------------------
    {
        "name": "create_leave_request",
        "description": "Tạo đơn xin nghỉ phép cho nhân viên VinFast.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên xin nghỉ phép"
                },
                "start_date": {
                    "type": "string",
                    "description": "Ngày bắt đầu nghỉ, định dạng DD/MM/YYYY"
                },
                "end_date": {
                    "type": "string",
                    "description": "Ngày kết thúc nghỉ, định dạng DD/MM/YYYY"
                },
                "reason": {
                    "type": "string",
                    "description": "Lý do xin nghỉ"
                }
            },
            "required": [
                "employee_id",
                "start_date",
                "end_date"
            ]
        }
    }
]


# ==============================================================================
# 2. MOCK DATABASE
# ==============================================================================

MOCK_DATABASE = {
    "VF2026001": {
        "full_name": "Nguyễn Văn An",
        "department": "Software Engineering",
        "position": "Software Engineer",
        "leave_balance": 8,
        "email": "an@vinfast.vn"
    },

    "VF2026002": {
        "full_name": "Trần Thị Bình",
        "department": "Human Resources",
        "position": "HR Specialist",
        "leave_balance": 2,
        "email": "binh@vinfast.vn"
    }
}


# ==============================================================================
# 3. HR POLICY MOCK DATA
# ==============================================================================

HR_POLICIES = {
    "nghỉ phép": {
        "title": "Chính sách nghỉ phép",
        "content": "Nhân viên được sử dụng số ngày phép năm theo quy định của công ty. Đơn nghỉ phép cần được gửi và phê duyệt theo quy trình nội bộ."
    },

    "bảo hiểm": {
        "title": "Chính sách bảo hiểm",
        "content": "Nhân viên được hưởng các chế độ bảo hiểm theo chính sách nhân sự hiện hành và quy định pháp luật áp dụng."
    }
}


# ==============================================================================
# 4. TOOL EXECUTION
# ==============================================================================

def execute_get_leave_balance(employee_id: str) -> str:
    """Tra cứu số ngày phép còn lại."""

    employee = MOCK_DATABASE.get(
        employee_id.strip().upper()
    )

    if employee:
        return json.dumps({
            "status": "SUCCESS",
            "employee_id": employee_id,
            "employee_name": employee["full_name"],
            "leave_balance": employee["leave_balance"]
        }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy nhân viên có mã '{employee_id}'"
    }, ensure_ascii=False)


def execute_search_hr_policy(policy_topic: str) -> str:
    """Tra cứu chính sách HR."""

    topic = policy_topic.strip().lower()

    policy = HR_POLICIES.get(topic)

    if policy:
        return json.dumps({
            "status": "SUCCESS",
            "topic": topic,
            "data": policy
        }, ensure_ascii=False)

    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Không tìm thấy chính sách liên quan đến '{policy_topic}'"
    }, ensure_ascii=False)


def execute_create_leave_request(
    employee_id: str,
    start_date: str,
    end_date: str,
    reason: str = "Nghỉ phép"
) -> str:
    """Tạo đơn xin nghỉ phép."""

    employee = MOCK_DATABASE.get(
        employee_id.strip().upper()
    )

    if not employee:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy nhân viên '{employee_id}'"
        }, ensure_ascii=False)

    booking_id = f"LV-{employee_id}-001"

    return json.dumps({
        "status": "SUCCESS",
        "request_id": booking_id,
        "employee_id": employee_id,
        "employee_name": employee["full_name"],
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "message": f"Tạo đơn nghỉ phép thành công cho {employee['full_name']}."
    }, ensure_ascii=False)


# ==============================================================================
# 5. TOOL ROUTER
# ==============================================================================

TOOL_ROUTER = {
    "get_leave_balance": execute_get_leave_balance,
    "search_hr_policy": execute_search_hr_policy,
    "create_leave_request": execute_create_leave_request
}


def dispatch_tool_call(
    tool_name: str,
    arguments: Dict[str, Any]
) -> str:
    """Hàm trung chuyển thực thi tool."""

    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)

        except Exception as e:
            return json.dumps({
                "status": "EXECUTION_ERROR",
                "error": str(e)
            }, ensure_ascii=False)

    return json.dumps({
        "status": "UNKNOWN_TOOL",
        "error": f"Tool '{tool_name}' không tồn tại!"
    }, ensure_ascii=False)