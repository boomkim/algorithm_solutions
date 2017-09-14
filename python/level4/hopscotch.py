def hopscotch(board, size):
	dp = [board[0]]
	max_cur= max(dp[0])
	idx_cur= dp[0].index(max_cur)
	for i in range(1,len(board)):
		dp.append([0,0,0,0])
		for j in range(len(board[0])):
			if j != idx_cur:
				dp[i][j] = max_cur + board[i][j]
			else:
				dp[i][j] = sorted(dp[i-1])[-2] + board[i][j]
		max_cur= max(dp[i])
		idx_cur= dp[i].index(max_cur)

	return max(dp[-1])



#아래는 테스트로 출력해 보기 위한 코드입니다.
board =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
print(hopscotch(board, 3))