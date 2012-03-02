# -*- coding: utf-8 -*-
import sys

vstup = "xxxx"
while vstup and vstup.count("konec") == 0:
    vstup = sys.stdin.readline()
    ret = vstup.replace("\n","")
    iret = ""
    for i in ret:
        iret = i + iret
    sys.stdout.write(iret + "\n")
    
    
