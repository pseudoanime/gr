# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from faker import Faker
import random
import sys

cause = sys.argv[1]

wd = webdriver.PhantomJS()
# wd = webdriver.Chrome()
wd.implicitly_wait(60)

fake = Faker()

fakesearch = random.choice([fake.name(),fake.address(), fake.text(), fake.state(), fake.city(),fake.street_name(), fake.country_code(), fake.license_plate(), fake.ean8(), fake.safe_color_name(), fake.company(), fake.catch_phrase(), fake.company_suffix(), fake.bs(), fake.credit_card_provider(), fake.cryptocurrency_code(), fake.currency_code(), fake.timezone(), fake.month_name(), fake.century(), fake.file_extension(), fake.free_email_domain(), fake.ascii_email(), fake.image_url(), fake.uri_page(), fake.user_name(), fake.slug(), fake.uri(), fake.url(), fake.domain_name(), fake.job(), fake.word(), fake.suffix(), fake.msisdn(), fake.ssn(), fake.windows_platform_token()])

try:
    wd.get("http://"+ cause +".easysearch.org.uk/")
    wd.find_element_by_id("searchString").send_keys(fakesearch)
    wd.find_element_by_css_selector(".submit-btn").click()
finally:
    wd.quit()
