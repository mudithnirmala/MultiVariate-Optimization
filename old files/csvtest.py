import csv
import region

mat1,mat2=[],[]

def writeCSV(file_name,matrix):

    with open(file_name, mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in matrix:
            output_writer.writerow(row)

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    n,d = list(map(int,next(csv_reader)))
    
    for row in csv_reader:

        try:
            func,boundry = list(map(int,row[:n+1])),list(map(int,row[n+1:]))
            boundry = [[boundry[i],boundry[i+1]] for i in range(0,len(boundry),2)]

        except:
            raise ValueError("Invalid Input")
        
        r= region.Region(func,boundry)
        print(r.getMaxValue())
        print(r.getMidPoint())
        mat1.append(r.getMidPoint())
        print(r.getDistanceToBoundry())
        mat2.append(r.getDistanceToBoundry())

writeCSV("mat1.csv",mat1)
writeCSV("mat2.csv",mat2)

