from langchain.prompts import PromptTemplate


def generate_prompt(jira_response:str) -> str:
    summary = jira_response["fields"]["summary"]
    description = jira_response["fields"]["description"]
    jira_pbi = {summary:description}
    prompt = PromptTemplate.from_template(
    """
    System Prompt: You are a test engineer. You create test cases based on the Jira story details.
    Jira story Summary and Description are provided as a dictionary where the dictionary key is the summary and value is the description 
    Iterate through the dictionary {jira_dict} and come up with test cases to test all Jira stories 
    
    Generate test cases in a list format , in which each row is a dictionary.
    Create test cases for each acceptance criteria.
    The length of list is equal to total number of test cases.
    Each test case is defined in a dictionary.
    Each dictionary has following keys :
    1. Test Case Number
    2. Description - The description of test case
    3. Preconditions - what conditions should be already available
    4. Input - Input values to test the application. Provide test values wherever applicable
    5. Test Steps - Steps to execute in order to test the feature.
    6. Expected Results
    The list should be properly terminated.
    In the dictionary there should not be unwanted commas.
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
