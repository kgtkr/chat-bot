from gensim.models import word2vec
import os
import json
import text
import MeCab
import io
import pandas as pd


def readDat():
    dir = "dat/news4vip"
    data = []
    for file in os.listdir(dir)[:100]:
        path = f"{dir}/{file}"
        with open(path, "r") as f:
            reses = [text.text(x[6]) for x in json.loads(f.read())["comments"]]
        for res in reses:
            data.append(res[0])
    return data


# http://own-search-and-study.xyz/2017/10/08/mecab%E3%81%A8gensim%E3%81%A7word2vec%E3%83%A2%E3%83%87%E3%83%AB%E3%82%92%E5%AD%A6%E7%BF%92%E3%81%99%E3%82%8B/
def tokenize(sentence):
    try:
        mecab = MeCab.Tagger("-Ochasen")
        data = mecab.parse(sentence)
        data = io.StringIO(data)
        data = pd.read_csv(data, sep='\t', header=None)
        # 名詞のみを使う場合。
        data = data.loc[(data[3].str.find("名詞") >= 0)]
        texts = list(data.iloc[:, 0])
        return texts
    except:
        return []


data = [tokenize(x) for x in readDat()]
print("end token")
model = word2vec.Word2Vec(data, size=100, min_count=5, window=5)
model.save("./main.model")
