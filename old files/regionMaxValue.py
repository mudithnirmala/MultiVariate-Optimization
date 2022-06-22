class Region:

    def __init__(self,regoin_function,boundry):
        # assert len(regoin_function)-1 == len(boundry), "Invalid Input"
        self.regoin_function=regoin_function
        self.boundry=boundry

    def getMaxValue():
        value = 0
        point=[]

        for i in range(len(boundry)):
            if regoin_function[i]>0:
                value += regoin_function[i]*max(boundry[i])
                point.append(max(boundry[i]))
            else:
                value += regoin_function[i]*min(boundry[i])
                point.append(min(boundry[i]))

        return value,point

