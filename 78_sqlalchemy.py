from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///test.db", echo=True)

Base = declarative_base()

# Table model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
user1 = User(name="Alice")
user2 = User(name="Bob")

session.add(user1)
session.add(user2)
session.commit()


users = session.query(User).all()

for user in users:
    print(user.id, user.name)