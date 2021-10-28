# a = map(int, input("Input").split())

# print(a)
# print(list(a))

def sel_sort(a):
    n = len(a)
    for i in range(0, n-1): # 0부터 n-2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 찾은 최솟값을 i번 위치로.
        a[i],a[min_idx] = a[min_idx],a[i]

d = map(int, input("Input").split())
sel_sort(d)
print(d)


# def sel_sort(a):
#     n = len(a)  # 리스트 a의 길이만큼 반복

#     for i in range(0, n-1): #0부터 n-2까지
#         # i번 위치부터 끝까지 자료 값 중 최소값의 위치를 찾음
#         min_idx = i         
#         for j in range(i+1, n):
#             #print("%d와 %d의비교" % (min_idx,j))
#             if a[j] < a[min_idx]:               # 리스트 최소값 인텍스번째와 i번째 값 비교
#                 min_idx = j                     # i번째가 최소값 인덱스번째 보다 적을 경우 i인덱스를 최소값 인덱스로 지정
#         #찾은 최소값을 i번 위치. i번쨰 값을 최소값 위치로 동시 교환
#         #파이썬에서 두 자료 값 서로 바꾸기
#         a[i],a[min_idx] = a[min_idx],a[i]
#         #print("min_idx", min_idx)
#         #print("a",a)

# #Searchlist = input("Choose Number , )").split(',')

# #Searchlist = map(int,input("Choose Number , )").split(','))

# Searchlist = [9,6,3,5,2] 
# print("정렬 전" , Searchlist)
# sel_sort(Searchlist)
# print("정렬 후" ,Searchlist)