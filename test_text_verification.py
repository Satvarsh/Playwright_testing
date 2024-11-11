import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.google.com/")
    page.get_by_label("Search", exact=True).click()
    page.get_by_label("Search", exact=True).fill("Wikipedia")
    page.goto("https://www.wikipedia.org/")
    page.get_by_label("Search Wikipedia").click()
    page.get_by_role("button", name="Collapse").click()
    page.get_by_label("close").click()
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("New")
    page.get_by_label("Search Wikipedia").press("Enter")
    expect(page.locator("#firstHeading")).to_contain_text("New")
    text = page.locator("#firstHeading").text_content()
    print(text)

    # page.goto("https://www.w3schools.com/html/html_forms.asp")
    # page.get_by_placeholder("Search...").click()
    # page.get_by_placeholder("Search...").fill("Samm")
    # page.get_by_label("Button to search").click()
    # page.locator("input[name='firstname']").fill("Satvarsh")
    # page.locator("input[name='lastname']").fill("Gondala")
    # page.get_by_label("First name:").click()
    # page.get_by_label("First name:").fill("Satvarsh")
    # page.get_by_label("Last name:").click()
    # page.get_by_label("Last name:").fill("Gondala")
    # with page.expect_popup() as page1_info:
    #     page.locator("#main div").filter(has_text="Example First name: Last name").get_by_role("button").click()
    # page1 = page1_info.value
    # expect(page1.locator("h1")).to_contain_text("Submitted Form Data")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
