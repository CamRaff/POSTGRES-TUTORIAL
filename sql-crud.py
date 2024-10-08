from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions fromt the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famours_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famours_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famours_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famours_for = "COBOL Language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famours_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famours_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famours_for = "World Wide Web"
)

cameron_rafferty = Programmer(
    first_name = "Cameron",
    last_name = "Rafferty",
    gender = "M",
    nationality = "British",
    famours_for = "Being a cool dude"
)

# add each instance of our programmers to our session
session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)
session.add(cameron_rafferty)


# commit our session to the database
session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=12).first()
# programmer.famours_for = "World President"


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not specified")
#     session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name, programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (yes/no): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("Programmer not found")


# deleting multiple records
# programmers =  session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id, 
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famours_for,
        sep=" | "
    )

