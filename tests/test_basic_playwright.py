import time

from playwright.sync_api import Page

#One way
def test_example1(playwright):
    browser = playwright.chromium.launch(headless=False)   #Invoking chrome engine
    context = browser.new_context()  #New context Chrome browser
    page = context.new_page() #Taking new Chrome tab
    page.goto('https://rahulshettyacademy.com')

#Second way
def test_exmple2(page:Page):
    page.goto('https://rahulshettyacademy.com')
    assert "Rahul Shetty" in page.title()

#---> #id .class_name
def test_coreLocators(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    assert page.title() !=""
    time.sleep(5)