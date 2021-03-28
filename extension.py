import os 
  
name=input("Input the filename:")


ext= os.name.splitext(name) 
  
print("The extension of the file is '%s':"%name,ext[1])

#print("root part of '% s':" % path, root_ext[0]) 
#print("ext part of '% s':" % path, root_ext[1], "\n") 
  
