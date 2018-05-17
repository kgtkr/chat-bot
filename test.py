import text
import os
import json

dir = "dat/news4vip"
for file in os.listdir(dir):
    path = f"{dir}/{file}"
    with open(path, "r") as f:
        reses = [text.text(x[6]) for x in json.loads(f.read())["comments"]]
    for res in reses:
        print(res)
