#import glob, os
import os

#Attach files

#os walk 


#1. file attribute flip slashes the other way Succesful for one directory change. Consider version and loop  **This works
#filename = 'C:/Users/Owner/Documents/Test1all/Doc1.txt'
#newfilename = 'C:/Users/Owner/Documents/Test1all/Rename1.txt'
#os.rename(filename, newfilename)

#rename folder location   loop make file 
infile=open(r''C:/Users/Owner/Documents/Test1all/Doc1.txt','r'')
while(line);
    print(line)
    line = inFile.Readline()
#2  find a way to create a list of all of the file locations in the folder


#slice
#os.rename(r'C:\Users\Owner\Documents\Test1all\OLD file name.file type',r'C:\Users\Owner\Documents\NewTest1')
#def rename(dir, pattern, titlePattern):
    #for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
     #   title, ext = os.path.splitext(os.path.basename(pathAndFilename))
      #  os.rename(pathAndFilename, 
       #           os.path.join(dir, titlePattern % title + ext))
        #          rename(r'c:\temp\xx', r'*.doc', r'new(%s)')