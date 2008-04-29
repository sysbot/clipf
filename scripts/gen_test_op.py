#!/usr/bin/python

import datetime
from random import randint

def run():

    prods=['gr%02d.pr%02d' % (gr,pr) for gr in range(10) for pr in range(20)]
    basedate=datetime.date(2000,01,01)
    for day in range(365*5):
        dt=basedate+datetime.timedelta(day)
        dtiso=dt.isoformat()
        print "%s:00:%s:%.2f:1:Note" % (dtiso,prods[0],20.0)
        for i in range(20):
            pr=prods[randint(10,199)]
            print "%s:00:%s:%.2f:0:Note" % (dtiso,pr,1.0)


run()

