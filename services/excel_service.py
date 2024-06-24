import pandas as pd

def export_to_excel(test_cases: list, file_name: str = "test_cases.xlsx"):
    df = pd.DataFrame(test_cases)
    df.to_excel(file_name, index=False)
    return file_name
