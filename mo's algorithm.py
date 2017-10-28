## mo's algorithm
from math import sqrt
##array
array=[2, 3, 1, 4, 2]##[1,2,3,4,5,6,7,8,9]
query=[[0, 4, 7, 2], [1, 4, 2, 1], [0, 4, 2, 0]]##[[1,9],[2,1],[3,1],[7,1],[4,1]]
##defining the block size sqrt(n)
block=int(sqrt(len(array)))
##comparision function
def compare(a,b):
    if(a[0]/block!=b[0]/block):
        return int(a[0]/block>b[0]/block)-1
    else:
        return int(a[1]>b[1])-1
##sorting the query array on the basis of the function
query.sort(compare)
'''
 solve the problem as normal
'''

## sample question
'''
    to find number of a particular number in a range
'''

store=[0]*101
ans=[0]*q
l,r=0,-1
for i in range(q):
    while(l < query[i][0]):
        store[array[l]]-=1
        l+=1
    while(l > query[i][0]):
        l-=1
        store[array[l]]+=1
    while(r < query[i][1]):
        r+=1
        store[array[r]]+=1
    while(r > query[i][1]):
        store[array[r]]-=1
        r-=1
    ans[query[i][3]]=store[query[i][2]]
for i in range(q):
    stdout.write(str(ans[i])+"\n")

