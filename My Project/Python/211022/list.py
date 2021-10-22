'''
myList=[30,10,20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)

print("pop() 으로 추출한 값 : %s" %myList.pop())
print("pop() 후의 리스트 : %s" % myList)

myList.sort()
print("sort() 후의 리스트 : %s" % myList)

myList.reverse()
print("reverse() 후의 리스트 : %s" % myList)

print("20 값의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" % myList)

myList.extend( [77, 88, 77] )
print("extend([77, 88, 77]) 후의 리스트 : %s" % myList)

print("77 값의 개수 : %d" % myList.count(77))
'''
'''
aa=[]
bb=[]
value=0

for i in range(0,10) :
    aa.append(value)
    value+=2
    print(aa)

for i in range(0,10) :
    bb.append(aa[9-i])
    print(bb)
print("bb[0]은 %d, bb[9]는 %d 입력됨 " % (bb[0], bb[9]))
'''

'''    
for i in range(10) : # 1차원 배열
    list1.append(i)
    print(list1)
'''
'''
#2차원 배열
list1=[]
list2=[]
value=1

for i in range(0,3) :
    for k in range(0,4) :
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]

for i in range(0,3) :
    for k in range(0,4) :
        print("%3d" % list2[i][k], end="")
    print("")
'''
'''
#2차원 배열 #2
list1=[] # 내부배열
list2=[] # 외부 배열
value=0  # 배열의 값을 위한 변수,초기화 되지 않고 증가하는 변수
for i in range(0,5) :       # 외부 배열을 위한 반복
    for k in range(0,4) :   # 내부 배열을 위한 반복
        list1.append(value) # 빈 리스트에 value 값을 추가
        value+=2            # value의 증가
        print(list1)        # 내부 배열에 외부 배열을 추가
    list2.append(list1)
    list1=[] # 내부배열을 초기화
print(list2)

for i in range(0,3) :
    for k in range(0,4) :
        print("%3d" % list2[i][k], end="")
    print("")

'''



