#!/usr/bin/python3
"""14-model_city_fetch_by_state
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    a = State.id
    b = City.state_id
    for c, i in session.query(State, City).filter(a == b).all():
        print("{}: ({}) {}".format(c.name, i.id, i.name))
