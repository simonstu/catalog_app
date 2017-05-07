from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog_database.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Cata Log", email="cata@log.com")
session.add(User1)
session.commit()

# Category Soccer
cat1 = Category(user_id=1, name="Soccer")

session.add(cat1)
session.commit()

item1 = Item(user_id=1,
             name="Great Ball",
             description="This is a great ball",
             category=cat1)

session.add(item1)
session.commit()

item2 = Item(user_id=1,
             name="Ball",
             description="This is a ball",
             category=cat1)

session.add(item2)
session.commit()

item3 = Item(user_id=1,
             name="Goal",
             description="This is a goal",
             category=cat1)

session.add(item3)
session.commit()


# Category Basketball
cat2 = Category(user_id=1, name="Basketball")

session.add(cat2)
session.commit()

item1 = Item(user_id=1,
             name="Great Basketball",
             description="This is a great Basketball",
             category=cat2)

session.add(item1)
session.commit()

item2 = Item(user_id=1,
             name="Basketball",
             description="This is a Basketball",
             category=cat2)

session.add(item2)
session.commit()

item3 = Item(user_id=1,
             name="Basket",
             description="This is a basket",
             category=cat2)

session.add(item3)
session.commit()


# Category Basketball
cat2 = Category(user_id=1, name="Frisbee")

session.add(cat2)
session.commit()

item1 = Item(user_id=1,
             name="Great Frisbee",
             description="This is a great Frisbee",
             category=cat2)

session.add(item1)
session.commit()

item2 = Item(user_id=1,
             name="Frisbee",
             description="This is a Frisbee",
             category=cat2)

session.add(item2)
session.commit()

item3 = Item(user_id=1,
             name="Another Frisbee",
             description="This is another Frisbee",
             category=cat2)

session.add(item3)
session.commit()

print "added some categories and items!"
