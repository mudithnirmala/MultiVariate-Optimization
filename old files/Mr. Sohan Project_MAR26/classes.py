class BreakpointManager:
    def __init__(self,breakpoint_list):
        self.breakpoint_list=sorted(breakpoint_list)

    def countBreakpoints(self):
        return len(self.breakpoint_list)
    def getBreakpoint(self,i):
        return self.breakpoint_list[i]
    
class Region:

    def __init__(self,N): 
        self.boundry=[0]*(N)
        self.regoin_function=[0]*(N+1)

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

