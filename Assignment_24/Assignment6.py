import pandas as pd
import numpy as np

def main():
    Border = "-" * 50

    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82],
    }

    df = pd.DataFrame(data)

    print(Border)
    print("Original dataframe is : ")
    print(df)
    print(Border)

    df['Total'] = df['Math'] + df['Science'] + df['English']

    df['Status'] = np.where(df['Total'] >= 250, 'Pass', 'Fail')
    
    count = df[df['Status'] == "Pass"]

    print(Border)
    print("Dataframe after adding status : ")
    print(df)
    print(Border)

    print("Number of students passed are : ", len(count))
    print(Border)

if __name__ == "__main__":
    main()