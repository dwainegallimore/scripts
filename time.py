import ntplib
from time import ctime


def gettime():
    c = ntplib.NTPClient()
    response = c.request('europe.pool.ntp.org', version=3)
    print ctime(response.tx_time)
    print response.tx_time

gettime()