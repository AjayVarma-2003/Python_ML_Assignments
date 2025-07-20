import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data = {
        'City' : ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi'],
    }

    df = pd.DataFrame(data)

    print("Dataframe before encoding : ")
    print(df)

    encode = LabelEncoder()

    df['Encoded City'] = encode.fit_transform(df['City'])

    print("Dataframe after encoding")
    print(df)

if __name__ == "__main__":
    main()