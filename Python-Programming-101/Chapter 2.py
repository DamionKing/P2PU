#2.1(Print X)
x = 5
x = x + 1
print(x)

#2.2(Hello Name)
name = raw_input('Enter your name:') 
print 'Hello '+ name

#2.3(Print Pay)
hours = int(raw_input("Enter Hours: "))
rate = float(raw_input("Enter Rate: "))
pay = int(hours) * float(rate)
print 'Your Pay Is: ', pay

#2.4(Print Width(int),Width(double),height(int))
width = 17
height = 12.0
print width / 2
print width / 2.0
print height / 3
print 1 + 2 * 5

#2.5(Convert Celsius to Fahrenheit & Print)
c = input('Convert Celsius to Fahrenheit\nEnter Temperature:')
conversion = float(c) * 9.0 / 5.0 + 32
print conversion 
