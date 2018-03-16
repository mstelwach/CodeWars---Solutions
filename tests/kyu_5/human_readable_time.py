import time
import datetime
def make_readable(seconds):
    if seconds < 86400:
        return time.strftime('%H:%M:%S', time.gmtime(seconds))
    else:
        for i in range(1,5):
            counter = 24
            day = str(datetime.timedelta(seconds=seconds))
            strng = time.strftime('%H:%M:%S', time.gmtime(seconds))
            if str(i) == day[0]:
                counter *= i
                if len(strng) == 7:
                    counter = counter + int(strng[1])
                elif len(strng) == 8:
                    counter = counter + int(strng[0:2])
                return str(counter) + strng[2:]

