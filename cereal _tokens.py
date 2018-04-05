import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

wd = webdriver.PhantomJS()
#wd = webdriver.Chrome()
wd.implicitly_wait(60)

try:
    wd.get("https://www."+sys.argv[1]+".co.uk/collect-and-win/tokens/")
    el = wd.find_element_by_css_selector("a[data-open='tokens-login']")
    wd.execute_script("arguments[0].click();", el)

    wd.find_element_by_id("user_login").send_keys(sys.argv[2])
    wd.find_element_by_id("tokens-login-email-button").click()
    wd.find_element_by_id("user_password").send_keys(sys.argv[3])
    wd.find_element_by_id("tokens-login-password-button").click()
    time.sleep(2)

    for x in range(0, 3):
        wd.get("https://www."+sys.argv[1]+".co.uk/collect-and-win/spin-to-win/")
        el = wd.find_element_by_css_selector("img[class='iw-spin']")
        time.sleep(2) 
        wd.execute_script("arguments[0].click();", el)
        time.sleep(10)

finally:
    wd.quit()