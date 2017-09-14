def lcm(a,b):
    mul = a * b
    mod = a % b
    while(mod>0):
        a = b
        b = mod
        mod = a % b
    return mul//b
    
def nlcm(num):
    lcms = [num[0]]
    answer = 0
    for i in range(len(num)-1):
        lcms.append(lcm(lcms[i],num[i+1]))
    print(lcms)
    return lcms[-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));