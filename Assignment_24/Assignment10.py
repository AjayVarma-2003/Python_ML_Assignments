import pandas as pd
import matplotlib.pyplot as plt

def main():
    Border = "-" * 50

    data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82],
    }

    df = pd.DataFrame(data)

    plt.boxplot(df['English'], data = df)
    plt.ylabel("Marks in english")
    plt.title("Boxplot")
    plt.show()

if __name__ == "__main__":
    main()