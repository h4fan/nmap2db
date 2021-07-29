#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, datetime

db_str = 'nmapscanresult.db'

def gettime():
    timenow = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    timetext = timenow.strftime('%Y/%m/%d')
    return timetext


def log2db(host, ip, port, state, protocol, service, version, scandate ):

    conn = sqlite3.connect(db_str)
    c = conn.cursor()
    c.execute("insert into records values(?,?,?,?,?,?,?,?)",(host, str(ip), port, str(state), str(protocol), str(service), str(version),str(scandate)))
    conn.commit()
    conn.close()


def parseresult(scanline):
    rec = scanline.split("\t")
    ip = rec[0].split(" ")[1]
    # print(ip,)
    ports = rec[1].split(":",1)[1]
    for pr in ports.split(","):
        pr = pr.strip()
        prlist = pr.split("/")
        print(ip,prlist[0],prlist[1],prlist[2],prlist[4],prlist[6])
        log2db("",ip,prlist[0],prlist[1],prlist[2],prlist[4],prlist[6],gettime())


with open("scanresult.txt","r") as fin:
    lines = fin.readlines()
    for line in lines:
        line = line.strip()
        if(line[0] == "#"):
            continue
        if(len(line.split("\t")) == 2):
            continue
        parseresult(line)

