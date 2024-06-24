import requests
from config.config import JIRA_API_TOKEN, JIRA_BASE_URL

def get_jira_ticket_response(jira_id: str) -> str:
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{jira_id}"
    headers = {
        "Authorization": f"Basic {JIRA_API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def create_jira_issues(test_cases: list):
    url = f"{JIRA_BASE_URL}/rest/api/2/issue/bulk"
    headers = {
        "Authorization": f"Bearer {JIRA_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "issueUpdates": [
            {
                "fields": {
                    "project": {"key": "YOUR_PROJECT_KEY"},
                    "summary": f"Test Case: {test_case['name']}",
                    "description": test_case['description'],
                    "issuetype": {"name": "Task"}
                }
            } for test_case in test_cases
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
