#4.1(Random Number Generator)
import random
for i in range(10):
    x = random.random()
print (x)

#4.2(Repeat Lyrics Not Defined)
#repeat_lyrics()
#def print_lyrics():
#   print ("I'm a lumberjack, and I'm okay.")
#   print ('I sleep all night and I work all day.')
#def repeat_lyrics():
#   print_lyrics()
#   print_lyrics()

#4.3(Repeat Lyrics)
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print ("I'm a lumberjack, and I'm okay.")
    print ('I sleep all night and I work all day.')
repeat_lyrics()
#4.4(Compute Pay)
def computepay(hours, rate, total):
    if hours > 40:
        overtime = hours - 40
        otRate = rate * 1.5
        total = overtime * otRate + rate * 40
    print 'Pay:', '%.2f' % total
hours = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))
total = round(hours * rate, 2)
computepay(hours, rate, total)


#4.4(Compute Pay)
def computepay(hours, rate, total):
    if hours > 40:
        overtime = hours - 40
        otRate = rate * 1.5
        total = overtime * otRate + rate * 40
    print 'Pay:', '%.2f' % total
hours = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))
total = round(hours * rate, 2)
computepay(hours, rate, total)

#4.5(Compute Grade)
def computegrade(score):
    if score >= .9:
        print 'A!'
    elif score >= .8:
        print 'B'
    elif score >= .7:
        print 'C'
    elif score >= .6:
        print 'D'
    elif score < .6:
        print 'F'
while True:
    try:
      score = float(input('Enter Score: '))
    except ValueError:
      print ('Error, Please enter numeric input')
      continue
    if score > 1 or score < 0:
      print ('Error, Enter a score between 0 and 1')
      continue
    else:
      break
computegrade(score)

#

