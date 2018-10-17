# coding: utf-8

# from でモジュールを読み込んで import でクラスを呼ぶ
from datetime import datetime, timedelta, timezone

today = datetime.now()
print(today)

# jp time
jst      = timezone(timedelta(hours=9))
today_jp = datetime.now(jst)
print(today_jp)

print(today_jp.year)
print(today_jp.month)
print(today_jp.day)

# create datetime object
day = datetime.strptime('2010-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")
print(day)