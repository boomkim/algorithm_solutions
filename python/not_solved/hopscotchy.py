def hopscotch(board, size):
	board2 = []
	for e in board:
		e = list(map(lambda x: [x,sorted(e).index(x)],e))
		board2.append(e)
	print(board2)
	for i in range(len(board2)):
		for j in range(len(board2[0])):
			print(board2[i][j][0])
	return 0 



#아래는 테스트로 출력해 보기 위한 코드입니다.
board =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
print(hopscotch(board, 3))