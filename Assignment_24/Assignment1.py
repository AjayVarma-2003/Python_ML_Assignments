import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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

    scaler = MinMaxScaler()

    df['Math_normalise'] = scaler.fit_transform(df[['Math']])

    print(Border)
    print("Dataframe with normalized column : ")
    print(df)
    print(Border)

if __name__ == "__main__":
    main()