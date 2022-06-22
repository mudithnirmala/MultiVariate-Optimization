import csv
import classes

N=0
mat1,mat2=[],[]
axis = [] #save intersections/breakpoints of all axes
all_regions = []

def writeCSV(file_name,matrix):

    with open(file_name, mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in matrix:
            output_writer.writerow(row)

def sohan_function(mid_point,distance_boundry):
    return [0]*(N+1)
        
def completeSearch(d,r):
    
    global all_regions
    global axis
    
    if(d==N):
        print(r.getMidPoint(),r.getDistanceToBoundry())
        r.setFunction(sohan_function(r.getMidPoint(),r.getDistanceToBoundry()))
        all_regions.append(r)
        return
    
    for i in range(axis[d].countBreakpoints()-1): # region count = intersection count-1
        r.setDimBoundry(d,[axis[d].getBreakpoint(i),axis[d].getBreakpoint(i+1)])
        completeSearch(d+1,r)


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    N = int(next(csv_reader))
    
    for row in csv_reader:

        try:
            this_breakpoint_list = list(map(int,row))
            axis.append(classes.Breakpoints(this_breakpoint_list)) # axis save all intersection points/break points of that axis

        except:
            raise ValueError("Invalid Input")
        
completeSearch(0,classes.Region(N))

