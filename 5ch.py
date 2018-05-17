import urllib.request
import json
import os


class Thread():
    def __init__(self, data):
        self.server = data[2]
        data3 = data[3].split("/")
        self.board = data3[0]
        self.key = data3[1]


def req(url):
    with urllib.request.urlopen(urllib.request.Request(url, None, {"User-Agent":  ua})) as res:
        return json.loads(res.read().decode("utf-8"))


ua = "Mozilla/4.0"
boards = ["news4vip", "livejupiter", "newsplus", "poverty", "famicom"]

while True:
    print("開始")
    for board in boards:
        try:
            print(board)
            ths = [Thread(th) for th in req(
                f"https://itest.5ch.net/subbacks/{board}.json")["threads"]]
            for th in ths:
                print(th.key)
                data = json.dumps(req(
                    f"https://itest.5ch.net/public/newapi/client.php?subdomain={th.server}&board={th.board}&dat={th.key}"))
                dir = f"dat/{th.board}"
                path = f"{dir}/{th.key}.json"
                os.makedirs(dir, exist_ok=True)
                open(path, 'w').write(data)
        except Exception:
            print("エラー")
