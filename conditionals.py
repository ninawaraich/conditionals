# age = 399
# if (age>= 18 and age <=21):
# 	print'I can vote but i cannot go to a bar!'
# elif age >= 21:
# 	print 'Yay! I can go to a bar and vote'
# else:
# 	print 'aww, I cannot vote or go to a bar'

# number = 8
# number2 = 9
# if (number%2!=0) and (number2%2!=0):
# 	print 'both', number,'and', number2, 'are odd'
# else:
# 	print 'both', number, 'and', number2, 'are not even'


number = 8
number2 = 8
if (number%2==0) and (number2%2!=0):
	print number, "is even and", number2, "is odd"
elif (number%2!=0) and (number2%2==0):
	print number, "is odd and", number2, "is even"
elif (number%2==0) and (number2%2==0):
	print "both numbers are even"
else:
	print "both numbers are odd"
