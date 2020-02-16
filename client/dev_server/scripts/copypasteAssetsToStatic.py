# Python program to explain shutil.copytree() method  
       
# importing os module  
import os  
   
# importing shutil module  
import shutil  
   
   
# Source path  
src = '../public/static/assets/'
   
# Destination path  
dest = '../../../server/static/assets/'
   
# Copy the content of  
# source to destination  

shutil.rmtree(dest)

destination = shutil.copytree(src, dest)  
