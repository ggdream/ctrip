# coding=utf-8
# Author: gdream@126.com


def xtrain(tickets: list) -> list:
    t = []
    for ticket in tickets:
        del ticket['TrainType']
        del ticket['UseTime']
        del ticket['PreSaleDay']
        del ticket['SaleReminder']
        del ticket['order']
        del ticket['Filter']
        del ticket['StartStationCss']
        del ticket['EndStationCss']
        del ticket['FightForTickets']
        del ticket['IsSupportCard']
        del ticket['IsCanHB']
        t.append(ticket)
    return t


def xxtrain(tickets: list) -> list:
    t = []
    for ticket in tickets:
        del ticket['Index']
        if ticket['ShowPriceText'][0] == '?':
            ticket['ShowPriceText'] = ticket['ShowPriceText'][1:-1]
        t.append(ticket)

    return t
