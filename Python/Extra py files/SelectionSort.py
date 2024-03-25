def minIndex (a , x , y):
    if x == y:
        return x
    z = minIndex(a,x+1,y)
    return (x if a[x] < a[z] else z)

def RSS (a, n, index = 0):
    if index == n:
        return -1
    z = minIndex(a , index , n-1)
    else:
        if z != index:
            a[z], a[index] = a[index], a[z]
        RSS(a, n, index + 1)
        
#If you pass a value to array inside a function the changes are visible outside the function but if you pass a value from outside the function to the function and change it the changes will not be visible to outside the function        
        

l1 = [5, 7, 2, 4, 6]
n = len(l1)
RSS(l1, n)
for x in l1:
    print(x , end = ' ')