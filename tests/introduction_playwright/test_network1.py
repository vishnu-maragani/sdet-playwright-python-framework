from playwright.sync_api import Page

fakePayloadOrder = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrder
    )
    
def test_network1(page: Page):
    #Login page
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.locator("#userEmail").fill("vis1@gmail.com")
    page.locator("#userPassword").fill("VisTech@0126")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button", name="Orders").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
    
    
