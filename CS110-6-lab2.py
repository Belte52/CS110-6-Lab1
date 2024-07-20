###Daniel Ortega
###CS110-week6-lab2

#workhours = input('workhours')
reg_wage = input('reg_wage')
#reg_hours = input('reg_hours')
#reg_rate = input('reg_rate')
#ov_rate = input('ov_rate')
ov_wage = input('ov_wage')
#overtime = input('overtime')
print("reg_wage = " + reg_wage)
print("ov_wage = " + ov_wage)

OT = float('overtime')
WH = float('workhours')
RH = float('reg_hours')
RR = float('reg_rate')
OTR= float('ov_rate')
RW = float('reg_wage')
OTW= float('ov_wage')

float = RH = 40
float = OT = 0.0
float = OTW  = 0.0
float = OTR = 27.78
float = WH = 50.
float = RW = 730.0
float = RR = 18.25

OT =  WH - RH
OTW = OT * OTR
RW = RH * RR
total_wage = RW + OTW

#print('reg_wage')
#print('ov_wage')
print('total_wage')