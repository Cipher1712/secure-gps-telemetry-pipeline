import gps

session = gps.gps(mode=gps.WATCH_ENABLE)

while True:
    report = session.next()
    print(report)