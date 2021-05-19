
import os 
location = r'C:\Users\Owner\SAVVY\Test1' # location equals the path 
print(location)
i= 0 #i-0 to irrate the code . How many times for example one by one 
for filename in os.scandir(location):
       print(filename.path)
       # Second for multiple extensions doc. text. etc 
       break_up = os.path.splitext(filename.path)
       file_name = break_up[0]
       file_ext = break_up[1]
       new_name = file_name + "new" + str(i) + file_ext
       os.rename(filename, new_name)
       i += 1
       # The code below only extracts txt and you would need to manually change the extension
     #  rename = "updated" + str(i) + ".txt" # updated is the date  add file extension
      # rename = location +"\\"+ rename 
       #print("renamed file",rename)
       #os.rename(filename.path, rename)
       #i += 1 #  Total culmulation function can tell the 


