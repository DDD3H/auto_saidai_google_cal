# How to use auto_saidai_google_cal

1. Set the start and end dates for the term.
```
peri_start = [datetime.date(2021,4,21),datetime.date(2021,7,1)]
peri_end = [datetime.date(2021,6,28),datetime.date(2021,8,26)]

```

** Note: you can set for 2 term **

2. Check if the timetable time setting is correct.
```
class_time_start = [time(9,00),time(10,30),time(13,30),time(15,00),time(16,30)]
class_time_end = [time(10,20),time(11,50),time(14,50),time(16,20),time(17,50)]
```

3. Please output the CSV file according to the Excel file for the timetable setting. The first term is read as "0.csv" and the second term is read as "1.csv".
4. Run "gl_cal.py" in Python
