import urllib
import time

print("Please write the link for the update.")
print("For more info, go to saipanneerselvam.github.io/answers/3245365 .")
link=input()
print("Thank you. We will now update Class.js.")
time.sleep(1)
urllib.urlretrieve(link, "class-js.upds")
time.sleep(3)
print("Updating Complete")