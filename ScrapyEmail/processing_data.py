import pandas as pd

def process_data(email_list):
    df = pd.DataFrame(email_list)
    df.to_excel("email_data.xlsx", index=False)
