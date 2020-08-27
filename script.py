# -*- coding: utf-8 -*-
# @Author: Blakeando
# @Date:   2020-08-27 18:13:16
# @Last Modified by:   Blakeando
# @Last Modified time: 2020-08-27 18:25:43
import random

while True:
    print(
        " ".join(
            random.choice(["You play osu", "Chimpe event", "monke"]) for x in range(60)
        )
        + "".join((chr(7) for x in range(666)))
    )
