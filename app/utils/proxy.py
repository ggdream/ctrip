# coding=utf-8
# Author: gdream@126.com


def proxy_tools(proxy: str):
    if proxy is None:
        return None
    else:
        return {'http': proxy, 'https': proxy}
