def expressions(num):
    answer = 0
    for i in range(1,num+1):
        if num%i == 0 and i%2 == 1 : answer += 1
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
