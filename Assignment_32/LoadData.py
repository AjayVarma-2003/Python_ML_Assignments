import pandas as pd

def NewsClassifier(dataset1, dataset2):
    fake_df = pd.read_csv(dataset1)
    true_df = pd.read_csv(dataset2)

    # Adding labels in both dataset
    fake_df["labels"] = 0
    true_df["labels"] = 1

    # Now combining datasets
    # concat method is used to combine two datasets.
    df = pd.concat([fake_df, true_df], axis = 0).reset_index(drop = True)

def main():
    NewsClassifier("Fake.csv", "True.csv")

if __name__ == "__main__":
    main()