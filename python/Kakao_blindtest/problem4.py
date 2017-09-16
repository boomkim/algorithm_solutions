import datetime

def solution(n, t, m, timetable):
	for i in range(len(timetable)):
		timetable[i] = datetime.datetime.strptime(timetable[i],'%H:%M')
	timetable.sort()

	bus = datetime.datetime.strptime('09:00','%H:%M')
	lastman = datetime.datetime.strptime('00:00','%H:%M')
	#버스가 와서 사람들을 태운다.
	for i in range(n):
		bus += datetime.timedelta(minutes=i*t)
		for j in range(m):
			if len(timetable)>0:
				if timetable[0]<=bus:
					if i == n-1 and j == m-1:
						return (timetable[0] - datetime.timedelta(minutes=1)).strftime('%H:%M') 
					else:
						lastman = timetable[0]
						timetable.remove(timetable[0])

	return bus.strftime('%H:%M') 


print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2,["09:10", "09:09", "08:00"]))
print(solution(2,10,2,["23:59"]))