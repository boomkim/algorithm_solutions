def sums(a,b):
    return (a+b)*(b-a+1)/2

def expressions(num):
    answer = 1
    center = num // 2 
    for i in range(1,center+1):
        for j in range(i+1,center+2):
            if sums(i,j) == num: 
                answer += 1 
                print("i: ",i, "j: ", j)
            
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
