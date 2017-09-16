import re 

def solution(str1, str2):
	p = re.compile('[a-zA-Z]{2}')
	arr1 =[]
	arr2 = []
	while str1 != '':
		if p.match(str1[0:2]):
			arr1.append(str1[0:2].lower())
		str1 = str1[1:]
	while str2 != '':
		if p.match(str2[0:2]):
			arr2.append(str2[0:2].lower())
		str2 = str2[1:]
	print (arr1,arr2)

	if len(arr1) == 0 and len(arr2) ==0:
		return 65536
	
	kyo = 0
	hap = 0
	for a in arr1:
		if a in arr2:
			kyo += 1
			arr2.remove(a)
		hap += 1
	hap += len(arr2)
	answer = kyo / hap * 65536
	return int(answer)

print(solution('FRANCE','french'))
print(solution('E=M*C^2','e=m*c^2'))