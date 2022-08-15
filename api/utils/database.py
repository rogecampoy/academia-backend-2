from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def db_engine():
    db_name = 'my_database'
    db_user = 'postgres'
    db_pass = 'postgres'
    db_host = 'localhost'
    db_port = '5432'

    db_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

    return db_string


engine = create_engine(db_engine())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()