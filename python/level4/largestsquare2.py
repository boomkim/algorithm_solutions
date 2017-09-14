def solution(board):
	answer = []
	for i in range(len(board)):
		for j in range(len(board[0])):
			count = 0
			for a in range(j,len(board[0])):
				if board[i][a] == 0:
					break
				count += 1
				count = min(count,(len(board)-i))
			cond = True
			for k in range(i+1,i+count):
				for l in range(j,j+count):
					if board[k][j] == 0:
						cond = False
			if cond:
				answer.append(count*count)

	return max(answer)

test1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
test2 = [[0,0,1,1],[1,1,1,1]]
print(solution(test1))
print(solution(test2))
