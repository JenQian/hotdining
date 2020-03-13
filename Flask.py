# Flask.py
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Import scrapting dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import functools
import operator
from datetime import date
import time
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///restaurants.sqlite")
print(engine)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Restaurant = Base.classes.restaurants

#################################################
# Flask Setup
#################################################
app = Flask(__name__)




@app.route("/api/v1.0/restaurants")
def restaurants():
     # Create our session (link) from Python to the DB
     session = Session(engine)

     """Return a list of all restaurants"""
     # Query all passengers
     results = session.query(Restaurant).all()

     df = pd.DataFrame([(d.index, d.name, d.address, d.city, d.state, d.description, d.star, d.full_address, d.postal_code, d.platform) for d in results], columns=['index', 'name', 'address', 'city', 'state', 'description', 'star', 'full_address', 'postal_code', 'platform'])
     data = df.to_dict('records')
     session.close()

     # Convert list of tuples into normal list

     return jsonify(data)

@app.route("/api/v1.0/available_times")
def available_times():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all restaurants
    
    results = session.query(Restaurant.name, Restaurant.platform, Restaurant.star, Restaurant.full_address, Restaurant.description).all()
    available_times = []
    current_urls = []
    today = date.today().strftime("%Y-%m-%d")
 


    for name, platform, star, full_address, description in results:
     #res_name = replace....

     #data = checkava(res_name, today, 'resy')
               #available_times.append({name: data})
          def check_avail(name,today,platform):
            #https://resy.com/cities/ny/le-bernardin?date=2020-03-12&seats=2
               

                if platform == 'Resy':
                    name = name.strip()
                    name = name.lower()
                    res_name = name.replace(' ', '-')
                    executable_path = {'executable_path': '/Users/jeqian/Documents/DA Bootcamp/CU-NYC-DATA-PT-10-2019-U-C/chromedriver'}
                    browser = Browser('chrome', **executable_path, headless=True,user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36")

                    base_url = 'https://resy.com/cities/ny/'
                    resy_url = base_url+res_name+'?date='+today+'&seats=2'

                    #resy_url = 'https://resy.com/cities/ny/the-modern?date=2020-03-12&seats=2'
                    browser.visit(resy_url)
                    print(resy_url)
                    #time.sleep(np.random.randint(4,10))
                    current_url = browser.url
                    resy_html = browser.html
                    resy_soup = BeautifulSoup(resy_html, 'html.parser')
                    resy_path = resy_soup.find_all(class_='ResyInlineBooking__wrapper--service')
                    times = [ times.text for times in functools.reduce(operator.iconcat, [res.find_all('div', class_="time") for res in resy_path], [])]
                    #if times == [] and current_url!='https://resy.com/' :
                        #raise Exception

                    return times, current_url

                elif platform == 'OpenTable':
                    executable_path = {'executable_path': '/Users/jeqian/Documents/DA Bootcamp/CU-NYC-DATA-PT-10-2019-U-C/chromedriver'}
                    browser = Browser('chrome', **executable_path, headless=True,user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36")
                    name = name.lower()
                    res_name = name.replace(' ', '-')
                    base_url = 'https://www.opentable.com'
                    #other_parts = '?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=ad4842b8-9fbf-4a79-846f-4c6b7a43f4fd&p=2&sd='
                    #end = '+20%3A00'
                    #op_url = base_url+res_name+other_parts+today+end
                    op_url = base_url+res_name
                    #op_url = 'https://www.opentable.com/r/catch-steak-maritime-hotel-new-york?avt=eyJ2IjoxLCJtIjoxLCJwIjowfQ&corrid=ad4842b8-9fbf-4a79-846f-4c6b7a43f4fd&p=2&sd=2020-03-14+20%3A00'
                    browser.visit(op_url)
                    browser.find_by_text('Find a Table').first.click()
                    r = requests.get(browser.url)
                    current_url = browser.url
                    print(op_url)
                    #op_html = browser.html
                    op_soup = BeautifulSoup(r.text, 'html.parser')
                    times = [times.text for times in op_soup.find_all(class_='f2cc84a2')[0].find_all("span")]
                    #if
                      # 
                    return times, current_url
               
                else:      
                    times = 'Not Available'
                    current_url = 'NA'
                    return times, current_url

              

          times, current_url = check_avail(name,today,platform)

          available_times.append([name, today, times,  star, full_address, description, current_url])

    return jsonify(available_times)

#@app.route("/api/v1.0/combined")
#def res_avail():
    # Create our session (link) from Python to the DB
 #   session = Session(engine)
  #  results = session.query(Restaurant.name, Restaurant.platform, Restaurant.star, Restaurant.full_address, Restaurant.description).all()
   # res_avail = []


    #for name, platform in results:



    #return jsonify(res_avail)

if __name__ == "__main__":
    app.run(debug=True)