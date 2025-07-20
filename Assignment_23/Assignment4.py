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

    print(Border)

    df_filtered = df[df['Science'] > 85]

    print("Students who scored more than 85 in science are : ")
    print(df_filtered['Name'])

    print(Border)

if __name__ == "__main__":
    main()