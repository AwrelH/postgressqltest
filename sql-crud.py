from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# dont forget to set_pg before applying anything

# executing the instructions from chinook database
db = create_engine("postgresql:///chinook")  # /// < local
base = declarative_base()


# class based model "programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     natiionality = Column(String)
#     famous_for = Column(String)


# class based model "countrys visited" table
class VisitedCountries(base):
    __tablename__ = "Visited Countries"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    country_capital = Column(String)
    language = Column(String)
    flagcolors = Column(String)
    whats_good = Column(String)
    size = Column(String)


# instead of connecting to database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (db)
Session = sessionmaker(db)
# open an actual session by calling Session()
session = Session()


# creating the database using declarative base subclass
base.metadata.create_all(db)


# creating records of visited countries
sweden = VisitedCountries(
    country_name="Sweden",
    country_capital="Stockholm",
    language="Swedish",
    flagcolors="Yellow and blue",
    whats_good="Kanelbulle",
    size='big'
)

denmark = VisitedCountries(
    country_name="Denmark",
    country_capital="Copenhagen",
    language="Danish",
    flagcolors="Red and White",
    whats_good="Lego",
    size="big"
)

france = VisitedCountries(
    country_name="France",
    country_capital="Paris",
    language="French",
    flagcolors="Red, White and Blue",
    whats_good="Croissant",
    size="big"
)

italy = VisitedCountries(
    country_name="Italy",
    country_capital="Rome",
    language="Italian",
    flagcolors="Green, White and Red",
    whats_good="Pizza",
    size="big"
)

switzerland = VisitedCountries(
    country_name="Switzerland",
    country_capital="Bern",
    language="Italian",
    flagcolors="Red and White",
    whats_good="Chocolate",
    size="big"
)

spain = VisitedCountries(
    country_name="Spain",
    country_capital="Madrid",
    language="Spanish",
    flagcolors="Red and Yellow",
    whats_good="Siesta",
    size="big"
)

# add instance to our session
session.add(sweden)
session.add(italy)
session.add(spain)
session.add(france)
session.add(denmark)
session.add(switzerland)

# creating records
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     natiionality="Bristish",
#     famous_for="First Programmer"
# )

# alan_turning = Programmer(
#     first_name="Alan",
#     last_name="Turning",
#     gender="M",
#     natiionality="Bristish",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     natiionality="American",
#     famous_for="COBOL langauge"
# )

# margaret_hamilton = Programmer(
#     first_name="Margret",
#     last_name="hamilton",
#     gender="F",
#     natiionality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     natiionality="American",
#     famous_for="Microsoft",
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     natiionality="British",
#     famous_for="world wide web",
# )


# add instance to our session
# session.add(ada_lovelace)
# session.add(alan_turning)
# session.add(tim_berners_lee)
# session.add(bill_gates)
# session.add(margaret_hamilton)
# session.add(grace_hopper)


# update a single record
# programmer = session.query(Programmer).filter_by(id=1).first()
# programmer.famous_for = "World President"


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == 'F':
#         person.gender = 'Female'
#     elif person.gender == 'M':
#         person.gender = 'Male'
#     else:
#         print('Gender not defined')
#     session.commit()


# deleting a single record
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# programmer = session.query(Programmer).filter_by(
# first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print(
# "Programmer Found: ", programmer.first_name + ' ' + programmer.last_name)
#     confirmation = input(
# 'Are you sure you want to delete this record? (y/n)')
#     if confirmation.lower() == 'y':
#         session.delete(programmer)
#         session.commit()
#         print('Programmer has been deleted')
#     else:
#         print('Programmer not deleted')
# else:
#     print('No records found')

# deleting all records
# countries = session.query(VisitedCountries)
# for country in countries:
#     session.delete(country)
# print('Table deleted')


# commit our session to database
session.commit()

# Q 1, find all programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + ' ' + programmer.last_name,
#         programmer.gender,
#         programmer.natiionality,
#         programmer.famous_for,
#         sep=" | "
#     )


# Q 2, find all countries
countries = session.query(VisitedCountries)
for country in countries:
    print(
        country.id,
        country.country_name,
        country.country_capital,
        country.language,
        country.flagcolors,
        country.size,
        country.whats_good,
        sep=" | "
    )
