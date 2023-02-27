import os
import time
import pyautogui

cumle = ['AI Kısa bilgi NO:' + str(i) for i in range(1, 366)]
tweat_sayisi = 0

while True:

    for tweet in cumle:
        os.chdir("C:\Program Files\Google\Chrome\Application")
        os.system("chrome.exe")
        time.sleep(0.5)
        pyautogui.write("https://chat.openai.com/chat")
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.write("cok kisa ilginc bir bilgi")
        pyautogui.press('enter')
        time.sleep(11)
        pyautogui.press('F11')
        time.sleep(0.5)
        pyautogui.click(x=772, y=124, button='left', clicks=3, interval=0.25)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'F4')
        time.sleep(0.5)
        os.chdir("C:\Program Files\Google\Chrome\Application")
        os.system("chrome.exe")
        time.sleep(0.5)
        pyautogui.write('https://twitter.com/compose/tweet')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write(tweet)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'F4')
        tweat_sayisi += 1
        if tweat_sayisi >= 365:
            print("Tüm tweatler atıldı!")
            break
        time.sleep(15)
