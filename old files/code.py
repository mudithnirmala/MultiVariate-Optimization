d=3 # dimension we consider
n=10 # number of seperators we input, default value

vertexList = [] # a list of tuples
seperators = [] # a list of seperators - seperators are represented by a list of coefficients ---> this is a matrix of seperator coefficients
I = []
I_list =[] # list of intersections

typedef struct{
    particular = [0]*d
    
    

} seperator;



def takeInputs():
    global seperators
    global vertexList
    
    for i = 0 to 2**d: # take all combinations of vertices, (0,0) and (4,4) ---> (0,4) and (4,0)
        thisVertex = tuple(map(int,input().strip().split()))
        vertexList.append(thisVertex)
                           
    inputVertexList()
    n = int(input().strip().split())

    for i from 1 to n:
        thisSeperator = list(map(int,input().strip().split()))
        seperators.append(thisSeperator)


def multiply(arr1,arr2):  # multiply two arrays(coefficients & points) with relevant indices 0*0 + 1*1 --> we use to subsitute points to the seperators
    thisSum=0
    for i in range(len(arr1)):
        thisSum+=arr1[i]*arr2[i]

    return thisSum


def isSeperatorPassingRegion(thisSeperator): 

    for ver1 in vertexList:
        for ver2 in vertexList:
            if(ver1==ver2): continue

            subsitute1 = thisSeperator[0] + multiply(thisSeperator[1:],vertex1)
            subsitute2 = thisSeperator[0] + multiply(thisSeperator[1:],vertex2)

            if(subsitute1*subsitute2 <0):
                return True
    return False

def isIntersectionPassingRegion(thisIntersect):
    



    
def removeUselessSeperators():
    for i in range(n):
        if(!isPassing(seperators[i])):
            remove(i)
    N= count(seperators)

def solveSeperators(seperator1,seperator2):

    # what is the form of the intersection we are going to use
    

takeInputs()
makeVertexList()
removeUselessSeperators()
                           
for k = 1 to N:
    for i = 1 to k-1:
        thisIntersect = solveSeperators(seperator[k],seperator[i])
        if(isIntersectionPassingRegion(thisIntersect)):
            I[k]+=1

print(sum(I)+N)
                           
