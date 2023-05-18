
import requests, sys, os 
from project.api import models
from flask import Blueprint, jsonify
from project import db
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

scrapper_blueprint = Blueprint('scrapper', __name__)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
webdriver_service = Service(ChromeDriverManager().install())

@scrapper_blueprint.route('/scrap', methods=['GET'])
def scrap():
    response_object = {
            "status" : "fail",
            "message" : "Something went wrong"
        }
    url = "https://www.rentcafe.com/apartments-for-rent/us/tx/houston/"
    # response = requests.get(url)
    try:
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

        # Navigate to the RentCafe URL
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        apartment_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'apartment')]")))
        for apartment_element in apartment_elements:
            # Extract the desired data from each apartment element
            name = apartment_element.find_element(By.CLASS_NAME, "property-name").text
            address = apartment_element.find_element(By.CLASS_NAME, "property-address").text
            rent = apartment_element.find_element(By.CLASS_NAME, "rent").text
        print(name,address,rent)
        # db.session.commit()
        response_object["status"] = "success"
        response_object["message"] = "Scrapped sucessfully"
        
        return jsonify(response_object), 200
    except Exception as e:
        print(f"Exception at : {e}", file=sys.stderr)
        exc_type, fname, exc_tb = sys.exc_info() 
        print(e, file=sys.stderr)
        print(exc_type, fname, exc_tb.tb_lineno, file=sys.stderr)
        response_object["error"] = str(e)
        return jsonify(response_object), 500
