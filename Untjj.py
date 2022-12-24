
import numpy
def calcDays(month, year):
	date = 0

	
	if month == 12:
		end = str(year)+'-'+str(month)+'-31'
		begin = str(year)+'-'+str(month)+'-01'
		date = 1
	else:

		
		if month < 10:
			endM = '-0'+str(month+1)
			beginM = '-0'+str(month)

		
		else:
			endM = '-'+str(month+1)
			beginM = '-'+str(month)

		end = str(year)+endM+'-01'
		begin = str(year)+beginM+'-01'

	
	return (numpy.datetime64(end) - numpy.datetime64(begin)+date)



month = 4


year = 2001


print(calcDays(month, year))
