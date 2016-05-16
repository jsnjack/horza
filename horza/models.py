from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Repository(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True)
    path = Column(String)

    def __repr__(self):
        return "<Repository {} {}>".format(self.id, self.path)
