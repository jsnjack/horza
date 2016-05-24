from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Configuration(Base):
    __tablename__ = "configuration"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    auth_token = Column(String)


class Repository(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True)
    path = Column(String, unique=True)

    def __repr__(self):
        return "<Repository {} {}>".format(self.id, self.path)


class PullRequest(Base):
    __tablename__ = "pullrequest"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    github_id = Column(Integer, unique=True)
