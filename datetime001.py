i##今日の日付を取得
import datetime
datetime.date.today()

datetime.datetime.now()


###日付のオブジェクトの使用方法###
# datetime.date(年, 月, 日)

new_years_day = datetime.date(2019, 1, 1)
new_years_day

new_years_day - datetime.date.today()
#timedeltaが表示され、あと何日かわかる

datetime.timedelta(14)

datetime.date.today() + datetime.timedelta(14)
