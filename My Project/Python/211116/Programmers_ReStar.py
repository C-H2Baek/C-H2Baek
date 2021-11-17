def solution(x, n):
    answer = []
    for i in range (1,n+1):
        answer.append(x*i)
    return answer

x= int(input("Start Number"))
n= int(input("Multiple Number"))
print(solution(x,n))