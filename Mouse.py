import win32api
import time
input()
location = (win32api.GetCursorPos())
time.sleep(3)
location2 = (win32api.GetCursorPos())
print("du bist an koordinate " + str(location))
print ("und jetzt bist du bei koordinate " + str(location2))