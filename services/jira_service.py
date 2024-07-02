import requests
from config.config import JIRA_API_TOKEN, JIRA_BASE_URL
import pandas as pd
import json


def get_jira_ticket_response(jira_id: str) -> str:
    url = f"{JIRA_BASE_URL}/rest/api/2/issue/{jira_id}"
    headers = {
        "Authorization": f"Bearer {JIRA_API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def create_jira_issues(df_test_cases: pd.DataFrame):
    # Iterate over the DataFrame and create Jira issues
    for index, row in df_test_cases.iterrows():
        issue_data = {
            "Features": row['Description'],
            "Preconditions": row['Preconditions'],
            "Input": row['Input'],
            "Test Steps": row['Test Steps'],
            "Expected Results": row['Expected Results']            
        }
        project_id = 10000
        parent_id = "TES-1"
        issue_type = "Sub-task"
        payload = generate_payload(issue_data, project_id, parent_id, issue_type)
        print(f"{payload=}")
        JIRA_URL = f"{JIRA_BASE_URL}/rest/api/2/issue"
        headers = {
            "Authorization": f"Bearer {JIRA_API_TOKEN}",
            "Content-Type": "application/json"
        }
        response = requests.post(JIRA_URL, headers=headers, data=json.dumps(payload))
        print(response.json())
        if response.status_code == 201:
            print(f"Issue created successfully: {response.json()['key']}")
        else:
            print(f"Failed to create issue: {response.content}")
   

# Test case dictionary
test_case = {
    "Test Case Number": 10.0,
    "Features": "The email is delivered to the user’s registered email address.",
    "Preconditions": "User has created the account and set preferences.",
    "Input": "Email address.",
    "Test Scenario": "Verify that the email is delivered to the user’s registered email address.",
    "Test Steps": [
      "Create user account.",
      "Login to the account.",
      "Set preferences for news categories, news sources, and time of delivery.",
      "Wait for daily summary email to arrive.",
      "Verify that the email is delivered to the user’s registered email address."
    ],
    "Expected Results": "The email is delivered to the user’s registered email address.",
    "Status": "",
    "Comments": ""
}


# Function to format the test case into Jira story format
def generate_payload(issue_data, project_id, parent_id, issue_type):
    test_steps = [f"{i+1}. {step}\n" for i, step in enumerate(issue_data['Test Steps'])]
    payload = {
        "fields": {
            "project": {
                "id": project_id
             },
            "summary": issue_data['Features'],
            "parent" : {
                "id": parent_id
            },
            "description": f"""
                        *Feature*: {issue_data['Features']}

                        *Preconditions*:
                        {issue_data['Preconditions']}

                        *Input*: {issue_data['Input']}

                        *Test Steps*:
                        {''.join(test_steps)}

                        *Expected Results*:
                        {issue_data['Expected Results']}

                        """,
            "issuetype": {
                "name": issue_type
            }
        }
    }
    return payload


