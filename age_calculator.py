from datetime import date


def get_dob():
    # write code here
	year = int(input('Enter year of birth: '))
	month = int(input('Enter month of birth: '))
	day = int(input('Enter day of birth: '))
	dob = date(year, month, day)
	
	return dob
	#newcomment
	# if (dob > datetime..now()):
	# 	print('not a valid date')
	# else: 
	# 	get_age(dob)


def get_age(dob):
    # write code here
	age = int(str(date.today() - dob).split(" ")[0]) // 365

	return str(age)
	


def main():
	# write code here
	dob = get_dob()
	age = get_age(dob)

	if (dob > date.today()):
		print('not a valid date')
	else: 
		print('you are ' + age + ' years old.') 



if __name__ == '__main__':
    main()
