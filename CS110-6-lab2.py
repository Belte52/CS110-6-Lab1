###Daniel Ortega
###CS110-week6-lab2
##Calculate Wages

reg_hours = 40
reg_rate = 18.25
ov_rate = 27.78

float = Regular_wage = 730.0
float = OT_wage = 0.0
float = Total_wage = 0.0
workhours = int(input("Hours Worked?"))
OT_hours = workhours - reg_hours
print("OT_hours:", OT_hours)

Regular_Wage = reg_hours * reg_rate
print("Regular_Wage is:", Regular_Wage)


OT_hours = workhours - 40
OT_wage = OT_hours * ov_rate
print("OT_wage:", OT_wage)
    

Total_wage = OT_wage + Regular_wage
print("Total_wage:", Total_wage)  




