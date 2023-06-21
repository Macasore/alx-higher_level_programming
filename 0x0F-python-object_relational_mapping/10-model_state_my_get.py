#!/usr/bin/python3
"""10-model_state_my_get
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
    state = sys.argv[4]
    get_state = session.query(State).filter(State.name == state).first()
    if get_state:
        print(get_state.id)
    else:
        print("Not found")
