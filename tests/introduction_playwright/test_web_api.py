import time

from playwright.sync_api import Page, Playwright, expect
from tests.introduction_playwright.utils.apiBase import ApiUtils  

def test_e2e_webApi(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    
    #Create Order 
    order_details = ApiUtils()
    order_id = order_details.createOrder(playwright) 
    print(order_id)
    #Login 
    page.get_by_placeholder("email@example.com").fill("vis1@gmail.com")
    page.locator("#userPassword").fill("VisTech@0126")
    page.locator(".btn").click()
    page.get_by_role("button",name="Orders").click()
     
    #Order confirmation
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")