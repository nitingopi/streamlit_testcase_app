import pandas as pd

def export_to_excel(test_cases: list, file_name: str = "test_cases.xlsx"):
    df = pd.DataFrame(test_cases)
    print(df.to_json(orient='records'))
    df.to_excel(file_name, index=False, header=False)
    # df.to_csv(file_name,sep='|')
    return file_name
