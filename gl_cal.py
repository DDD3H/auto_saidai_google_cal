# -*- coding: utf-8 -*-

import pandas as pd
import datetime
import csv

######Definition#######
Frame = []

def bool_check(x):
	if x == 'FALSE':
		return False
	elif x == 'TRUE':
		return True

def time(hours,minutes):
	if hours*60 + minutes >= 24*60:
		return False
	else:
		return hours*60 + minutes

def dis_time(x):
	hours_ = x // 60
	minutes_ = x % 60
	if minutes_ == 0:
		nu = '00'
		if hours_ <= 12:
			return str(hours_) + ':' + nu + ' ' + 'AM'
		else:
			hours_cov = hours_ - 12
			return str(hours_cov) + ':' + nu + ' ' + 'PM'
	else:
		if hours_ <= 12:
			return str(hours_) + ':' + str(minutes_) + ' ' + 'AM'
		else:
			hours_cov = hours_ - 12
			return str(hours_cov) + ':' + str(minutes_) + ' ' + 'PM'

def days(x):
	days_list = ['Monday','Tuesday','Wednesday','Thursday','Friday']
	for i in range(5):
		if x == days_list[i]:
			return i


class_time_start = [time(9,00),time(10,30),time(13,30),time(15,00),time(16,30)]
class_time_end = [time(10,20),time(11,50),time(14,50),time(16,20),time(17,50)]


def caculater(Term_Pre_start,Term_Pre_end,csv_name):
	

	f = open(csv_name, 'r',encoding='shift_jis')

	for i in csv.reader(f):
		list_ =  []
		Start_Date = Term_Pre_start

		start_count = days(i[2]) - days(Term_Pre_start.strftime('%A'))
		if start_count >= 0:
			Start_Date = Term_Pre_start + datetime.timedelta(days=start_count)
		elif start_count < 0:
			Start_Date = Term_Pre_start + datetime.timedelta(days=7) + datetime.timedelta(days=start_count)

		while Start_Date <= Term_Pre_end:
			list_ = []
			list_.append(i[0]) #Add 'Subject'
			list_.append(Start_Date.strftime('%Y/%m/%d'))
			list_.append(dis_time(class_time_start[int(i[1])-1]))
			list_.append(Start_Date.strftime('%Y/%m/%d'))
			list_.append(dis_time(class_time_end[int(i[1])-1]))
			list_.append('FALSE')
			list_.append(i[4])
			list_.append('')
			list_.append('FALSE')

			if bool_check(i[3]):
				if Start_Date.strftime('%A') == 'Monday' or Start_Date.strftime('%A') == 'Tuesday':
					Start_Date = Start_Date + datetime.timedelta(days=2)
				elif Start_Date.strftime('%A') == 'Wednesday' or Start_Date.strftime('%A') == 'Thursday':
					Start_Date = Start_Date + datetime.timedelta(days=5)
				elif Start_Date.strftime('%A') == 'Friday' and (i[1] == '2' or i[1] == '4'):
					list_.append(i[0]) #Add 'Subject'
					list_.append(Start_Date.strftime('%Y/%m/%d'))
					list_.append(dis_time(class_time_start[int(i[1])]))
					list_.append(Start_Date.strftime('%Y/%m/%d'))
					list_.append(dis_time(class_time_end[int(i[1])]))
					list_.append('FALSE')
					list_.append(i[4])
					list_.append('')
					list_.append('FALSE')
					Start_Date = Start_Date + datetime.timedelta(days=7)
			else:
				Start_Date = Start_Date + datetime.timedelta(days=7)

			Frame.append(list_)

#######################



columns_list = ['Subject','Start Date','Start Time', 'End Date','End Time', 'All Day Event', 'Description', 'Location', 'Private']

peri_start = [datetime.date(2021,4,21),datetime.date(2021,7,1)]
peri_end = [datetime.date(2021,6,28),datetime.date(2021,8,26)]

for i in range(2):
	caculater(peri_start[i],peri_end[i],str(i)+'.csv')

df = pd.DataFrame(Frame, columns=columns_list)
print(df.head())
df.to_csv("gl.csv",index=False)

