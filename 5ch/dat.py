import config
import hashlib
import hmac
import urllib.request
import urllib


def get_dat(sid: str, server: str, board: str, key: str) -> str:
    message = f"/v1/{server}/{board}/{key}" + sid + config.APP_KEY
    hobo = hmac.new(config.HM_KEY, message.encode(
        'utf-8'), hashlib.sha256).hexdigest()

    url = f'https://api.5ch.net/v1/{server}/{board}/{key}'
    values = {'sid': sid, 'hobo': hobo, 'appkey': config.APP_KEY}
    headers = {'User-Agent': config.UA}
    data = urllib.parse.urlencode(values).encode('utf-8')
    res = urllib.request.urlopen(urllib.request.Request(
        url, data, headers))
    return res.read().decode("sjis")
