import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {
        'Age' : [18, 22, 25, 30, 35],
    }

    df = pd.DataFrame(data)

    print("Dataframe without normalization : ")
    print(df)

    scaler = MinMaxScaler()

    df['Normalized Age'] = scaler.fit_transform(df[['Age']])

    print("Dataframe after normalization : ")
    print(df)

if __name__ == "__main__":
    main()