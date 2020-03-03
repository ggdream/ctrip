# coding=utf-8
# Author: gdream@126.com
from prettytable import PrettyTable


def train_once_table(tickets: list):
    table = PrettyTable()
    table.field_names = ["No",
                         "Train",
                         "始发站",
                         "目标站",
                         "发车时间",
                         "抵达时间",
                         "TakeDays",
                         "TakeTime",
                         "MinPrice",
                         "可购买",
                         "可预订"]

    for i, t in enumerate(tickets):
        table.add_row([i + 1,
                       t['TrainName'],
                       t['StartStationName'],
                       t['EndStationName'],
                       t['StratTime'],
                       t['EndTime'],
                       t['TakeDays'],
                       t['TakeTime'],
                       t['TrainMinPrice'],
                       t['IsDirect'],
                       t['IsBookable']])

    print(table)


def train_transfer_table(tickets: list):
    table = PrettyTable()
    table.field_names = ["No",
                         "启程站",
                         "终点站",
                         "中转站",
                         "中途空余",
                         "总耗时",
                         "MinPrice"]
    for i, t in enumerate(tickets):
        table.add_row([i + 1,
                       t['DepartStation'],
                       t['ArriveStation'],
                       t['TransferStation'],
                       t['TransferTakeTime'],
                       t['TotalRuntime'],
                       t['ShowPriceText']
                       ])
    print(table)
