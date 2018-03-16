def print_calender(year):
	print '='*12,year,'='*12
	month = 0
	dayone = firstday(year)
	month_name = ['Jan','Feb','Mar','Apr',
				  'May','Jun','Jul','Aug',
				  'Sep','Oct','Nov','Dec']
	month_days = [31,28,31,30,
				  31,30,31,31,
				  30,31,30,31]
	day_name = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
	if lunar_year(year):
		month_days['Feb'] = 29
	for n in month_name:
		print n
		print '='*28
		for d in day_name:
			print d,
		print
		
		everyday(dayone,month)
		dayone = (dayone+month_days[month])%7
		
		print '\n\n'
		month += 1
		
		
def everyday(day1,month):
	month_days = [31,28,31,30,
				  31,30,31,31,
				  30,31,30,31]
	print '%s'%('  '*(2*day1-1)),
	for m in range(month_days[month]):
		print '%+03s'%(m+1),
		if (day1+(m+1))%7 == 0:
			print
		
		

def lunar_year(x):
	if (x%4 == 0 and x%100 != 0) or (x%400 == 0):
		return True
	
def firstday(x):
	passed = 0 #Record how many days has passed since 1900
	for i in range(1900,x):
		if lunar_year(i):
			passed += 1
	passed += 365*(x-1900)
	day = (passed+1)%7 #1 = Mon;2 =Tue;...;6 = Sat;0 = Sun.
	return day
	
if __name__ == '__main__':
	x = int(input('Please enter the year(>1900)...'))
	print_calender(x)