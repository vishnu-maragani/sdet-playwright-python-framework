import time

from playwright.sync_api import Page, expect

def test_UiValidationDynamicScript(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iPhoneLocator = page.locator("app-card").filter(has_text="iphone X")
    iPhoneLocator.get_by_role("button").click()
    nokiaLocator = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaLocator.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)



def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    with page.expect_popup() as newPage:
        page.locator(".blinkingText").click()
        child = newPage.value
        email_link = child.get_by_role("link",name="mentor@")
        text = email_link.text_content()
        # expect(email_link).to_have_text("mentor@rahulshettyacademy.com")
        assert text == "mentor@rahulshettyacademy.com"
        

