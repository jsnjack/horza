import os
import sys
sys.path.append(os.path.dirname(__file__))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings

settings = Settings

# Make sure that working folder is exists
if not os.path.exists(settings.db_path):
    os.makedirs(settings.db_path)

# Database section
engine = create_engine(settings.db_url, echo=settings.db_echo)
_Session = sessionmaker(bind=engine)
session = _Session()
