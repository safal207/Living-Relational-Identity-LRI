import time
from playwright.sync_api import sync_playwright

def test_alice_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the app
        page.goto("http://localhost:8005")

        # Wait for title
        page.wait_for_selector("h1")

        # Take initial screenshot
        page.screenshot(path="verification/alice_initial.png")
        print("Initial screenshot taken.")

        # Click "Study"
        page.click("button.btn-action")
        page.wait_for_timeout(1000) # Wait for reload

        # Click "Promote"
        page.click("button.btn-promote")
        page.wait_for_timeout(1000)

        # Take screenshot after actions
        page.screenshot(path="verification/alice_promoted.png")
        print("Promoted screenshot taken.")

        # Click "Error"
        page.click("button.btn-error")
        page.wait_for_timeout(1000) # wait for alert or page reload

        # Handle dialog if any (though we are headless, so alert might be suppressed or need handling)
        # The demo uses alert() on body onload if error state. Playwright auto-dismisses dialogs by default but we can listen.

        page.on("dialog", lambda dialog: dialog.accept())

        # Take screenshot of error state
        page.screenshot(path="verification/alice_error.png")
        print("Error screenshot taken.")

        browser.close()

if __name__ == "__main__":
    test_alice_demo()
