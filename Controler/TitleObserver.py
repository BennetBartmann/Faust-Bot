import re
import urllib
from urllib import request

from Communication.Connection import Connection
from Controler.PrivMsgObserverPrototype import PrivMsgObserverPrototype


def beautify_title(title):
    """
    main purpose: make tweets nicer
    :param title: string to beautify

    """
    return title


class TitleObserver(PrivMsgObserverPrototype):

    def update_on_priv_msg(self, data):
        url = re.search("(?P<url>https?://[^\s]+)", data['message'])
        if url is not None:
            print(url)
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
                url = url.string
                req = urllib.request.Request(url, None, headers)
                resource = urllib.request.urlopen(req)
                encoding = resource.headers.get_content_charset()
                # der erste Fall kann raus, wenn ein anderer Channel benutzt wird
                if url.find('rehakids.de') != -1:
                    encoding = 'windows-1252'
                if not encoding:
                    encoding = 'utf-8'
                content =  resource.read().decode(encoding)
                titleRE = re.compile("<title>(.+?)</title>")
                title = titleRE.search(content).group(1)
                title = beautify_title(title)
                print(title)
                Connection.singleton().send_channel(title)
            except Exception as exc:
                print(exc)
                pass