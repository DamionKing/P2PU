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
while True:   
    file = raw_input('Enter a filename: ')
    try:
      f = open(file, 'rU')
      break
    except:
      print('Enter a valid filename: ')
      continue
spamlines=0
spamtotal=0
for line in f:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    colonposition = line.find(':') 
    spamtotal = spamtotal + float(line[colonposition+1:]) 
    spamlines = spamlines + 1 
print 'Average spam confidence:', spamtotal/spamlines 
#7.3(Easter Egg)
file = raw_input('Enter a filename: ')
if file== 'mbox-short.txt':
        print('Was up, this is an egg fool!Haha jk!')  
exit()  
try: fh = open(file) 
except: 
    print 'File cannot be opened:', file

        
    
