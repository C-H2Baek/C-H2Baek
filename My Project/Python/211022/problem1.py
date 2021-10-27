

myList = input("Choose Number : split , )").split(',')
#myList = [55,9,5,3,2,4,3,4,4,]
count=0

#print(type(myList))

while True:
    
    print(myList)
    num = input("Search Number")
    
    for i in range(len(myList)):
        if myList[i] == num:
            print("%s is %d Location." % (num,i+1))
            break
        count+=17
    if count == len(myList):
        print("nothing number in list.")
    count = 0

