from playwright.sync_api import Playwright

credentials = {"userEmail":"vis1@gmail.com","userPassword":"VisTech@0126"}
product = {"_id":"69a40c6e415d779f9b4df4c5","product":{"_id":"6960ea76c941646b7a8b3dd5","productName":"iphone 13 pro","productCategory":"electronics","productSubCategory":"mobiles","productPrice":55000,"productDescription":"Apple phone","productImage":"https://rahulshettyacademy.com/api/ecom/uploads/productImage_1767959158182.jpg","productRating":"0","productTotalOrders":"0","productStatus":True,"productFor":"women","productAddedBy":"admin","__v":0}}
class ApiToken: 
    def GetTokeId(self,playwright:Playwright):
        context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = context.post("/api/ecom/auth/login",
                                data=credentials,
                                headers={
                                    'Application-Type':'application/json'
                                })
        result = response.json()
        return result['token']
    
    def AddOrder(self,playwright:Playwright):
        token = self.GetTokeId(playwright)
        context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response =  context.post("/api/ecom/user/add-to-cart",
                     data=product,
                     headers={
                         "Authorization":token,
                         "Content-Type":"application/json"
                     })
        result = response.json()
        return result["message"]