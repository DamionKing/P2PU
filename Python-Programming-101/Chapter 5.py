#5.1(Sum,Count,Average)
sum = 0
count = 0
average = 0
while True:
    number = raw_input('Enter a number: ')
    if number == 'done':
        break
    try:
        numberfloat = float(number)
        count = count + 1
        sum = sum + numberfloat
    except:
        print 'bad data'
if count > 0:
    average = float(sum) / float(count)
print sum, count, average
#5.2(Sum,Count,Min,Max)
min = None
max = None
sum = 0
count = 0
while True:
    number = raw_input('Enter a number: ')
    if number == 'done':
        break
    try:
        numberfloat = float(number)
        count = count + 1
        sum = sum + numberfloat
        if min is None or numberfloat < min:
            min = numberfloat
        if max is None or numberfloat > max:
            max = numberfloat
    except:
        print 'bad data'
print sum, count, min, max