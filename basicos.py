import os
from os import path

# Windows path
windowsPath = "C:\Intel"
wrongPath = "C:\DoesntExists"

isValidPath = path.exists(windowsPath)
isInvalidPath = path.exists(wrongPath)

print (windowsPath + " exists? : " + str(isValidPath))

if isValidPath :
	someFile = windowsPath + "\Logs\IntelAMT.log"
	print ("And the size of " + someFile + "is : " + str(path.getsize(someFile))) # 40.04 KB

print (wrongPath + " exists? : " + str(isInvalidPath))

#building paths
newPath = path.join("C:", "Documents", "Pictures")
print (newPath)