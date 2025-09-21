import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://pageindexrepo-pjcqzhtmkf9sh9siumr5j9.streamlit.app/", timeout=60000)
        await page.wait_for_selector("body")
        text = await page.inner_text("body")
        print(text[:1000])

asyncio.run(run())
