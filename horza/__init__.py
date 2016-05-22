import logging
import logging.config
import os
import sys
sys.path.append(os.path.dirname(__file__))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings

settings = Settings

logging.config.dictConfig(settings.LOGGING)

# Make sure that working folder is exists
if not os.path.exists(settings.DB_PATH):
    os.makedirs(settings.DB_PATH)

# Database section
engine = create_engine(settings.DB_URL, echo=settings.DB_ECHO)
_Session = sessionmaker(bind=engine)
session = _Session()
