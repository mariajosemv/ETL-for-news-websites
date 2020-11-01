from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newspaper_db.db')

#engine = create_engine('mysql//root:password@localhost:3306/newspaper_db') # create db
Session = sessionmaker(bind=engine)
Base = declarative_base()

