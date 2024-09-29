"""
Bu propgram Yiğit çıtak tarafından
GNU/Linux sistemler için programlanmıştır.
Sürüm tutmayan bir programdır

Terminal anlık saat programı:
"""

import time
import sys

while True:
    try:
        current_time = time.strftime("%H:%M:%S")

        sys.stdout.write(f'\r|Terminal saati|  Saat: {current_time}  ₺')
        sys.stdout.flush()

    except:
        print("")
        sys.exit()
