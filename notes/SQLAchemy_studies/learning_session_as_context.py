from sqlalchemy.orm import Session
from User import User
from engine import engine

with Session(engine) as session:
    user = session.get(User,1)
    print(user.to_dict())