import pyautogui
import time as timer

def main():
    horizontal_coordinate = 645
    vertical_coordinate = 1050
    pyautogui.moveTo(horizontal_coordinate, vertical_coordinate, 0.8)
    pyautogui.click()
    timer.sleep(6)
    pyautogui.getWindowsWithTitle("Zoom")[0].maximize()
    x_coordinate = 750
    y_coordinate = 393
    pyautogui.moveTo(x_coordinate, y_coordinate, 0.8)
    pyautogui.click()
    timer.sleep(5)
    pyautogui.typewrite(str(id1))
    pyautogui.press('enter')
    timer.sleep(5)
    pyautogui.typewrite(str(passwd1))
    pyautogui.press('enter')
    #the recording part
    timer.sleep(time_in_sec)
    pyautogui.hotkey('win', 'alt', 'r')

def sec():
    x_coordinate = 750
    y_coordinate = 393
    pyautogui.moveTo(x_coordinate, y_coordinate, 0.8)
    pyautogui.click()
    timer.sleep(5)
    pyautogui.typewrite(str(id2))
    pyautogui.press('enter')
    timer.sleep(5)
    pyautogui.typewrite(str(passwd2))
    pyautogui.press('enter')
    #the recording part
    timer.sleep(1090)
    pyautogui.hotkey('win', 'alt', 'r')

def third():
    x_coordinate = 750
    y_coordinate = 393
    pyautogui.moveTo(x_coordinate, y_coordinate, 0.8)
    pyautogui.click()
    timer.sleep(5)
    pyautogui.typewrite(str(id3))
    pyautogui.press('enter')
    timer.sleep(5)
    pyautogui.typewrite(str(passwd3))
    pyautogui.press('enter')
    #the recording part
    timer.sleep(1090)
    pyautogui.hotkey('win', 'alt', 'r')


res = input("Do you want automate 1 class(1) or automate all the classes(2)?: ")
if res in ['1']:
    time = input("Enter how many minutes away is the meeting from starting(always enter 2 or 3 minutes more from the actual time): ")
    id1 = input("Enter the meeting id: ")
    passwd1 = input("Enter the meeting password: ")
    time_in_sec = float(float(time) * 60)
    main()
elif res in ['2']:
    time = input("Enter how many minutes away is the meeting from starting(always enter 2 or 3 minutes more from the actual time): ")
    id1 = input("Enter the first meeting id: ")
    passwd1 = input("Enter the first meeting password: ")
    id2 = input("Enter the second meeting: ")
    passwd2 = input("Enter the second meeting password: ")
    id3 = input("Enter the third meeting id: ")
    passwd3 = input("Enter the third meeting password: ")
    time_in_sec = float(float(time) * 60)
    main()
    timer.sleep(3600)
    sec()
    timer.sleep(3600)
    third()
else:
    print("Error 400: Bad response!")

