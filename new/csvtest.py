import csv
import region
import Sohan


mat1,mat2=[],[]
class RegionHelper:

    def writeCSV(file_name,matrix):

        with open(file_name, mode='w') as output_file:
            output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for row in matrix:
                output_writer.writerow(row)

    def readCSV(file_name):


        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            inputs=[list(map(int,row)) for row in csv_reader]

        return inputs

    def generateRegions(regionList,dimention_matrix,current_dim=0,dimention_list=[]):
        # print(dimention_list)
        if len(dimention_matrix)==current_dim:
            regionList.append(region.Region(dimention_list))
            return
        
        for i in range(len(dimention_matrix[current_dim])-1):
            RegionHelper.generateRegions(regionList,dimention_matrix,current_dim+1,dimention_list+[[dimention_matrix[current_dim][i], dimention_matrix[current_dim][i+1]]])

    def getMaxValue(file_name):

        input_matrix= RegionHelper.readCSV(file_name)
        print(input_matrix)

        N=int(input_matrix[0][0])
        dimention_matrix=input_matrix[1:]

        regionList=[]

        RegionHelper.generateRegions(regionList,dimention_matrix)

        for regionObject in regionList:
            regionObject.setFunction(Sohan.sohan_function(regionObject.getMidPoint(),regionObject.getDistanceToBoundary()))

        
        for regionObject in regionList:
            regionObject.getMaxValue()


        
RegionHelper.getMaxValue('data.csv')

# print()
# for item in regionList:
#     # pass
#     print(item.getBoundary())


#         try:
#             func,boundry = list(map(int,row[:n+1])),list(map(int,row[n+1:]))
#             boundry = [[boundry[i],boundry[i+1]] for i in range(0,len(boundry),2)]

#         except:
#             raise ValueError("Invalid Input")
        
#         r= region.Region(func,boundry)
#         print(r.getMaxValue())
#         print(r.getMidPoint())
#         mat1.append(r.getMidPoint())
#         print(r.getDistanceToBoundry())
#         mat2.append(r.getDistanceToBoundry())

# writeCSV("mat1.csv",mat1)
# writeCSV("mat2.csv",mat2)

