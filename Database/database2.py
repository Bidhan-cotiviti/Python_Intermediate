from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@host.docker.internal/postgres')

connection = engine.connect()

Base = declarative_base()

class Supervisor(Base):
    __tablename__ = 'supervisors'
    
    id = Column(Integer(), primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email_id = Column(String(150), nullable=False)
    
    projects = relationship('Project', backref='supervisor')

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer(),primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    submitted_on = Column(DateTime(), default=datetime.now)
    supervisor_id = Column(Integer(), ForeignKey('supervisors.id'))
    
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

Bidhan = Supervisor(
    firstname="Bidhan",
    lastname="Khatiwada",
    email_id="bidhankhatiwada32@gmail.com"
)

project6 = Project(

    title = "NLP",
    supervisor = Bidhan
)
session.add(project6)
session.delete(project6)
session.commit()
session.flush()

