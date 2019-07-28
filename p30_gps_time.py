import serial, time, os, re, random, datetime, random, sys, subprocess
import Tkinter as tk

s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + "\n"
print(s)

gps_week = 2059
gps_ms = 431591000

# Goal 27-06-2019 23:53:11

days = gps_ms / 1000 / 60 / 60 / 24
h = (gps_ms - (days * 1000 * 60 * 60 * 24)) / 1000 / 60 / 60
min = (gps_ms - (days * 1000 * 60 * 60 * 24) - (h * 1000 * 60 * 60)) / 1000 / 60 
s = (gps_ms - (days * 1000 * 60 * 60 * 24) - (h * 1000 * 60 * 60) - (min * 1000 * 60)) / 1000 

print(str(days))
print(str(h))
print(str(min))
print(str(s))
time = str(h) + ":" + str(min) + ":" + str(s)
print(time)

clip = tk.Tk().clipboard_get()
#print(clip)

log = "Some weird text week=2059 ms=431591000 das 10"

r = re.findall(r'\d+', log)
print(r)

r_week = re.match('week=\d+', log)
print(r_week)
#r_week_number = re.match(r'\d+', r_week)
#print(r_week_number)
#print(str(r_week_number))