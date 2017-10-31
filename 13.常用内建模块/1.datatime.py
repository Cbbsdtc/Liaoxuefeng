from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

#指定某个日期和时间
dt = datetime(2015, 4, 19, 12, 20, 22)
print(dt)

#datetime转换为timestamp
dts = dt.timestamp()
print(dts)

#timestamp转换为datetime
t = 1428412424
print(datetime.fromtimestamp(t))

#str转换为datetime 转换后的datetime是没有时区信息的
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime加减
from datetime import timedelta
now = datetime.now()
now + timedelta(hours=10)
now - timedelta(days=1)
now + timedelta(days=2, hours=12)
