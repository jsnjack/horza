import os
import sys
sys.path.append(os.path.dirname(__file__))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings

settings = Settings

engine = create_engine(settings.db_url, echo=settings.db_echo)
_Session = sessionmaker(bind=engine)
session = _Session()
