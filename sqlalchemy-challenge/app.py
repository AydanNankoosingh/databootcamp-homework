# Flask imports
from flask import Flask, jsonify

# SQLAlchemy imports
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Date imports
import datetime as dt
from dateutil.relativedelta import relativedelta

# NumPy import
import numpy as np

# ------------------------------------------------------------------------------

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# ------------------------------------------------------------------------------


app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    Surf's Up API<br/><br/>

    Available routes:<br/><br/>
    precipitation data:<br/>
    ---- /api/v1.0/precipitation<br/><br/>
    station data:<br/>
    ---- /api/v1.0/stations<br/><br/>
    temperature data:<br/>
    ---- /api/v1.0/tobs/api/v1.0/start_date<br/>
    ---- /api/v1.0/start_date/end_date<br/>
    """



@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query setup -- dates
    max_date = session.query(func.max(Measurement.date))
    latest = dt.date.fromisoformat((max_date.first()[0]))
    year_from_latest = latest - relativedelta(years=1)

    # Perform a query to retrieve the data and precipitation scores
    q = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date <= latest).filter(Measurement.date >= year_from_latest).all()

    # close session
    session.close()

    # Convert list of tuples into list of dicts
    prcp = []
    [prcp.append({x[0]:x[1]}) for x in q]

    return jsonify(prcp)



@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the station data
    q = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    #close session
    session.close()

    # Convert list of tuples into list of dicts
    stations_data = []
    [stations_data.append({'station':x[0], 'name':x[1], 'latitude':x[2], 'longitude':x[3], 'elevation':x[4]}) for x in q]

    return jsonify(stations_data)



@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query setup -- dates
    max_date = session.query(func.max(Measurement.date))
    latest = dt.date.fromisoformat((max_date.first()[0]))
    year_from_latest = latest - relativedelta(years=1)

    # Perform a query to retrieve the temperature obs data
    q = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
        filter(Measurement.date <= latest).filter(Measurement.date >= year_from_latest).all()

    # close session
    session.close()

    # Convert list of tuples into list of dicts
    temp_data = []
    [temp_data.append({'date':x[0], 'station':x[1], 'tobs':x[2]}) for x in q]

    return jsonify(temp_data)



@app.route("/api/v1.0/<start>")
def temp_open(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query setup -- dates
    max_date = session.query(func.max(Measurement.date))
    min_date = session.query(func.min(Measurement.date))

    if start >= min_date.all()[0][0] and start <= max_date.all()[0][0]:
        # Perform a query to retrieve the min, avg & max temperature from the start date or later
        q = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()

        # close session
        session.close()

        # Convert list of tuples into list of dicts
        temp_data = []
        temp_data.append({'min':q[0][0], 'avg':q[0][1], 'max':q[0][2]})

        return jsonify(temp_data)
    else:
        # close session
        session.close()

        return jsonify({'error':'invalid date'})



@app.route("/api/v1.0/<start>/<end>")
def temp_closed(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query setup -- dates
    max_date = session.query(func.max(Measurement.date))
    min_date = session.query(func.min(Measurement.date))

    if start >= min_date.all()[0][0] and start <= max_date.all()[0][0] and end >= min_date.all()[0][0] and end <= max_date.all()[0][0] and start <= end:
        # Perform a query to retrieve the min, avg & max temperature from the start date or later
        q = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).filter(Measurement.date <= end).all()

        # close session
        session.close()

        # Convert list of tuples into list of dicts
        temp_data = []
        temp_data.append({'min':q[0][0], 'avg':q[0][1], 'max':q[0][2]})

        return jsonify(temp_data)
    else:
        # close session
        session.close()

        return jsonify({'error':'invalid combination of dates'})


if __name__ == "__main__":
    app.run()
