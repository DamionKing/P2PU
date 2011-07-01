#3.1(Overtime Pay)
hours = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))
total = round(hours * rate, 2)
if hours > 40:
    overtime = hours - 40
    ovRate = rate * 1.5
    total = overtime * ovRate + rate * 40
print 'Your Pay Is:', '%.2f' % total
#3.2(Pay Idiot Proof)
import sys
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    hours = int(hours)
except:
    print 'Error, Please Enter Numeric Input'
    sys.exit() ##Stop script execution due to error
try:
    rate = float(rate)
except:
    print 'Error, Please Enter Numeric Input'
    sys.exit() ##Stop script execution due to error
pay = hours * rate
print 'Your Pay Is: ', pay
#3.3(Grade Check)
while True:
    try:
      score = float(input('Enter Score: '))
    except ValueError:
      print 'Error, Please enter numeric input'
      continue
    if score > 1 or score < 0:
      print 'Error, Enter a score between 0 and 1'
      continue
    else:
      break
if score >= .9:
    print 'A'
elif score >= .8:
    print 'B'
elif score >= .7:
    print 'C'
elif score >= .6:
    print 'D'
elif score < .6:
    print 'F'
