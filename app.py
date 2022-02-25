import flask
import os
import selenium
import time
from flask import send_from_directory
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    #driver.get('https://parcelsapp.com/en/tracking/9400128206335591615282')
    #time.sleep(10)
    driver.get('https://www.youtube.com')
    tracking_number = driver.find_element_by_css_selector('#endpoint > tp-yt-paper-item > yt-formatted-string')
    #driver.close()
    return tracking_number
if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()