from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that represents the database
engine = create_engine('sqlite:///example.db', echo=True)  # Replace 'sqlite:///example.db' with your database URL

# Create a base class using declarative_base()
Base = declarative_base()

# Define a class that represents a table in the database
class User(Base):
    __tablename__ = 'users'  # Table name

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example usage:
# Adding data
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

# Querying data
users = session.query(User).all()
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")

# Closing the session
session.close()
