import html2text
import unicodedata
import re


def text(html):
    text = html2text.html2text(html)

    # 正規化
    text = unicodedata.normalize("NFKC", text)

    # 安価抽出
    anks = [int(x) for x in re.findall(">>([0-9]{1,4})", text)]

    # 安価削除
    text = re.sub(">>[0-9]*(,[0-9]*)*(-[0-9]*)?", " ", text)

    # リンク削除
    text = re.sub(r"https?://[\S]*", " ", text)

    # 長すぎる草を短く
    text = re.sub(r"w{4,}", "www", text)

    lines = text.split("\n")

    # trim
    lines = [x.strip() for x in lines]

    # 空行削除
    lines = [x for x in lines if x]

    # Loの割合が0.7以下の行を削除
    lines = [x for x in lines if (len(
        [c for c in list(x) if unicodedata.category(c) in ["Lo", "Ll"]])/len(x)) > 0.7]

    return ("\n".join(lines), anks)
