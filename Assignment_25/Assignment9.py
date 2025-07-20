import pandas as pd
import numpy as np

def main():
    data = {
        'Marks' : [45, 67, 88, 32, 76],
    }

    df = pd.DataFrame(data)

    print("Original dataframe is : ")
    print(df)

    df['Marks'] = df['Marks'].where(df['Marks'] > 50, 'Fail')

    print("Dataframe after updation is : ")
    print(df)

if __name__ == "__main__":
    main()