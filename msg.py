import pywhatkit as pwk
import pyautogui
import time

# import random

# def generate_indian_number():
#     return "+91" + str(random.randint(6000000000, 9999999999))

# print(generate_indian_number()) 

phone = "+91 70073 51XXX" 
message = "This is an automated message"

# repeat = 5  # Number of times to send

# for _ in range(repeat):
pwk.sendwhatmsg_instantly(phone, message) 
pyautogui.press("enter")
time.sleep(2)  
pyautogui.hotkey("ctrl", "w")
time.sleep(1)