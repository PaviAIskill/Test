# PyAutoGUI Automation Script
# Opens Google Chrome -> Searches YouTube -> Opens YouTube
# Searches "moral stories" -> Opens first video

import pyautogui
import time
import subprocess

# Safety feature
pyautogui.FAILSAFE = True

print("Automation will start in 5 seconds...")
time.sleep(5)

# ---------------------------------------------------
# STEP 1: Open Google Chrome
# ---------------------------------------------------

# Change the path if Chrome is installed elsewhere
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Open Chrome with Google
subprocess.Popen([chrome_path, "https://www.google.com"])

# Wait for Chrome to open
time.sleep(5)

# ---------------------------------------------------
# STEP 2: Click Google Search Bar
# Coordinates:
# X = 385, Y = 290
# ---------------------------------------------------

pyautogui.click(x=385, y=290)

# Type YouTube
pyautogui.write("YouTube", interval=0.1)

# Press Enter
pyautogui.press("enter")

# Wait for results page
time.sleep(5)

# ---------------------------------------------------
# STEP 3: Click YouTube Link
# Coordinates:
# X = 147, Y = 312
# ---------------------------------------------------

pyautogui.click(x=147, y=312)

# Wait for YouTube to load
time.sleep(7)

# ---------------------------------------------------
# STEP 4: Click YouTube Search Bar
# Coordinates:
# X = 380, Y = 117
# ---------------------------------------------------

pyautogui.click(x=380, y=117)

# Type search text
pyautogui.write("moral stories", interval=0.1)

# Press Enter
pyautogui.press("enter")

# Wait for search results
time.sleep(5)

# ---------------------------------------------------
# STEP 5: Open First Video
# ---------------------------------------------------

# Click first video result
# Adjust coordinates if needed
pyautogui.click(x=796, y=529)

print("Automation Completed Successfully!")