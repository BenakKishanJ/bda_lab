import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    date, temp = line.split(',')
    temp = int(temp)
    if temp > 30:
        msg = "Hot Day"
    elif temp < 10:
        msg = "Cold Day"
    else:
        msg = "Pleasant Day"

    print("%s\t%s" % (date, msg))
