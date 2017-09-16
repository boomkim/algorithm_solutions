import datetime

def solution(cacheSize, cities):
	answer = 0
	cache = []
	for city in cities:
		if len(cache) == 0:
			cache.append([city.lower(),datetime.datetime.now()])
			answer += 5
		elif city.lower() in [i[0] for i in cache]:
			answer += 1 
			cache[[i[0] for i in cache].index(city.lower())][1] = datetime.datetime.now()
		else: 
			if len(cache)<cacheSize:
				cache.append([city.lower(),datetime.datetime.now()])
				answer += 5
			else:
				cache[[i[1] for i in cache].index(min([i[1] for i in cache]))] = [city.lower(),datetime.datetime.now()]
				answer += 5 

	return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))