import pyautogui
import time

search_icon_location = pyautogui.locateOnScreen('Screenshot_1.png', confidence=0.8)
if search_icon_location:
        pyautogui.click(search_icon_location)
        print("Search icon clicked.")
        time.sleep(1)
        pyautogui.write('whatsapp')
        pyautogui.press('enter')  
        time.sleep(2)
        pyautogui.write('Homies')
        ammu_icon_location = pyautogui.locateOnScreen('Happy_birthday_email/Screenshot_2.png', confidence=0.8)
        if ammu_icon_location:
            pyautogui.click(ammu_icon_location)
        else:
            exit()
        time.sleep(3)
        pyautogui.write('Happy Birthday! May your day be filled with joy! 🎂')
        time.sleep(1)
        pyautogui.press('enter')  
else:
        print("Search icon not found.")
