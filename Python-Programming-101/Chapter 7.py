#7.1(Capitalize & Read From File)
while True:   
    file = raw_input('Enter a filename: ')
    try:
      f = open(file, 'rU')
      break
    except:
      print('Enter a valid filename: ')
      continue
for line in f:
    print line.rstrip().upper()
#7.2(Average Spam Confidence)
#7.3(Easter Egg)
