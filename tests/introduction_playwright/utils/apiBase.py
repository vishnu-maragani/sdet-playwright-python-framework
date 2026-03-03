from playwright.sync_api import Playwright
ordersPayload = {"orders":[{"country":"India","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}
loginPayload = {"userEmail":"vis1@gmail.com","userPassword":"VisTech@0126"}
class ApiUtils:
    
    def getToken(self,playwright:Playwright):
        #Login Auth toke 
        login_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        token = login_context.post("/api/ecom/auth/login",
                           data=loginPayload,
                           headers={
                               "Content-Type":"application/json"
                           })
        assert token.ok
        responseBody  = token.json()
        return responseBody["token"]
    
    def createOrder(self,playwright:Playwright):
        token = self.getToken(playwright)
        #Post request : 
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        order_response = api_request_context.post("/api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={
                                     "Authorization":token,
                                     "Content-Type":"application/json"
                                 })
        order_id = order_response.json()
        return order_id['orders'][0]