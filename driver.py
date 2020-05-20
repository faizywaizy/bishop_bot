"""

1) Connect to the window
2)  Write Script
3) Convert to send_keys() with delays with time.sleep()
    - Buffs // done
    - Heals // not done, using pet pot
    - Telecasting -> not done, need to figure out simulating it
    // later
    - minor randomization

4) add location detection using minimap
5) add

"""

import time
from datetime import datetime

from random import randrange

from pywinauto import *
from pywinauto.keyboard import send_keys
from telecast import *


def buff_HS_MW():
    send_keys('{d down}'
              '{d up}'
              )
    time.sleep(3)


def buff_MG_OTHER():
    send_keys('{f down}'
              '{f up}'
              )
    time.sleep(3)

def feed_pet():
    send_keys('{n down}'
              '{n up}'
              )


if __name__ == '__main__':
    app = Application().connect(handle=0x00140B1C)
    print("Connected!")

    dlg = app.top_window()

    start = datetime.utcnow()
    run_time = 3600 * 1.75  # 1 hour
    dlg.set_focus()

    buff_HS_MW()
    buff_MG_OTHER()
    feed_pet()

    buff_timer = time.perf_counter()
    pet_timer = time.perf_counter()

    while (datetime.utcnow() - start).total_seconds() < run_time:
        dlg.set_focus()

        if time.perf_counter() - buff_timer > 110:
            move_to_x_target(-270)
            buff_HS_MW()
            buff_MG_OTHER()
            buff_timer = time.perf_counter()

        if time.perf_counter() - pet_timer > 300:
            feed_pet()
            pet_timer = time.perf_counter()

        platform_attack()

    send_keys('%{F4 down}'
              '%{F4 up}'
              )


