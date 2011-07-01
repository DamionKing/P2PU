#6.1(Tardis Reverse)
k = 'Tardis'
i = 0
for letter in k:
  i = i - 1
  print k[i]
#6.2(Prints Out Banana)
fruit = 'banana'
print fruit[:]
#6.3(Print Count Banana)
def count(word):
    count = 0
    for letter in word:
        if letter == 'a' :
            count = count + 1
    print count
word = raw_input('Enter word:')
count(word)
#6.4(Count 'a' in banana)
word='banana'
print word.count('a',0,6)
#6.5(Half String)
str = 'X-DSPAM-Confidence: 0.8475'
halfStr = str[str.find(':')+ 1 :]
print float(halfStr)
#6.6(Various Stuff With Strings)
myName = 'Wesley Mark Pennock: Next Einstein'
print 'The string I will be testing is',myName
print '\nCapitalize:',myName.capitalize() 
print '\nCenter(100, #):',myName.center(100, '#') 
print '\nCount of letter(e):',myName.count('e')
print '\nEndswith (einstein):',myName.endswith('einstein') 
print '\nEndswith (Einstein):',myName.endswith('Einstein') 
myNameSansColon = myName.split(': ')[0] + '{0}' + myName.split(': ')[1]
print '\nSplit name at \': \' and concatonate with \'{0}\':',myNameSansColon 
print '\nFormat split string with {is an}:',myNameSansColon.format(' is '+'the ')
print '\nReplace the letter \'e\' with the word \'blackhole\':',myName.replace('e',' blackhole ')
print '\nStrip \'Einstein\' from my string:',myName.strip('Einstein'),'\n\n' 