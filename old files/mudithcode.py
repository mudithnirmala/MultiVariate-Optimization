N = int(input().strip())  # total number of independent variables
ranges = list(map(int,input().strip().split())) # all ranges start with 0 so we only add highest value of the range
D= int(input().strip()) # total number of discontinuous variables

hyperplane_count = list(map(int,input().strip().split())) # number of hyperplanes of all D dimensions(intersection points with D axes)
planeaxis_intersections =[] # Dimension * list of intersections of that dimension

region_function = [] # 2D list for each region --> list of coefficients
region_coord = [] # coordinate of the relevant region (First region along x1 , second region along x2,.. )

region_boundary = [] #2D list--> R*D [region_index][dimension] --> [upperBoundary, lowerBoundary]
region_max = [] # maximum value of the function in the region
region_max_coord = [] # coordinate at the maximum value of the region


for thisDimCount in hyperplane_count: #Dim -> dimension
    thisDimIntersections = list(map(int,input().strip().split()))
    # intersection points of the hyperplanes with this Dimension axis
    planeaxis_intersections.append(thisDimIntersections)
    # they should give 0 and Highest value in range as hyperplanes

R = int(input().strip()) # we can simply calculate this by multiply hyperplane_count


for i in range(R):
    # first line coordinate of the REGION
    coord = list(map(int,input().strip().split()))
    region_coord.append(coord)
    func = list(map(int,input().strip().split()))
    region_function.append(func)

def assign_boundaries():
    global region_coord

    for r in range(R):
        thisBoundary = [] # a 2D list [dimension][0/1 -- lower/upper]
        for d in range(D):
            thisCord = region_coord[r][d]
            thisBoundary.append([planeaxis_intersections[d][thisCord],planeaxis_intersections[d][thisCord+1] ])
            
        region_boundary.append(thisBoundary)       

    #print(region_boundary)

def getFunctionValue(coord,this_func):
    print(this_func)
    eqnSum=this_func[-1]  # last one of the function is constant
    for i in range(N): #length is N  
        eqnSum+= coord[i]*this_func[i]
    
    return eqnSum
def findHighestPoint(r): # input region --> output the highes point+ value

    global region_boundary
    global region_function
    
    dimension_boundary = region_boundary[r]
    this_func = region_function[r]
    for i in range(D,N):
        dimension_boundary.append([0,ranges[i]]) # for continuous dimensions boundary is range

    # now let's go to the function
    #if function has positive coefficients we take upper boundary, otherwise lower boundar( partial derivative is coefficient)

    highestVal =0
    pointCoord =[]
    for i in range(N):
        thisCoordValue = dimension_boundary[i][0 if this_func[i]<0  else 1]
        pointCoord.append(thisCoordValue)

    highestVal = getFunctionValue(pointCoord,this_func)

    return highestVal,pointCoord
    
assign_boundaries()

highestVal=0
allHighestPoint =[]

for r in range(R):
    thisVal,thisPoint = findHighestPoint(r)
    
    if(thisVal>highestVal):
        highestVal= thisVal
        allHighestPoint= thisPoint

    print("region",r,"highestValue",thisVal,"coordinate",thisPoint)

print("Total of all regions")

print("highestValue",highestVal,"coordinate",allHighestPoint)
