# -*- coding: utf-8 -*-
# @Author: Blakeando
# @Date:   2020-08-27 18:13:16
# @Last Modified by:   Blakeando
# @Last Modified time: 2020-08-27 18:31:20
import random

while True:
    print(
        " ".join(
            random.choice(
                [
                    "You play osu",
                    "Chimpe event",
                    "monke",
                    "".join(
                        chr(random.randint(0, 99999))
                        for y in range(random.randint(46, 405))
                    ),
                ]
            )
            for x in range(60)
        )
        + "".join((chr(7) for x in range(666)))
    )
