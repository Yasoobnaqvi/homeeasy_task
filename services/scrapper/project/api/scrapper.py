
import requests, sys, os 
from project.api import models
from flask import Blueprint, jsonify
from project import db
from bs4 import BeautifulSoup

scrapper_blueprint = Blueprint('scrapper', __name__)

@scrapper_blueprint.route('/scrap', methods=['GET'])
def scrap():
    response_object = {
            "status" : "fail",
            "message" : "Something went wrong"
        }
    url = "https://www.rentcafe.com/apartments-for-rent/us/tx/houston/"
    response = requests.get(url)
    try:
         # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the relevant elements and extract data
        listings = soup.find("ul", class_="listings")
        apartments = listings.find_all("li", class_="listing-details")
        
        for apartment in apartments:
            # Extract apartment details
            name = apartment.find("div", class_="listing-name").text.strip()
            address = apartment.find("div", class_="listing-address").text.strip()
            city = apartment.find("span", class_="rent").text.strip()
            state = apartment.find("span", class_="availability").text.strip()

        building = models.Building()
        building.name = name
        building.address = address
        building.city = city
        building.state = state
        db.session.commit()
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
