def getMinSum(A,B):
    A.sort()
    B.reverse()
    sum=0
    for i in range(len(A)):
        sum = sum+ A[i]*B[i]

    return sum

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))