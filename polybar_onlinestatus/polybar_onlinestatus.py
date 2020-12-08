#!/usr/bin/env python
import argparse


class OnlineStatus:
    """"""
    def __init__(self):
        self.url = "https://google.com"
        self.parser = argparse.ArgumentParser()
        self.cache_timeout = 10
        self.timeout = 2
        self.offline_icon = ""
        self.online_icon = ""
        self.color = {
            "reset": "\u001b[0m",
            "offline": "\u001b[31m",
            "online": "\u001b[32m"
        }
        self.parser.add_argument("--boolean-mode", dest="boolean_mode", help="Returns boolean value if True, network icon if False", action="store_true")
        self.parser.add_argument("--color-mode", dest="color_mode", help="Sets color to result if True", action="store_true")

        self.args = self.parser.parse_args()
        if self.args.boolean_mode:
            self.boolean_mode = True
        else:
            self.boolean_mode = False
        self.args = self.parser.parse_args()
        if self.args.color_mode:
            self.color_mode = True
        else:
            self.color_mode = False

    def check_online(self):
        from urllib.request import urlopen
        from urllib.error import URLError
        from subprocess import call
        if "://" in self.url:
            try:
                urlopen(self.url, timeout=self.timeout)
                return True
            except URLError:
                return False
        else:
            try:
                return call(['ping', '-c', '1', self.url]) == 0
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
                return f"{self.color['online'] if self.check_online() else self.color['offline']}{self.check_online()}"
            else:
                return self.check_online()
        else:
            if self.color_mode is True:
                if self.check_online():
                    return f"{self.color['online']}{self.online_icon}{self.color['reset']}"
                else:
                    return f"{self.color['offline']}{self.offline_icon}{self.color['reset']}"
            else:
                if self.check_online():
                    return f"{self.online_icon}"
                else:
                    return f"{self.offline_icon}"


def main():
    return OnlineStatus().online_result()


# print(main()) # For testing purposes
