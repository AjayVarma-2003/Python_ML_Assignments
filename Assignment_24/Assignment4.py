import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Border = "-" * 50

    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82],
    }

    df = pd.DataFrame(data)

    col_names = df.columns

    x = []
    for i in range(1, len(col_names)):
        x.append(col_names[i])

    y = df[df['Name'] == 'Sagar'].iloc[0, 1:].values

    plt.pie(y, labels = ['Math', 'Science', 'English'], autopct = '%1.1f%%')
    plt.show()

if __name__ == "__main__":
    main()