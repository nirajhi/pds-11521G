#########################################################################################
#																						#
# 								PROGRAMMING IN DATA SCIENCE		                        #
#								ASSIGNMENT-1 a									    #
#								STUDENT ID:											    #
#								STUDENT NAME										    #
#								DATE OF SUBMISSION:                                     #
#								UNDER GRADUATE OR POST GRADUATE                         #
#																						#
##########################################################################################

### Importing read file and utilty method ##
import io_module as io
import utility as util


### Defining the dataset.
### *_2d.txt has 2 coordinate
### *_3d.txt has 3 coordinate
### *_4d.txt has 4 coordinate

red_data =  ["datasets/red_2d.txt","datasets/red_4d.txt","datasets/red_6d.txt"]
blue_data =  ["datasets/blue_2d.txt","datasets/blue_4d.txt","datasets/blue_6d.txt"]
unknown_data =  ["datasets/unknown_2d.txt","datasets/unknown_4d.txt","datasets/unknown_6d.txt"]

red_dataset = None
blue_dataset = None
unknown_dataset = None


###Reading the dataset
while True:
	try:
		select_dimension = int(input("Select the Dimension for the Red and blue dataset (2,4,8):"))
		if select_dimension == 2:
			red_dataset = io.read_multi_dim_data(red_data[0])
			blue_dataset = io.read_multi_dim_data(blue_data[0])
			unknown_dataset = io.read_multi_dim_data(unknown_data[0])
			break


		elif select_dimension == 4:
			red_dataset = io.read_multi_dim_data(red_data[1])
			blue_dataset = io.read_multi_dim_data(blue_data[1])
			unknown_dataset = io.read_multi_dim_data(unknown_data[1])
			break

		elif select_dimension == 8:
			red_dataset = io.read_multi_dim_data(red_data[2])
			blue_dataset = io.read_multi_dim_data(blue_data[2])
			unknown_dataset = io.read_multi_dim_data(unknown_data[2])
			break

		else:
			raise ValueError

	except ValueError:
		print("Please enter a valid number")




### Write a code to find whether the unknow_point is red or blue



# The output is in output folder