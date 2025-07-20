import pandas as pd

def main():
    Border = "-" * 50

    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82],
    }

    df = pd.DataFrame(data)

    df['Gender'] = ['Male', 'Male', 'Female']

    df['Gender'] = df['Gender'].map({'Male' : 1, 'Female' : 2})
    print(Border)
    print("Dataframe after encoding : ")
    print(df)
    print(Border)

    x = df.groupby('Gender')
    avg_marks = x[['Math', 'Science', 'English']].mean()

    print(Border)
    print("Average marks are : ")
    print(avg_marks)
    print(Border)

if __name__ == "__main__":
    main()