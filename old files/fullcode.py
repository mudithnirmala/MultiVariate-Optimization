N=int(input().strip()) # number of dimensions

all_regions=[]
dimensions = [] # save breakpoints/intersections of all dimensions

class Dimension:
    def __init__(self,intersection_list):
        self.intersection_list=sorted(intersection_list)

    def countIntersections(self):
        return len(self.intersection_list)
    def intersection(self,i):
        return self.intersection_list[i]
    
class Region:

    def __init__(self): 
        self.boundry=[0]*(N)

    def setDimBoundry(self,d,dim_boundry):
        self.boundry[d]=dim_boundry

    def setFunction(self,regoin_function):
        assert len(regoin_function)-1 == len(self.boundry), "Region function and boundry do not match"
        self.regoin_function=regoin_function

    def getMaxValue(self):
        value = 0
        point=[]

        for i in range(len(self.boundry)):
            if self.regoin_function[i]>0:
                value += self.regoin_function[i]*max(self.boundry[i])
                point.append(max(self.boundry[i]))
            else:
                value += self.regoin_function[i]*min(self.boundry[i])
                point.append(min(self.boundry[i]))

        return value,point

    def getMidPoint(self):
        return [sum(i)/2 for i in self.boundry]

    def getDistanceToBoundry(self):
        return [(max(i)-min(i))/2 for i in self.boundry]

def sohan_function(mid_point,distance_boundry):
    return [0]*(N+1)
        

def completeSearch(d,r):
    
    global all_regions
    global dimensions
    
    if(d==N):
        print(r.getMidPoint(),r.getDistanceToBoundry())
        r.setFunction(sohan_function(r.getMidPoint(),r.getDistanceToBoundry()))
        all_regions.append(r)
        return
    
    for i in range(dimensions[d].countIntersections()-1): # region count = intersection count-1
        r.setDimBoundry(d,[dimensions[d].intersection(i),dimensions[d].intersection(i+1)])
        completeSearch(d+1,r)


for d in range(N):
    intersection_list = list(map(int,input().strip().split())) # 0 and maxm of range <-- input as an intersection   continuos dimensions-> only 0 maximum(range)
    dimensions.append(Dimension(intersection_list))

completeSearch(0,Region())
