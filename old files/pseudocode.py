input d
vertexList = []
I = []

struct seperator{
    int coeff[d+1]
}
struct intersecton{
    int coeff[d]
}
struct vertex{
    int cord[d]
}

def takeInputs():
    input vertex1
    input vertex2
    input n

    seperator seperators[]

    for i from 1 to n:
        input thisSeperator
        seperators[i] = thisSeperator


def multiply(arr1,arr2):
    thisSum=0
    for i in range(arr1):
        thisSum+=arr1[i]*arr2[i]

    return thisSum

def makeVertexList():
    
    for i = 0 to 2**d: # take all combinations of vertices, (0,0) and (4,4) ---> (0,4) and (4,0)
        vertex thisVertex[]
        boolString = str(bool(i))
        boolString = '0' *(d-len(boolString)+ boolString

        for j in range(d):
            thisVertex.cord[j] = boolString[j]=='0'? vertex1[j]:vertex2[j]

        vertexList.append(thisVertex)


def isPassingRegion(thisSeperator): # I think this same function works for intersections as well-> think more

    for ver1 in vertexList:
        for ver1 in vertexList:
            if(ver1==ver2): continue

            subsitute1 = multiply(thisSeperator,vertex1)
            subsitute2 = multiply(thisSeperator,vertex2)

            if(subsitute1*subsitute2 <0):
                return True
    return False

def removeUselessSeperators():
    for i in range(n):
        if(!isPassing(seperators[i])):
            remove(i)
    N= count(seperators)    

takeInputs()
makeVertexList()
removeUselessSeperators()
                           
for k = 1 to N:
    for i = 1 to k-1:
        thisIntersect = solve(seperator[k],seperator[i])
        if(isPassingRegion(thisIntersect)):
            I[k]+=1

print(sum(I)+N)
                           
