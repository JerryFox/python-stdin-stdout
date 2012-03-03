# -*- coding: utf-8 -*-
"""sample of using stdin and stdout"""

import sys

iinput = "xxx"
while iinput and iinput.count("end") == 0:
    iinput = sys.stdin.readline()
    istring = iinput.replace("\n","")   # remove EOL
    irev_string = ""
    for i in istring:
        irev_string = i + irev_string
    sys.stdout.write(irev_string + "\n")
    
    
