month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February','December'):
	season = 'winter'
elif month in ('march','April', 'May'):
	season = 'summer'
elif month in ('june''July', 'August'):
	season = 'spring'
elif month in ('september','october','November'):
        season='fall'
else:
	season = 'autumn'


if (month == 'March' and day >= 20):
	season = 'summer'

elif (month == 'June' and day >= 21):
	season = 'summer'

elif (month == 'September' and day>= 22):
	season = 'autumn'

elif (month == 'December' and day >= 21):
	season = 'winter'

print("Season is",season)
