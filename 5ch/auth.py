import urllib.request
import urllib
import hmac
import hashlib
import config


def auth() -> str:
    hb = hmac.new(config.HM_KEY, (config.APP_KEY +
                                  config.CT).encode('utf-8'), hashlib.sha256).hexdigest()
    url = 'https://api.5ch.net/v1/auth/'
    values = {'KY': config.APP_KEY, 'CT': config.CT, 'HB': hb}
    headers = {'User-Agent': config.UA, 'X-2ch-UA': config.X_2ch_UA}
    data = urllib.parse.urlencode(values).encode('utf-8')
    res = urllib.request.urlopen(urllib.request.Request(
        url, data, headers))
    return res.read().decode("utf-8").split(':')[1]
