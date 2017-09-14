def gcdlcm(a, b):
    c, d = a, b
    mod = a % b 
    while(mod>0):
        c = d
        d = mod
        mod = c % d
    gcd = d 
    return [gcd,a*b//gcd]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))