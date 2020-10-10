import pandas as pd
import numpy as np
from preprocessing import TextPreprocessor
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle
from sklearn.model_selection import train_test_split
import os


def f():
    data = pd.read_csv("./data/comments.csv")
    data = data[['CONTENT', 'RATING']]
    data.info()
    data = data[data.RATING >= 1]
    data.info()
    data['label'] = data['RATING']
    data.info()
    data = data.reset_index()
    data.info()
    data.to_csv("./data/comments_deal.csv", encoding="utf_8")


def f2():
    data = pd.read_csv("./data/comments_deal.csv")
    print(data.head())
    data.info()
    process = TextPreprocessor(stopword_file="./data/stopwords/stopword_normal.txt")
    X = data.CONTENT
    print(X[0:5])
    # transformer = CountVectorizer(analyzer=process.process_line)
    # transformer.fit(X)
    # X = transformer.transform(X)
    for i in range(5):
        X[i] = process.process_line(X[i])
    print(X[0:5])
    # data['CONTENT'] = X
    # print(data.head())
    # data.to_csv("./data/comments_deal_2.csv", encoding="utf_8")


def f3():
    data = pd.read_csv("./data/comments_deal.csv")
    data = data[['CONTENT', 'RATING', 'label']]
    data['label'] = data['label'].astype('int')
    data['RATING'] = data['RATING'].astype('int')
    data.info()
    print(data.head())
    data.to_csv("./data/comments_deal0.csv", encoding="utf_8", sep="\n")


def f4():
    data = pd.read_csv("./data/comments_deal.csv")  # , lineterminator="\n"comment_trainset_2class
    data.info()
    data = data[['CONTENT', 'RATING', 'label']]
    data_n = data[0:20000]
    data_n.info()
    data_n.to_csv("./data/comments_deal_2w.csv", encoding="utf_8")
    # process = TextPreprocessor(stopword_file="./data/stopwords/stopword_normal.txt")
    # X = data.CONTENT
    # bow_transformer = CountVectorizer(analyzer=process.process_line).fit(X)
    # X = bow_transformer.transform(X)
    # print(X[0:5])
    # data.to_csv("./data/comments_deal_2.csv", encoding="utf_8")
    # print(data.head())
    # X = data.CONTENT
    # data.info()
    # data.fillna(method='ffill')
    # data.dropna()
    # print(data.isnull().sum())
    # data.info()
    # y = data.label
    # bow_transformer = CountVectorizer(analyzer=process.process_line).fit(X)
    # X = bow_transformer.transform(X)
    # print(X)


def f5():
    data = pd.read_csv("./data/comments_deal_2w.csv")
    print(data.head())
    process = TextPreprocessor(stopword_file="./data/stopwords/stopword_normal.txt")
    X = data.CONTENT
    for i in range(5):
        X[i] = process.process_line(X[i])
    print(X[0:5])
    bow_transformer = CountVectorizer(analyzer=process.process_line).fit(X)
    X = bow_transformer.transform(X)
    print(X[0:5])


def f6():
    data = pd.read_csv("data/comments_dealNan.csv")
    # train_data = pd.read_csv("./data/comments_deal.csv")
    # print(train_data.isnull().sum())
    # train_data['CONTENT'] = train_data['CONTENT'].ffill()
    # print(train_data.isnull().sum())

    # train_data.to_csv("./data/comments_dealNan.csv", encoding="utf_8")
    data = data[['CONTENT', 'RATING', 'label']]
    train_data = data[0:10000]
    train_data.info()
    train_data.to_csv("./data/comments_train_1w.csv", encoding="utf_8")
    test_data = data[10000:15000]
    test_data.info()
    test_data.to_csv("./data/comments_test_5k.csv", encoding="utf_8")
    train_data = pd.read_csv("./data/comments_train_1w.csv")
    process = TextPreprocessor(stopword_file="./data/stopwords/stopword_normal.txt")
    transformer = CountVectorizer(analyzer=process.process_line)
    X = train_data.CONTENT
    y = np.array(train_data.label.tolist())
    transformer.fit(X)
    X = transformer.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=11)
    print("X_train: {}, X_test: {}, y_train: {}, y_test: {}".format(X_train.shape, X_test.shape,
                                                                    y_train.shape, y_test.shape))

    transformer_path = './output/bow_transformer_1w.pkl'
    if not os.path.exists(transformer_path):
        pickle.dump(transformer, open(transformer_path, 'wb'))


def fun(a):
    if a < 3:
        return -1
    elif a == 3:
        return 0
    else:
        return 1


def f7():
    # data = pd.read_csv("data/comments_train_10w.csv")
    # data = data[['CONTENT', 'RATING', 'label']]
    # data['label'] = data.apply(lambda x: fun(x.RATING), axis=1)
    # print(data['label'].unique())
    # data.to_csv("./data/comments_train_10w_3class.csv", encoding="utf_8")
    data = pd.read_csv("data/comments_test_5w.csv")
    data = data[['CONTENT', 'RATING', 'label']]
    data['label'] = data.apply(lambda x: fun(x.RATING), axis=1)
    print(data['label'].unique())
    data.to_csv("./data/comments_test_5w_3class.csv", encoding="utf_8")


# f3()
# f4()
# f5()
# f6()
# f7()

# data = pd.read_csv("data/comments_dealNan.csv")
# # print(data.groupby('RATING').size())


def f8():
    data = pd.read_csv("./data/comments_train_50w.csv")
    # data.info()
    # print(data.groupby('RATING').size())
    data = data[['CONTENT', 'RATING', 'label']]
    # data['label'] = data.apply(lambda x: fun(x.RATING), axis=1)
    data_new = pd.DataFrame(columns=['CONTENT', 'RATING', 'label'])
    for i in range(5):
        data_sel = data[data.RATING == (i + 1)]
        data_sel = data_sel[0:20000]
        data_new = data_new.append(data_sel, ignore_index=True)
    print(data_new.groupby('RATING').size())
    print(data_new.groupby('label').size())
    data_new.to_csv("./data/comments_train_10w_5class_uniform.csv", encoding="utf_8")


def f9():
    train_data = pd.read_csv("./data/comments_train_10w_3class_uniform.csv")
    train_data.info()
    process = TextPreprocessor(stopword_file="./data/stopwords/stopword_normal.txt")
    transformer = TfidfVectorizer(analyzer=process.process_line, max_features=50000)
    # transformer = CountVectorizer(analyzer=process.process_line)
    X = train_data.CONTENT
    y = np.array(train_data.label.tolist())
    transformer.fit(X)
    X = transformer.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=11)
    print("X_train: {}, X_test: {}, y_train: {}, y_test: {}".format(X_train.shape, X_test.shape,
                                                                    y_train.shape, y_test.shape))

    transformer_path = './output/tfid_transformer_10w_3class_uniform.pkl'
    if not os.path.exists(transformer_path):
        pickle.dump(transformer, open(transformer_path, 'wb'))


f9()
