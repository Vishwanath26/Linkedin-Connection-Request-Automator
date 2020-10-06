# import scrapy
# from scrapy import Request
# import re
# from selenium import webdriver  # connect python with webbrowser-chrome
# from selenium.webdriver.common.keys import Keys
# import pyautogui as pag
# import time
#
#
# class MyFirstSpider(scrapy.Spider):
#     name = "JD2"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20070308 Minefield/3.0a1'
#     }
#     start_urls = [
#         "https://www.justdial.com/Ahmedabad/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Bangalore/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Chennai/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Delhi/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Hyderabad/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Kanpur/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Kolkata/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Mumbai/Skoda-Dealers/nct-10076152",
#         "https://www.justdial.com/Pune/Skoda-Dealers/nct-10076152"
#     ]
#     count = 0


# from selenium import webdriver
# #from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
import pyautogui as pag


# def login():
#     # Getting the login element
#     username = driver.find_element_by_id("login-email")
#
#     username.send_keys('vishwanath.sharma724@gmail.com')
#     password = driver.find_element_by_id('login - password')
#     password.send_keys('chandrabhalkinker@@@')
#
#     # Getting the tag for submit button
#     driver.find_element_by_id("login-submit").click()
#     print('successfully logged in')

#
#
# def goto_network():
#     driver.find_element_by_id("mynetwork-tab-icon").click()
#
#
# def send_requests():
#     # Number of requests you want to send
#     n = input("Number of requsts: ")
#
#     for i in range(0, n):
#         # position(in px) of connection button
#         pag.click(880, 770)
#     print("Done !")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def main():
    # url of LinkedIn
    url = "https://www.linkedin.com"

    # url of LinkedIn network page
    #network_url = "http://linkedin.com / mynetwork/"

    # path to browser web driver
    # driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    username = driver.find_element_by_name("session_key")
    username.send_keys('mitasha98@gmail.com')
    
    password = driver.find_element_by_name("session_password")
    password.send_keys('Mahamahim@')
    
    # Getting the tag for submit button
    driver.find_element_by_class_name("sign-in-form__submit-button").click()
    print('successfully logged in')
    
    for k in range (5, 9):
        url2 = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B"96622"%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page='+str(k)+'&title=Engineer'  
        driver.get(url2)
        if k is 5:
            time.sleep(5)
            pag.click(1273, 322)
    # for i in range(0, 10):
    #     test = input(" start sending requests(y / n)")
    #     currentMouseX, currentMouseY = pag.position()
    #     print(currentMouseX)
    #     print(currentMouseY)
    #     driver.execute_script("window.scrollTo(0, 159)") 

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

# def main():
#
#     url = 'https://www.linkedin.com'
#     driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#     driver.get(url)
#     #for login
#     username = driver.find_element_by_id('login - email')
#     username.send_keys('vishwanath.sharma724@gmail.com')
#     password = driver.find_element_by_id('login - password')
#     password.send_keys('chandrabhalkinker@@@')
#     driver.find_element_by_id('login - submit').click()
#     print('successfully logged in')
    # #for company page
    # url2 = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221337%22%5D&facetNetwork=%5B%22S%22%5D&origin=FACETED_SEARCH&title=Engineering'
    # driver.get(url2)
    # #send requests
    # n = input( % u201CNumber
    # of
    # requsts: % u201D)
    # for i in range(0, n):
    #     pag.click(880, 770)
    # print( % u201CDone ! % u201D)

