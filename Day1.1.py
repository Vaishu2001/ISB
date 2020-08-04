'''#create a file 

#open a file
#give name+extension
#click enter
#fo=open("C:\\Users\\ASUS\\test.txt",'a')
#fo.write("Hello all.Welcome to ISB.")
#In order to write multiple lines then create a list of lines
#line_list=["It is really hot in Kolkata\n""BTW how is your preparation of ISB going?\n","Are you attending warm up session?\n"]
#fo.writelines(line_list )

#one file has data for starting 15 days of a month
#other file has data for next 15 days of a month
#you want to update the data in the other file

#open the first file in append mode
ff=open("C:\\Users\\ASUS\\example.txt",'a')
#open the second file in read mode
sf=open("C:\\Users\\ASUS\\test.txt",'r')
#read data from second file 
info=sf.read()
#append the info read data in the first file
ff.write(info)
#close the files
ff.close()
sf.close()'''
# moving a file
#change the locations of the file
#new directory formation ->os.mkdir("new_directory_path")
import os
import shutil

#os.mkdir("C:\\Users\\ASUS\\alien brain\\Mani")
#shutil.move("C:\\Users\\ASUS\\ABC","C:\\Users\\ASUS\\alien brain\\Mani\\ABC")
#In order to copy a file
#shutil.copy("C:\\Users\\ASUS\\output_1.txt","C:\\Users\\ASUS\\alien brain\\Mani\\output_1.txt ")
#copy the multiple files
#for every file in the forloop,copy it
'''file_list=["C:\\Users\\ASUS\\output3_1.txt","C:\\Users\\ASUS\\output3_2.txt","C:\\Users\\ASUS\\output3_3.txt"]
for file in file_list:
	shutil.copy(file,"C:\\Users\\ASUS\\alien brain\\Mani\\")'''
#rename the file
#os.rename("C:\\Users\\ASUS\\output_2.txt"," C:\\Users\\ASUS\\result_2.txt")
#_____sem_res.txt->semester result.txt
#C:\\Users\\ASUS\\1st sem_res.txt->C:\\Users\\ASUS\\1st semester result.txt
'''re_files=["C:\\Users\\ASUS\\1st sem_res.txt","C:\\Users\\ASUS\\2nd sem_res.txt","C:\\Users\\ASUS\\3rd sem_res.txt"]
for i in re_files:
	j=i.split(" ")
	#print(j)
	new_path=j[0]+"semester result.txt"
	#print(new_path)
	os.rename(i,new_path)'''
#os.remove("C:\\Users\\ASUS\\alien brain\\Mani\\test.txt") 
os.remove("C:\\Users\\ASUS\\alien brain\\Mani\\output_1.txt")




