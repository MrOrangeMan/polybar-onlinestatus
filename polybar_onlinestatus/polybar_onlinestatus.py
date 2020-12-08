#!/usr/bin/env python
import argparse
from time import sleep


class OnlineStatus:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.offline_icon = "  "
        self.online_icon = "  "
        self.color = {
            "end": "%{F-}",
            "offline": "%{F#f00}",
            "online": "%F{#080}"
        }
        self.parser.add_argument("-bm", "--boolean-mode", dest="boolean_mode", help="Returns boolean value if True, network icon if False", action="store_true")
        self.parser.add_argument("-cm", "--color-mode", dest="color_mode", help="Sets color to result if True", action="store_true")
        self.parser.add_argument("-ct", "--cache-timeout", type=int, metavar="REFRESH_RATE", dest="cache_timeout", help="Specify cache refresh rate in seconds, defaults to 5")
        self.parser.add_argument("-ut", "--url-timeout", type=int, metavar="TIMEOUT", dest="url_timeout", help="Specify URL ping timeout in seconds, defaults to 2")
        self.parser.add_argument("-l", "--link", "--url", type=str, metavar="URL", dest="url", help="Specify URL that will be used to verify connection, defaults to 'https://google.com'")
        self.args = self.parser.parse_args()
        self.cache_timeout = self.args.cache_timeout if self.args.cache_timeout is not None else 5
        self.timeout = self.args.url_timeout if self.args.url_timeout is not None else 2
        self.url = self.args.url if self.args.url is not None else "https://google.com"
        if self.args.boolean_mode:
            self.boolean_mode = True
        else:
            self.boolean_mode = False
        if self.args.color_mode:
            self.color_mode = True
        else:
            self.color_mode = False

    def check_online(self):

        from urllib.request import urlopen
        from urllib.error import URLError
        from subprocess import call, DEVNULL
        if "://" in self.url:
            try:
                urlopen(self.url, timeout=self.timeout)
                return True
            except URLError:
                return False
        else:
            try:
                return call(['ping', '-c', '1', '-W', f'{self.timeout}', f'{self.url}'], stdout=DEVNULL, stderr=DEVNULL) == 0
            except URLError:
                return False

    @property
    def ping_url(self):
        return self.url

    @ping_url.setter
    def ping_url(self, new_url):
        self.url = new_url

    def online_result(self):
        if self.boolean_mode is True:
            if self.color_mode is True:
                return f"{self.color['online'] if self.check_online() else self.color['offline']}{self.check_online()}{self.color['end']}"
            else:
                return self.check_online()
        else:
            if self.color_mode is True:
                if self.check_online():
                    return f"{self.color['online']}{self.online_icon}{self.color['end']}"
                else:
                    return f"{self.color['offline']}{self.offline_icon}{self.color['end']}"
            else:
                if self.check_online():
                    return f"{self.online_icon}"
                else:
                    return f"{self.offline_icon}"


def main():
    while True:
        sleep(OnlineStatus().cache_timeout)
        return OnlineStatus().online_result()


# print(main())  # For testing purposes

