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

    df['Total'] = df['Math'] + df['Science'] + df['English']

    x = df['Name']
    y = df['Total']

    plt.figure(figsize = (8, 5))
    plt.bar(x, y, width = 0.3, edgecolor = 'black', color = 'blue')
    plt.xlabel("Name of students")
    plt.ylabel("Total marks of student")
    plt.title("Student names vs Total marks")
    plt.show()

if __name__ == "__main__":
    main()