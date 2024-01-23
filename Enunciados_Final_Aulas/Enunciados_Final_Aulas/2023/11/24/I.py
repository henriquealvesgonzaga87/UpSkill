# I - Introduction to Python Language (5 marks)
#
# Make a program to calculate a payroll, knowing that the discounts
# are the Income Tax (IT), which depends on the gross salary
# (as shown in the table below) and 10% for the Union (INSS)
# and that the FGTS corresponds to 11% of the Gross Salary,
# but it is not deducted (it is the company that deposits).
# Net Salary corresponds to Gross Salary minus discounts.
# The program should ask the user for the hourly rate and
# the number of hours worked in the month. Do all data entry
# validations and result formatting.
# IR discount:
# Gross Salary up to 900 (inclusive) - exempt
# Gross Salary up to 1500 (inclusive) - 5% discount
# Gross Salary up to 2500 (inclusive) - 10% discount
# Gross Salary above 2500 - 20% discount Print the information on the screen, arranged according to the example below. In the example the hour value is 5 and the hour amount is 220.
#
# Gross Salary: (5 * 220) : 1100.00
# (-) IT (5%).............:   55.00
# (-) INSS (10%)..........:  110.00
# FGTS (11%)..............:  121.00
# Total discounts.........:  165.00
# Net Salary..............:  935.00
#
#


# while True:
#     try:
#         hourly_rate = float(input(("Hourly rate ?")))
#     except:
#         continue
#     if hourly_rate > 0:
#         break
#
# while True:
#     try:
#         number_hours_worked = float(input(("Nmber of hours worked ?")))
#     except:
#         continue
#     if number_hours_worked > 0:
#         break


hourly_rate = 8
number_hours_worked = 55

gs = hourly_rate * number_hours_worked
if gs <= 900:
    it = 0
elif gs <= 1500:
    it = 5
elif gs <= 2500:
    it = 10
else:
    it = 20

vit = round(gs * it/100.0, 2)
inss = round(gs * .1, 2)
fgts = round(gs * .11, 2)
td = vit + inss
ns = gs - td


dots = "({} * {})".format(hourly_rate, number_hours_worked)
dots = dots + "." * (11 - len(str(dots)))
print("Gross Salary {}:{:8.2f}".format(dots, gs))
dots = "({:d}%)".format(it)
dots = dots + "." * (17 - len(str(dots)))
print("(-) IT {}:{:8.2f}".format(dots, vit))
print("(-) INSS (10%)..........:{:8.2f}".format(inss))
print("FGTS (11%)..............:{:8.2f}".format(fgts))
print("Total discounts.........:{:8.2f}".format(td))
print("Net Salary..............:{:8.2f}".format(ns))

