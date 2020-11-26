a = 'apple'
a1 = 'apple'[0]

print (a)
print (a1)

a2 = 'apple'[1]

print (a1, a2)
print (a1 + a2)
print (len(a))


print ('l {} Python.'.format('love'))

b = input('Type in a string\n')
print (b.upper())


num = 8
newnum = num/2
print ("new number is: {}".format(int(newnum)))


# The cost of one server per hour.
cost_per_hour = 0.51
# Compute the costs for one server.
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day
# Display the results.
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))


age = input ('Type in age\n')
if int(age) < 35:
    print ('age less than 35\n')
elif int(age)>=35 and int(age) < 60:
    print ('age is greater or equal to 35 and less than 60\n')
else:
    print ('age is greater 60')

# Ask for the distance.
distance = input('How far would you like to travel in miles? ')
# Convert the distance to an integer.
distance = int(distance)
# Determine what mode of transport to use.
if distance < 3:
    mode_of_transport = 'walking'
elif distance < 300:
    mode_of_transport = 'driving'
else:
    mode_of_transport = 'flying'
# Display the result.
print('I suggest {} to your destination.'.format(mode_of_transport))

print ('end\n')

animals = ['man', 'bear', 'pig']
print (animals)
print (animals[0])
animals.insert(2, 'dog')
print (animals)
