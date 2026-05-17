# Playwright Human-like Automation
# Open Chrome -> Go to YouTube directly
# Search "moral stories" -> Open first video

from playwright.sync_api import sync_playwright
import time
import random

with sync_playwright() as p:

    # Launch persistent Chrome profile
    browser = p.chromium.launch_persistent_context(
        user_data_dir="playwright_profile",  # Saves cookies/session
        channel="chrome",
        headless=False,
        viewport={"width": 1366, "height": 768},
        args=[
            "--start-maximized",
            "--disable-blink-features=AutomationControlled"
        ]
    )

    # Open page
    page = browser.new_page()

    # ---------------------------------------------------
    # STEP 1: Open YouTube directly
    # ---------------------------------------------------

    page.goto("https://www.youtube.com")

    # Wait naturally
    time.sleep(random.uniform(3, 5))

    # ---------------------------------------------------
    # STEP 2: Click Search Bar
    # ---------------------------------------------------

    page.click('input[name="search_query"]')

    # Type like human
    search_text = "moral stories"

    for char in search_text:
        page.keyboard.type(char)
        time.sleep(random.uniform(0.05, 0.2))

    # Press Enter
    page.keyboard.press("Enter")

    # Wait for results
    time.sleep(random.uniform(4, 6))

    # ---------------------------------------------------
    # STEP 3: Open First Video
    # ---------------------------------------------------

    first_video = page.locator('(//*[@id="video-title"])[1]')
    first_video.click()

    # Watch video for few seconds
    time.sleep(10)

    print("Automation Completed Successfully!")

    # Keep browser open
    input("Press ENTER to close browser...")

    browser.close()
    