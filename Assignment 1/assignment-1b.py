#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT-1 b										    #
#								STUDENT ID:											    #
#								STUDENT NAME										    #
#								DATE OF SUBMISSION:                                     #
#								UNDER GRADUATE OR POST GRADUATE                         #
#																						#
##########################################################################################

import io_module as io
import clustering as cluster
import tkinter

###Reading the Red, blue and unknown valude form the text file

data_2c_2d = "datasets/data_2c_2d.txt"
data_4c_2d = "datasets/data_4c_2d.txt"
data_2c_4d = "datasets/data_2c_4d.txt"
data_4c_4d = "datasets/data_4c_4d.txt"



read_data = io.read_multi_dim_data(data_2c_2d)

## find the Dimension and Data sample here
num_of_dimension =  ##add your code here

sample_size =  ## add your code here


###Any number greater than 1
cluster_size = int(input("Input the cluster size:"))

##Create a random cluster center based on number of dimension(num_of_dimension) and size of cluster(select_cluster_size)
cluster_center = cluster.generate_K_cluster_centres(num_of_dimension, cluster_size)
##create list based on the cluster center




## threshold to a small value
threshold = 0  ##change the value of 0

####K mean algorithm
### Find the best cluster center here




#### Plot the data points and the cluster centers


top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=700, width=700)

###plot here using the week 3,4 ,5 and 6 code.

C.pack()
top.mainloop()
