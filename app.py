import flask
import os
import selenium
import time
from flask import send_from_directory
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-sh-usage')

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
    driver.get('https://parcelsapp.com/en/tracking/9400128206335591615282')
    #time.sleep(10)

    #tracking_number = driver.find_element_by_css_selector('#tracking-info > div:nth-child(1) > div.row.parcel > div.col-md-4.col-lg-4 > table > tbody > tr:nth-child(1) > td.value > span').text
    tracking_number = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tracking-info > div:nth-child(1) > div.row.parcel > div.col-md-4.col-lg-4 > table > tbody > tr:nth-child(1) > td.value > span')))
    return tracking_number.text
if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()