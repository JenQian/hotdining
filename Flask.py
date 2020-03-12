# Flask.py
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


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

if __name__ == "__main__":
    app.run()