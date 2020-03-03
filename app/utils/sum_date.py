# coding=utf-8
# Author: gdream@126.com
import datetime
from dateutil.relativedelta import relativedelta


def adate(ddate: str) -> str:
    d = datetime.datetime.strptime(ddate, '%Y-%m-%d')
    return (d + relativedelta(days=2)).strftime('%Y-%m-%d')


def date_(ddate: int) -> str:
    ddate = str(ddate)
    return '-'.join((ddate[0:4], ddate[4:6], ddate[6:8]))
