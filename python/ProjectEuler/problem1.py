#Problem 1
#14 April 2012

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

values = [ ]
count = 1 


while 3 * count < 1000:
    values.append (3 * count)
    count = count + 1

print values

count = 1
while 5 * count < 1000:
    values.append (5 * count)
    count = count + 1
    
print values

values.sort()
print values

uniques = set(values)

print uniques

print sum(uniques)
