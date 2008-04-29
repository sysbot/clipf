#!/usr/bin/python

def run():

    for gr in range(10):
        if gr:
            dc='0'
        else:
            dc='1'
        print "gr%02d.:0:Group %02d" % (gr,gr)
        for pr in range(20):
            print "gr%02d.pr%02d:%s:Product %02d%02d" % (gr,pr,dc,gr,pr)

run()

