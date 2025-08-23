import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def Preprocess(x_train, x_test):
    # In this dataset we have use TF-IDF vectorization
    # TF_IDF(Term Frequency - Inverse Document frequency) is used for converting text into numeric matrix
    # it used weightage technique mean words which appears often get higher weightage that is Term Frequency
    # and words like the is a and get lower weightage that is done by Inverse Document frequency.
    # we can not use standard scalar here as it is used for numeric values only.
    
    vectorizer = TfidfVectorizer(stop_words = "english", max_df = 0.7)

    x_train = vectorizer.fit_transform(x_train)
    x_test = vectorizer.transform(x_test)

    return x_train, x_test

def NewsClassifier(dataset1, dataset2):
    fake_df = pd.read_csv(dataset1)
    true_df = pd.read_csv(dataset2)

    # Adding labels in both dataset
    fake_df["labels"] = 0
    true_df["labels"] = 1

    # Now combining datasets
    # concat method is used to combine two datasets.
    df = pd.concat([fake_df, true_df], axis = 0).reset_index(drop = True)

    # Feature & labels separation
    x = df["text"]
    y = df["labels"]

    # Data split
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    # We have to vectorize only x_train and X_test to avoid data leakage.
    X_train, X_test = Preprocess(X_train, X_test)

def main():
    NewsClassifier("Fake.csv", "True.csv")

if __name__ == "__main__":
    main()