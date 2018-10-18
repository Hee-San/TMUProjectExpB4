# -*- coding: utf-8 -*-

def unIdentification(DB, Query):
    return 0

def aaaIdentification(DB, Query):
    nDB = len(DB)
    minDif = 999999999
    index = -1
    for i in range(nDB):
        DBimg = DB[i]
        dif = sum(sum(abs(DBimg - Query)))
        if dif < minDif:
            minDif = dif
            index = i
    return index
