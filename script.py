# -*- coding: utf-8 -*-
# @Author: Blakeando
# @Date:   2020-08-27 18:13:16
# @Last Modified by:   Blakeando
# @Last Modified time: 2020-08-27 18:21:35
import sys
try:
    if sys.argv[1] == "cock":
        while True:
            print(' '.join("You play osu" for x in range(60)) + ''.join((chr(7) for x in range(666))))
    else:
        while True:
            print("Chimp event" + ''.join((chr(7) for x in range(666))))
