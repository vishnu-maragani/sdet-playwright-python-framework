import time

from playwright.sync_api import Page, Playwright, expect

from tests.introduction_playwright.utils.apiBase import ApiUtils
from tests.introduction_playwright.utils.token_id import ApiToken

def intercept_request(route):
    route.continue_(url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69a7cc3d415d779f9b561ddf")
    
def test_network2(page: Page):
    #Login page
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)
    page.locator("#userEmail").fill("vis1@gmail.com")
    page.locator("#userPassword").fill("VisTech@0126")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button", name="Orders").click()
    page.get_by_role("button", name="View").first.click()
    expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")



#Bypassing the session login 
def test_session_bypass(playwright:Playwright):
    token_id = ApiToken()
    result = token_id.GetTokeId(playwright)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    #Scripting  to inject token session in local storage 
    page.add_init_script(f"""localStorage.setItem('token','{result}')""")
    
    #Login done
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    #Test case done
    page.get_by_role("button",name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()