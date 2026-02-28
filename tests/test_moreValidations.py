import time

from playwright.sync_api import Page, expect


def test_UIchecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    
     #Radio button click
    page.locator("input[value='radio1']").check()
    
    #Search box filtering items
    page.get_by_role("textbox",name="Type to Select Countries").fill("india")
    page.locator(".ui-autocomplete",has_text="India").click()
    
    #Select options 
    page.get_by_role("combobox").select_option("option2")
    
    #Checkbox
    page.locator("#checkBoxOption2").check()
    
    #Switch to tab 
    # with page.expect_popup() as newPage:
    #     page.locator("#opentab").click()
    #     tab1 = newPage.value
    #     tab1.get_by_role("link",name="courses").click()
    #     expect(tab1.get_by_role("heading",name="My courses")).is_visible()
    
    #Window switch  
    # with page.expect_popup() as windows:
    #     page.locator("#openwindow").click()
    #     window_page = windows.value
    #     expect(window_page).to_have_title("QAClick Academy - A Testing Academy to Learn, Earn and Shine")
    
    #Hide, Display and placeholder
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Table Data 
    headers = page.locator("table tbody tr th")
    index_value = None
    for i in range(headers.count()):
        if "Course" in headers.nth(i).text_content():
            index_value=i
            break
    row_data = page.locator("table tbody tr").filter(has_text="30").first
    expect(row_data.locator("td").nth(index_value)).to_contain_text("Selenium")
    
    #Scroll table: 
    table = page.locator("#product").nth(1)
    table.scroll_into_view_if_needed()  #Optional This lines helps to scroll the table if needed
    headers2 = page.locator("table thead tr th")
    index_val = None
    for i in range(headers2.count()):
        if "City" in headers2.nth(i).text_content():
            index_val= i
            break
    row_data2 = page.locator("table tbody tr").filter(has_text="Ronaldo")
    expect(row_data2.locator("td").nth(index_val)).to_have_text("Chennai")

    #Alert boxes
    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Alert").click()
    
    #Frame Handling - Use frameLocators
    FramePage = page.frame_locator("#courses-iframe")
    FramePage.get_by_role("link",name="All Access plan").click()
    expect(FramePage.locator("body")).to_contain_text("Happy Subscibers")
    
    #Mouse hover - Use hover method
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()
   
    
    

def test_VegMart(page:Page):
    
    #Check the price of rice is equal to 37
    #Identify the price colum
    #Identify the rice column
    #Extract the price of the rice  and compare to 37
    
    #Tables Handling
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    with page.expect_popup() as NewPage:
        page.get_by_role("link",name="Top Deals").click()
        Page1= NewPage.value
        
        # Finding table headers
        # rice_row = Page1.locator("table tbody tr").filter(has_text='Rice')
        # rice_price = rice_row.locator("td").nth(1).text_content()
        # assert int(rice_price) == 37

        header_texts = Page1.locator("table thead tr th")
        index_value = None
        for i in range(header_texts.count()):
            if "Price" in header_texts.nth(i).text_content():
                index_value=i
                break
        rice_col = Page1.locator("tr").filter(has_text="Rice")
        rice_price = rice_col.locator("td").nth(index_value).text_content()
        assert int(rice_price)==37
        
    