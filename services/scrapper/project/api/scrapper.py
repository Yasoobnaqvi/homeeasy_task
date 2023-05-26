
import sys, os , time , requests
from project.api import models
from flask import Blueprint, jsonify
from project import db
from bs4 import BeautifulSoup
from selenium import webdriver
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
# from proxy_randomizer import RegisteredProviders


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
    baseurl = "https://www.rentcafe.com/apartments-for-rent/us/tx/houston/"
    
    try:

        
        # rp = RegisteredProviders()
        # rp.parse_providers()
        # proxies     = {"https": proxy.get_proxy()}
        # software_names = [SoftwareName.CHROME.value]
        # operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
        # user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        # # Get list of user agents.
        # user_agents = user_agent_rotator.get_user_agents()
        # # Get Random User Agent String.
        # user_agent = user_agent_rotator.get_random_user_agent()
        
        

        
        # print(headers)

        response = requests.get(baseurl)

        # Check if the request was successful (status code 200)
        # if response.status_code == 200:
        #     # Print the HTML content of the response
        #     print(response.text)
        # else:
        #     print("Error:", response.status_code)
        # driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

        # # Navigate to the RentCafe URL
        # page = 1
        # while True:
        #     url = baseurl 
        #     # + "?page=" + str(page)
        #     driver.get(url)
            
        #     if page == 5:
        #         break
        #     # as
        #     wait = WebDriverWait(driver, 20)

        #     innerElement = wait.until(EC.presence_of_element_located((By.ID, "results")))
        #     soup = BeautifulSoup(driver.page_source, "html.parser")
        #     print(innerElement)
        #     details_buttons = soup.select("button[id^='view-details-']")
        #     # details_urls = [button["details-url"] for button in details_buttons]
        #     # for url in details_urls:
        #     #     try:
        #     #         print(url)
                    
        #     #     except:
        #     #         pass
        #     data = []
        #     for element in details_buttons:
        #         data.append(element
        #         )
        #     page += 1
        # # for apartment_element in apartment_elements:
        #     # view_details = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@id, 'veiw-details')]")))

            
        # # db.session.commit()
        # # response_object["asd"] = apartment_cards
        # response_object["data"] = data
        response_object["asd"]  = response.status_code
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

