
#open system interface
import os
os.getcwd()      # Return the current working directory
#'C:\\Python311'
os.chdir('/server/accesslogs')   # Change current working directory
print(os.system('mkdir today'))   # Run the command mkdir in the system shell