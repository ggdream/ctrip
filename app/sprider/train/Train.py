# coding=utf-8
# Author: gdream@126.com
import logging
import requests
from random import choice
from xpinyin import Pinyin
from urllib.parse import urlencode, quote
from useragentxxc import PersonComputer as pc

from app.model import RedisClient
from app.utils import adate, xtrain, xxtrain, proxy_tools, train_once_table, train_transfer_table


p = Pinyin()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s：   %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


def train_once(dcity: str, acity: str, ddate: int, IsGaoTie='false', IsDongChe='false', proxy=None) -> list:
    url = "https://trains.ctrip.com/TrainBooking/Ajax/SearchListHandler.ashx?Action=getSearchList"
    headers = {
        "Origin": "https://trains.ctrip.com",
        "Referer": f"https://trains.ctrip.com/TrainBooking/Search.aspx?from={p.get_pinyin(dcity, '')}&to={p.get_pinyin(acity, '')}&day={ddate}&fromCn={quote(quote(dcity))}&toCn={quote(quote(acity))}",
        "User-Agent": pc.random(),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        'value': '{"IsBus":false,"Filter":"0","Catalog":"","IsGaoTie":%s,"IsDongChe":%s,"CatalogName":"","DepartureCity":%s,"ArrivalCity":%s,"HubCity":"","DepartureCityName":%s,"ArrivalCityName":%s,"DepartureDate":%s,"DepartureDateReturn":%s,"ArrivalDate":"","TrainNumber":""}' % (IsGaoTie, IsDongChe, p.get_pinyin(dcity, ""), p.get_pinyin(acity, ""), dcity, acity, ddate, adate(str(ddate)))
    }
    try:
        response = requests.post(url, headers=headers, data=urlencode(data), proxies=proxy_tools(proxy), timeout=1).json()
        if detailed := response['TrainItemsList']:
            logger.info(f"[{ddate}] {dcity}-->{acity}")
            return xtrain(detailed)
        else:
            logger.warning(f"[{ddate}] {dcity}-->{acity}：But no train number")
    except Exception as e:
        logger.error(f"[{ddate}] {dcity}-->{acity}：{e}")


def train_transfer(dcity: str, acity: str, ddate: str, proxy=None) -> list:
    url = "https://trains.ctrip.com/TrainBooking/Ajax/SearchListHandler.ashx?Action=getTransferList"
    headers = {
        "Origin": "https://trains.ctrip.com",
        "Referer": f"https://trains.ctrip.com/TrainBooking/Search.aspx?from={p.get_pinyin(dcity, '')}&to={p.get_pinyin(acity, '')}&day={ddate}&number=&fromCn={quote(quote(dcity))}&toCn={quote(quote(acity))}",
        "User-Agent": pc.random(),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        'value': '{"departure":%s,"arrive":%s,"date":%s}' % (dcity, acity, ddate)
    }
    try:
        response = requests.post(url, headers=headers, data=urlencode(data), proxies=proxy_tools(proxy), timeout=1).json()
        if response:
            logger.info(f"[{ddate}] {dcity}- * ->{acity}")
            return xxtrain(response)
        else:
            logger.warning(f"[{ddate}] {dcity}- * ->{acity}：But no train number")
    except Exception as e:
        logger.error(f"[{ddate}] {dcity}- * ->{acity}：{e}")


def train_sprider(config=None):
    if config['use']:
        client = RedisClient(config['redis'])
        for key in config['trip']['route']:
            print("="*400)

            data1 = train_once(key, config['trip']['route'][key], config['trip']['ddate'], proxy=choice(config['proxy']))
            data2 = train_transfer(key, config['trip']['route'][key], config['trip']['ddate'], proxy=choice(config['proxy']))

            client.set(f'{config["trip"]["ddate"]} {key}{config["trip"]["route"][key]}', {'once': data1, 'more': data2})

            if config['visual']:
                train_once_table(data1)
                train_transfer_table(data2)

            print("="*400)
    else:
        print("="*400)
        train_once_table(train_once(config['dcity'], config['acity'], config['ddate']))
        print("="*400)
        train_transfer_table(train_transfer(config['dcity'], config['acity'], config['ddate']))
        print("="*400)
