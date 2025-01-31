with open(f'C:\\Users\\Jaimin\\OneDrive\\Desktop\\jarvis\\Jarvis_copy.py','r') as mainfile:
    content = mainfile.read()
    
with open(f'C:\\Users\\Jaimin\\OneDrive\\Desktop\\jarvis\\JarvisCopy.py','w') as contentfile:
    contentfile.write(content)
    
print("Content copied!!")