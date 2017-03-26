# -*- coding: utf-8 -*-
import time
from selenium import webdriver
wd = webdriver.PhantomJS()
success = True
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.goodreads.com/")
    wd.find_element_by_id("userSignInFormEmail").send_keys("pseudoanime@gmail.com")
    wd.find_element_by_id("user_password").click()
    wd.find_element_by_id("user_password").clear()
    wd.find_element_by_id("user_password").send_keys("inuyasha")
    wd.find_element_by_css_selector("input.gr-button.gr-button--dark").click()
    pageNo = 1
    wd.get("https://www.goodreads.com/")
    wd.get("https://www.goodreads.com/giveaway?page=" + str(pageNo))
        while True:
        print bannedUrls
        if  (pageNo > 3):
            wd.quit()
        giveawayUrls = wd.find_elements_by_link_text("Enter Giveaway")
        print len(giveawayUrls)
        if len(giveawayUrls) == len(bannedUrls) :
            bannedUrls = [];
            pageNo +=1
        elif len(giveawayUrls) > 0 :
            for giveaway in giveawayUrls:
                currentUrl = giveaway.get_attribute("href")
                if not currentUrl in bannedUrls :
                    giveaway.click()
                    if (wd.current_url == "https://www.goodreads.com/giveaway") :
                        print "error"
                        bannedUrls.append(currentUrl)
                        wd.get("https://www.goodreads.com/giveaway?page=" + str(pageNo))
                        break
                    else :
                        wd.find_element_by_id("addressSelect2781698").click()
                        if not wd.find_element_by_id("termsCheckBox").is_selected():
                            wd.find_element_by_id("termsCheckBox").click()
                        if wd.find_element_by_id("want_to_read").is_selected():
                            wd.find_element_by_id("want_to_read").click()
                        wd.find_element_by_id("giveawaySubmitButton").click()
                        wd.get("https://www.goodreads.com/giveaway?page=" + str(pageNo))
                        break
        else :
            pageNo +=1
            wd.get("https://www.goodreads.com/")
            wd.get("https://www.goodreads.com/giveaway?page=" + str(pageNo))
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
