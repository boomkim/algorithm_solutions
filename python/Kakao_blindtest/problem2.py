def solution(dartResult):
    temp = 0
    sums = 0
    arr = []
    t = ''
    for c in dartResult:
        if c.isdigit():
            t += c
        else:
            arr.append(t)
            t = ''
            arr.append(c)
    print(arr)
    nums =[]
    for c in arr:
        if c.isdigit():
            sums += temp
            temp = int(c)
        elif c == 'S':
            temp = temp
            nums.append(temp)
        elif c == 'D':
            temp = temp*temp
            nums.append(temp)
        elif c == 'T':
            temp = temp*temp*temp
            nums.append(temp)
        elif c == '*':
            temp = temp*2
            nums[-1] = nums[-1]*2
            if len(nums)>1:
                sums += nums[-2] + temp
            else:
                sums += temp
            temp = 0
        elif c == '#':
            temp = temp * -1
            nums[-1] = temp
    answer = sums + temp 
    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1D#2S*3S'))
print(solution('1D2S3T*'))