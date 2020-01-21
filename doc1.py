import pandas as pd


def create_df(filename):
    mid = pd.read_csv("D:/"+filename, index_col=0 )

    final = []
    col_name = mid.columns
    for i in range(len(col_name)):
        if 'WorkedWith' in col_name[i]:
            final.append(col_name[i])

    df = mid[mid.Country == 'India'][final]
    return df

main = create_df("dataset1.csv")

main.to_csv("D:\Database_India.csv")
