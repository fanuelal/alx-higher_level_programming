#!/usr/bin/python3
"""Write a script that lists all State objects that
contain the letter a from t\
he database hbtn_0e_6_usa"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    searched = session.query(State).filter(State.name == sys.argv[4]).first()
    if searched:
        print('{}'.format(searched.id))
    else:
        print('Not found')
    session.close()
