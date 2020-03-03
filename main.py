# python 3.8.1
# coding=utf-8
# QQ：1586616064
# Author: gdream@126.com

from app import train_sprider
from app.conf import tconf


if __name__ == '__main__':
    conf = tconf()
    train_sprider(conf)
