# class

# pip install sqlalchemy

from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_cities_dub'

    id = Column(Integer, primary_key=True)
    city = Column(String)

    def __repr__(self):
        return f'User#id:{self.id}#city:{self.city}'


engine = create_engine('sqlite://', echo=True)
Base.metadata.create_all(engine)

# first endpoint
with Session(engine) as session:
    myself = User(
        id=224787,
        city='Surgut'
    )

    session.add_all([myself])
    session.commit()

# second endpoint ORM
from sqlalchemy import select

session = Session(engine)
users = select(User).where(User.city.in_(['Surgut', 'Yerevan']))

for user in session.scalars(users):
    print(user)


