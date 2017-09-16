def solution(n, arr1, arr2):
	answer = []
	for i in range(len(arr1)):
		arr1[i] = "{0:b}".format(arr1[i]).zfill(n)
		arr2[i] = "{0:b}".format(arr2[i]).zfill(n)
		s = ""
		for j in range(len(arr1)):
			if int(arr1[i][j]) or int(arr2[i][j]) == 1:
				s += "#"
			else:
				s += " "
		answer.append(s)
	print(answer)
	return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])