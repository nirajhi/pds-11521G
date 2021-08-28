#Function to read 2D data from file and save data to a list of tuples
def read_data_file(filename):
    dataset = []
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:#end of file
                break
            line = line.replace('\n', '') #remove end of line \n character 
            xystring = line.split(' ') #x y coordinates in string format
    	            #use split function to separate x & y strings then
        	#use float function to convert x & y strings to x & y numbers and #add them as a tuple (x, y) to dataset that is a list 
            dataset.append((float(xystring[0]), float(xystring[1])))
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset
#end of function


def calculate_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])**2
    return distance**0.5




def find_neared_neighbour(unknown_sample, data_list):
      min_distance = 100.0
      nearest_point = unknown_sample
      for sample in data_list:
          distance = calculate_distance(unknown_sample, sample)
          if  distance < min_distance:
              min_distance = distance
              nearest_point = sample
      return nearest_point        
  
  
    	