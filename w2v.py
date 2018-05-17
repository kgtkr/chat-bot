from gensim.models import word2vec

model = word2vec.Word2Vec.load("./main.model")
results = model.wv.most_similar(positive=['マーシー'])
for result in results:
    print(result)
