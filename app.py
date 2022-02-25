import flask
import os
from flask import send_from_directory
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    #op = webdriver.ChromeOptions()
    #op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    #op.add_argument('--headless')
    #op.add_argument('--no-sandbox')
    #op.add_argument('--disable-dev-sh-usage')

    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
    #driver.get('https://parcelsapp.com/en/tracking/9400128206335591615282')
    #tracking_number = driver.find_element_by_xpath('//*[@id="tracking-info"]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/span')
    #driver.close()
    return "hello world"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()