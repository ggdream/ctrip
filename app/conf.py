# coding=utf-8
# Author: gdream@126.com
from yaml import load, SafeLoader


class Config:
    def __init__(self):
        with open('config.yaml', 'r', encoding='utf-8')as f:
            self.config = load(f.read(), Loader=SafeLoader)

    def conf_train(self) -> dict:
        return self.config

    def conf_airpl(self) -> dict:
        pass


def tconf() -> dict:
    if sure := input('若使用配置文件，请输入任意字符后回车：'):
        conf = Config()
        ttconf = conf.conf_train()
    else:
        print("="*400)
        ddate = input('启程日期：')
        dcity = input('始发城市：')
        acity = input('目标城市：')
        print("="*400)
        ttconf = {
            'use': False,
            'ddate': int(ddate),
            'dcity': dcity,
            'acity': acity,
            'visual': True
        }
    return ttconf

