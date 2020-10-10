from preprocessing import TextPreprocessor
import pickle

while (True):
    s = input("input:")
    preprocessor = TextPreprocessor(stopword_file='./data/stopwords/stopword_normal.txt')
    s = preprocessor.process_line(s)
    transformer = pickle.load(open('./output/bow_transformer_10w_3class_uniform.pkl', "rb"))
    s = transformer.transform(s)
    predict = pickle.load(open('./output_3class/MNB_Model_uniform.pkl', "rb"))
    res = predict.predict(s)
    ans = 0.0
    for i in range(len(res)):
        ans += res[i]
    ans /= len(res)
    check = int(round(ans))
    if check == 1:
        print("好评")
    elif check == 0:
        print("中评")
    else:
        print("差评")
