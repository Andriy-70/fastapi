import os.path
import uuid

from playwright.async_api import async_playwright


async def make_screenshot(url: str):

    file_name = str(uuid.uuid4()) + ".png"

    file_path = os.path.join("screenshots", file_name)

    async with async_playwright() as p:
        browser = await(p.chromium.launch(headless=True)) # браузер

        page = await browser.new_page()

        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.screenshot(path=file_path)

        await browser.close()
    return file_path