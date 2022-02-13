'''Starting module'''
from WaterManager import WaterManager
import sys

def main():
    '''Main method'''
    #get filename from first command ine argument
    input_file = sys.argv[1]
    #create instance of WaterManager class
    manager=WaterManager()
    #open file in read mode
    file=open(input_file,"r")
    #read all lines in file
    lines=file.readlines()
    #for each line in file
    for line in lines:
        #get  rid of trailing whitespaces create list of words
        words=line.strip().split()
        #if first word  is ALLOT_WATER
        if words[0]=="ALLOT_WATER" :
            #extract flates
            flat=int(words[1])
            #extract corporation and borewell ratio
            a,b=map(int,words[2].split(":"))
            #call allot_water with extracted methods
            manager.allot_water(flat,a,b)
        #if first word is Add_GUESTS
        elif words[0]=="ADD_GUESTS" :
            guests=int(words[1])
            #add guests
            manager.add_guest(guests)
        #if first word is BILL
        elif words[0]=="BILL" :
            #get bill
            manager.get_bill()

#program execution starts from here
if __name__ == "__main__":
    main()