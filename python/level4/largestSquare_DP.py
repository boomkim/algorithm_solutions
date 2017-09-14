def findLargestSquare(board):
    answer = 0
    dp = []
    for i in range(len(board)):
    	row = []
    	for j in range(len(board[0])):
    		if i == 0 or j == 0:
    			row.append(0)
    		elif board[i][j] == 'O':
    			row.append(min(dp[i-1][j-1],dp[i-1][j],row[j-1])+1)
    		elif board[i][j] == 'X':
    			row.append(0)
    		if row[j]>answer: answer = row[j]
    	dp.append(row)

    return answer*answer

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))