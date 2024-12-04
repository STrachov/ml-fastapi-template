import asyncio
import random
import time

from playwright.async_api import async_playwright
#from playwright_stealth import stealth_async


async def screenshot_page(page, number: int = 1):
    screenshot_path = f"./screenshots/screenshot{number}.png"
    await page.screenshot(path=screenshot_path)
    print(f"Screenshot {number} was created")

async def test_playwright():
    try:
        # Start Playwright
        async with async_playwright() as p:
            # Launch the browser
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(
                #user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                #proxy={"server": "http://myproxyserver.com:8080"},
            )
            page = await context.new_page()
            #await stealth_async(page)

            # Open a website
            await page.goto('https://www.upwork.com/ab/account-security/login')
            print(f"Page opened")
            await screenshot_page(page,1)


            # Simulate natural typing and mouse movements
            await page.type(
                '#login_username',
                'test@gmail.com',
                delay=random.randint(300, 1000)
            )

            #await page.keyboard.press("Enter")

            #or

            await page.mouse.move(
                x=random.randint(600, 900),
                y=random.randint(300, 400),
                steps=3
            )


            # Add random delay between actions
            #time.sleep(random.uniform(1, 3))
            await page.click('#login_control_continue')

            # Take action, such as clicking login or other necessary steps
            await page.click('#login_control_continue')

            # # Wait for the password input field to appear
            await page.wait_for_selector('#login_password', timeout=3000)
            # 
            # # Step 2: Enter Password and click "Log in"
            await page.type(
                '#login_password',
                'password',
                delay=random.randint(200, 1500)
            )
            await page.keyboard.press("Enter")

            await page.mouse.move(
                random.randint(0, 600),
                random.randint(34, 800),
                steps=10
            )

            # Add random delay between actions
            time.sleep(random.uniform(3, 5))

            # Take action, such as clicking login or other necessary steps
            #await page.click('#login_control_continue')




            # Close the browser
            await browser.close()

    except Exception as e:
        print(f"Playwright environment check failed: {e}")

# Run the test
asyncio.run(test_playwright())
