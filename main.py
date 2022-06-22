import csv
import region

N=0
axis_breakpoints = [] # 2D list save intersections/breakpoints of all axes : first index= dimension/axis , second index= breakpoint index
all_regions = []

def writeCSV(file_name,matrix):
    #write a 2 dimensional list to a csv file

    with open(file_name, mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in matrix:
            output_writer.writerow(row)

def sohan_function(mid_point,distance_boundry):
    return [1]*(N+1)
        
def completeSearch(d,r):
    # reccursively generate all possible region. d- current dimension  r- Region class object
    
    global all_regions
    global axis_breakpoints
    global N

    #termination condition: If all the N dimensions have been looped then terminate
    #this will not affect the time complexity(N~700) because most of the dimensions are continuos and they have one option
    if(d==N):
        print(r.getMidPoint(),r.getDistanceToBoundary())
        #request the coefficients of the function as a list of N+1 length: last element be the constant
        r.setFunction(sohan_function(r.getMidPoint(),r.getDistanceToBoundary()))
        print(r.getMaxValue())
        all_regions.append(r)
        return
    
    for i in range(len(axis_breakpoints[d])-1): # region count = intersection count-1
        #loop through every possible interval of the dth dimension/axis 
        r.setDimBoundary(d,[axis_breakpoints[d][i],axis_breakpoints[d][i+1]])
        completeSearch(d+1,r)


with open('test_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    N = int(next(csv_reader)[0]) # Number of dimensions, we only take the first element of the list(N,commas)

    for row in csv_reader:
        while '' in row: # remove the null elements inserted as a result of additional commas in csv file
            row.remove('')
        try:
            this_bp_list = list(map(int,row)) # intersection points(breakpoints) of the particular(row)s dimension
            axis_breakpoints.append(this_bp_list) # axis save all intersection points/break points of that axis

        except:
            raise ValueError("Invalid Input")
       
completeSearch(0,region.Region(N))

