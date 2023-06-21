#!/usr/bin/python3
"""9-model_state_filter_a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    filter_a = session.query(State).filter(State.name.contains("a"))\
        .order_by(State.id.asc()).all()
    for i in filter_a:
        print("{}: {}".format(i.id, i.name))
