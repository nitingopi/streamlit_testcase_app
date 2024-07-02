import pandas as pd

def export_to_excel(df_test_cases: pd.DataFrame, file_name: str = "test_cases.xlsx"):
    # df = pd.DataFrame(test_cases)
    # print(df.to_json(orient='records'))
    df_test_cases.to_excel(file_name, index=False, header=True)
    # df.to_csv(file_name,sep='|')
    return file_name
