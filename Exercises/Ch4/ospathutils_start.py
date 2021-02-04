#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  #print(os.name)
  
  # Check for item existence and type
  #print("Item exusts: " +str(path.exists("testfile.txt")))
  #print("Item is a file :" +str(path.isfile("testfile.txt")))
  #print("Item is a directory :" +str(path.isdir("testfile.txt")))
  
  # Work with file paths
  #print("Item path :" + str(path.realpath("testfile.txt")))
  #print("Item path and name :" + str(path.split(path.realpath("testfile.txt"))))

  print("**********************************")
  # Get the modification time
  #t = time.ctime(path.getmtime("testfile.txt")) #ctime classe to convert the modification time to real time & getmtime() function gives the modification time of the file.
  #t = time.ctime(path.getmtime("testfile.txt")) 
  #print(t)
  #print(datetime.datetime.fromtimestamp(path.getmtime("testfile.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("testfile.txt"))
  print("It has been " +str(td) + " since the file was modified ")
  print("Or, " + str(td.total_seconds()) + "seconds")
                                                                
  
  
if __name__ == "__main__":
  main()
