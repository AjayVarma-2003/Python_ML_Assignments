import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    data = {
        'Department' : ['HR', 'IT', 'Finance', 'HR', 'IT'],
    }

    df = pd.DataFrame(data)

    print("Data before encoding")
    print(df)

    df['Department'] = df['Department'].map({'HR' : 0, 'IT' : 1, 'Finance' : 2})

    print("Dataframe after encoding : ")
    print(df)

if __name__ == "__main__":
    main()