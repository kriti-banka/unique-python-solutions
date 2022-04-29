c=0
def hanoi(n,source,aux,target):
    global c
    c=c+1
    if n==1:
        print("move disc 1 from source",source,"to target",target)
        return
    
    hanoi(n-1,source,target,aux)
    print("move disc",n,"from source",source,"to target",target)
    hanoi(n-1,aux,source,target)
   
    

n = int(input("enter number of disc"))
hanoi(n, 'A', 'C', 'B')
# A, B, C are the rod
print ("Sorted array is:")
for i in range(n):
    print (i,end=" ")
print("\n")
print("minimum number of moves are:", c)
