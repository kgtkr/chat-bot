import text
import os
import json

data = ""
dir = "dat/news4vip"
for file in os.listdir(dir)[:100]:
    path = f"{dir}/{file}"
    with open(path, "r") as f:
        reses = [text.text(x[6]) for x in json.loads(f.read())["comments"]]
    for res in reses:
        data += res[0]+"\n"

open("main.txt", 'w').write(data)
