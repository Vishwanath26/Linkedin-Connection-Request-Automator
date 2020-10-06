from selenium.webdriver.common.keys import Keys
import pyautogui as pag


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def main():
    # url of LinkedIn
    url = "https://www.linkedin.com"
    driver.get(url)
    username = driver.find_element_by_name("session_key")
    username.send_keys('Your Email here')
    
    password = driver.find_element_by_name("session_password")
    password.send_keys('Your Password here')
    
    # Getting the tag for submit button
    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    print('successfully logged in')
    
    for k in range (5, 9):
        url2 = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B"96622"%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page='+str(k)+'&title=Engineer'  
        driver.get(url2)
        if k is 5:
            time.sleep(5)
            pag.click(1273, 322)

        x = 960
        y = 470
        for i in range(0, 8):
            pag.moveTo(x, y, duration=2, tween=pag.easeInOutQuad)
            pag.click();
            pag.click(934, 460);
            time.sleep(2)
            y+=159
            if i is 3:
                driver.execute_script("window.scrollTo(0, 498)") 
                print('scrolled')
                x = 960
                y = 470
     


if __name__ == '__main__':
    main()


