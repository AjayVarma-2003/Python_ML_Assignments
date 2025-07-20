import pandas as pd

def main():
    data = {
        'Name' : ['A', 'B', 'C'],
        'Age' : [21.0, 22.0, 23.0],
    }

    df = pd.DataFrame(data)

    print("Data type of columns of dataframe is : ")
    print(df.dtypes)

    df['Age'] = df['Age'].astype(int)
    print("Data type of columns now : ")
    print(df.dtypes)

if __name__ == "__main__":
    main()