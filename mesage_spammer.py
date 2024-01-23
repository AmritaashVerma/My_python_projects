import pyautogui
import time
from timeit import default_timer as timer

start = timer()

typ = input("Do you want to spam emojis on whatsapp web(press e) or a simple text message(press t): ")
msg = input("Enter the message or emoji you want to spam: ")
num = input("Enter the number of times you want to spam the message: ")
i = 0

if typ in ['t', 'T', ' t', ' T']:
	print("Get ready, the spamming starts in 5")
	time.sleep(1)
	print("4")
	time.sleep(1)
	print("3")
	time.sleep(1)
	print("2")
	time.sleep(1)
	print("1")
	time.sleep(1)
	print("FIRE IN THE HOLE!!!!")
	time.sleep(1)
	while i < float(num):
		pyautogui.typewrite(msg)
		time.sleep(float(0.25))
		pyautogui.press("enter")
		i = i+1

elif typ in ['e', 'E', ' e', ' E']:
	print("Get ready, the spamming starts in 5")
	time.sleep(1)
	print("4")
	time.sleep(1)
	print("3")
	time.sleep(1)
	print("2")
	time.sleep(1)
	print("1")
	time.sleep(1)
	print("FIRE IN THE HOLE!!!!")
	time.sleep(1)
	while i < float(num):
		pyautogui.typewrite(":" + msg)
		time.sleep(float(0.25))
		pyautogui.press("enter")
		time.sleep(float(0.25))
		pyautogui.press("enter")
		i = i+1

else:
	print("Invalid response, either enter e or t in the first question.")

end = timer()
print(start-end)