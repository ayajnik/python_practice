try:
    import csv 
    import os
    import sys
    print('\n')
    print('Libraries Imported')
    print('\n')
except:
    print('\n')
    print('Libraries not installed')
    print('\n')

##importing the dataset
with open("H_Clinton-emails.csv", "r") as file:
    file_reader = csv.DictReader(file)    ##with this command we have created an object of the file
    print('\n')
    print("File uploaded")
    print("\n")

##printing the header of the file
    print('The variables that we are delaing in this dataset are:')
    i = file_reader.fieldnames
    #print(i)
    print('\n')
    print('These were the variables in the datasets')
    print('\n')

## looking at the datatype of the columns
    print("The data type used in this file are:")
    for a,b in enumerate(i):
        print(a, '----->'+b, '----->', type(b))
        #print('\n')
        #print(type(a))

    for w in file_reader:
        print(w[0])       

    