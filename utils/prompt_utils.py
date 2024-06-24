from langchain.prompts import PromptTemplate


def generate_prompt(jira_response:str) -> str:
    summary = jira_response["fields"]["summary"]
    description = jira_response["fields"]["description"]
    jira_pbi = {summary:description}
    prompt = PromptTemplate.from_template(
    """
    System Prompt: You are a test engineer. You create test cases based on the Jira story details.
    Jira story Summary and Description are provided as a dictionary where the dictionary key is the summary and value is the description 
    Iterate through the dictionary {jira_dict} and come up with test scenarios to test all Jira stories 
    
    Generate test cases in a HTML table format, where the headers are:- 
    Test Case_Number | Features | Preconditions | Input | Test Scenario | Test Steps | Expected Results | Status | Comments
    Each test case is in a row of table. 
    Status and Comments columns should be empty
    """
    )
    # examplesText = ""
    # confluenceLink = ""
    # final_prompt = prompt.format(
    #     jira_dict=jira_pbi, examples=examplesText, details=confluenceLink
    # )
    final_prompt = prompt.format(
        jira_dict=jira_pbi )

    return final_prompt
