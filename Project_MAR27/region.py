class Region:

    def __init__(self,N):
        #declare the two attributes of the region: boundary and function
        #parameter N describes the number of dimensions
        self.boundary=[0]*N
        self.region_function=[0]*(N+1)

    def setDimBoundary(self,d,dim_boundary):
        #assign the boundary of the region: 2D list of length N(*2) describing the boundaries of each dimension by a pair of numbers
        self.boundary[d]=dim_boundary

    def setFunction(self,region_function):
        #assign the N-dimension function as a list of (N+1) coefficients, the last coefficient be the constant of the function 
        assert len(region_function)-1 == len(self.boundary), "Region function and boundary do not match"
        self.region_function=region_function

    def getMaxValue(self):
        #calculate and return the (maximum value,highest point coordinates) of the region: this should be exected after assigning function: else return 0,0 for default function
        value = 0
        point=[]

        # ALGORITHM : checking corner vertex points is sufficient, because the function is linear and the partial derivative is a constant with respect to all variables
        # maximum value for a given dimension can be found by the upper boundary(if partial derivative=coefficient >=0) or by the lower bound(if partial derivative <0) 
        for i in range(len(self.boundary)):
            if self.region_function[i]>=0:
                value += self.region_function[i]*max(self.boundary[i])
                point.append(max(self.boundary[i]))
            else:
                value += self.region_function[i]*min(self.boundary[i])
                point.append(min(self.boundary[i]))

        return value,point

    def getMidPoint(self):
        # This returns a list of all middle points for the N dimensions, simply calculating the median of boudary values
        return [sum(i)/2 for i in self.boundary]

    def getDistanceToBoundary(self):
        # This returns N dimensional list: the distance from the middle point of the region to the nearest boundary(boundary of the region) of the particular dimension
        # This is calculated by deviding the range(Upper boundary- Lower boundary) by 2
        return [(max(i)-min(i))/2 for i in self.boundary]

