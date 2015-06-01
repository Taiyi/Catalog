from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Item, Base, User

engine = create_engine('sqlite:///catalog.db')
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


# Default User
User1 = User(name="John Doe", email="johndoe@gmail.com",
             picture='http://ia.media-imdb.com/images/M/MV5BMTk1MjM3NTU5M15BMl5BanBnXkFtZTcwMTMyMjAyMg@@._V1_SY317_CR14,0,214,317_AL_.jpg')
session.add(User1)
session.commit()

# Desktop Items
category1 = Category(name="Desktops")

session.add(category1)
session.commit()

Item1 = Item(name="Standard Desktop",
             description="An everyday computer for the everyday man.",
             category=category1)

session.add(Item1)
session.commit()


Item2 = Item(name="Gaming Desktop",
             description="Slices through gigaflops like a knife through butter.",
             category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="Quantum Desktop",
             description="For experts only. Handle with extreme caution.",
             category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="Mini Desktop",
             description="Can run a webserver or something. Not for daily use.",
             category=category1)

session.add(Item4)
session.commit()

Item5 = Item(name="Black Desktop",
             description="This one is black.",
             category=category1)

session.add(Item5)
session.commit()


# Laptop Items
category2 = Category(name="Laptops")

session.add(category2)
session.commit()


Item1 = Item(name="Standard Laptop",
             description="Elegantly combines form and function.",
             category=category2)

session.add(Item1)
session.commit()

Item2 = Item(name="Gaming Laptop",
             description="Trades mobility for raw power.",
             category=category2)

session.add(Item2)
session.commit()

Item3 = Item(name="Durable Laptop",
             description="Waterproof and can survive six foot drops. But why?",
             category=category2)

session.add(Item3)
session.commit()

Item4 = Item(name="Fancy Laptop",
             description="Spend obscene amounts of money to impress other people with obscene amounts of money",
             category=category2)

session.add(Item4)
session.commit()

Item5 = Item(name="Ultrathin Laptop",
             description="Super portable. Take it to everywhere you want and some places you shouldn't.",
             category=category2)

session.add(Item5)
session.commit()


# Cellphone Items
category3 = Category(name="Cellphones")

session.add(category3)
session.commit()


Item1 = Item(name="Smartphone",
             description="The standard phone. Can make calls",
             category=category3)

session.add(Item1)
session.commit()

Item2 = Item(name="Thin Smartphone",
             description="Bending it voids the warranty",
             category=category3)

session.add(Item2)
session.commit()

Item3 = Item(name="Quality Smartphone",
             description="Vibrant colors, powerful processor, and long battery life. What else do you need?",
             category=category3)

session.add(Item3)
session.commit()

Item4 = Item(name="Flip Phone",
             description="A fossil. Can only make calls",
             category=category3)

session.add(Item4)
session.commit()

Item5 = Item(name="Brick",
             description="Literally a brick. But cheap.",
             category=category3)

session.add(Item5)
session.commit()


# Gaming Items
category4 = Category(name="Gaming Devices")

session.add(category4)
session.commit()


Item1 = Item(name="Game Console",
             description="Plays games on the television.",
             category=category4)

session.add(Item1)
session.commit()

Item2 = Item(name="Other Game Console",
             description="Also plays games on the television. But rabid fans will insist that this one is better",
             category=category4)

session.add(Item2)
session.commit()

Item3 = Item(name="High-End Game Console",
             description="Graphics out of the wazoo. Yet no games.",
             category=category4)

session.add(Item3)
session.commit()

Item4 = Item(name="Handheld System",
             description="Plays games on the go and on the can.",
             category=category4)

session.add(Item4)
session.commit()

Item5 = Item(name="Other Handheld System",
             description="Inexplicably has five screens and three analog sticks.",
             category=category4) 

session.add(Item5)
session.commit()


# Printing Items
category5 = Category(name="Printers")

session.add(category5)
session.commit()


Item1 = Item(name="Laser Printer",
             description="Not as interesting as its name.",
             category=category5) 

session.add(Item1)
session.commit()

Item2 = Item(name="Combo Printer",
             description="Built in scanner, copier, and faxer. What can't it do?",
             category=category5) 

session.add(Item2)
session.commit()

Item3 = Item(name="Dot-Matrix Printer",
             description="Wake up Neo. The Matrix has you.",
             category=category5) 

session.add(Item3)
session.commit()

Item4 = Item(name="3D Printer",
             description="Now you can finally pirate a car.",
             category=category5) 

session.add(Item4)
session.commit()


# Headphone Items
category6 = Category(name="Headphones")

session.add(category6)
session.commit()


Item1 = Item(name="Cheap Headphones",
             description="Cheap and durable.",
             category=category6) 

session.add(Item1)
session.commit()

Item2 = Item(name="Quality Headphones",
             description="The thinking man's choice.",
             category=category6) 

session.add(Item2)
session.commit()

Item3 = Item(name="Designer Headphones",
             description="More of a fashion statement than a sound delivery system.",
             category=category6) 

session.add(Item3)
session.commit()

Item4 = Item(name="Noise Cancelling Headphones",
             description="What did you just say?",
             category=category6) 

session.add(Item4)
session.commit()

Item5 = Item(name="Earbuds",
             description="Compact and portable. But will always tangle.",
             category=category6) 

session.add(Item5)
session.commit()


# Keyboard Items
category7= Category(name="Keyboards")

session.add(category7)
session.commit()

Item1 = Item(name="Standard Keyboard",
             description="An ordinary reliable keyboard.",
             category=category7) 

session.add(Item1)
session.commit()

Item2 = Item(name="Mechanical Keyboard",
             description="The clicking sensation calms the fingertips and drives all nearby people mad.",
             category=category7) 

session.add(Item2)
session.commit()

Item3 = Item(name="Wireless Keyboard",
             description="Be free of your mortal chains.",
             category=category7) 

session.add(Item3)
session.commit()

Item4 = Item(name="Multimedia Keyboard",
             description="Has several buttons whose purpose no one is sure of.",
             category=category7) 

session.add(Item4)
session.commit()

Item5 = Item(name="Dvorchak Keyboard",
             description="Gain incredible typing speed and accuracy at the cost of your eternal soul.",
             category=category7) 

session.add(Item4)
session.commit()


# Mouse Items
category8= Category(name="Mice")

session.add(category8)
session.commit()

Item1 = Item(name="Standard Mouse",
             description="Not so much of a standard as it is a classic.",
             category=category8) 

session.add(Item1)
session.commit()

Item2 = Item(name="Wireless Mouse",
             description="The hassle of replacing batteries is usually worth the convience of no more tangles. Usually.",
             category=category8) 

session.add(Item2)
session.commit()


Item3 = Item(name="Gaming Mouse",
             description="Enough buttons and macros to make a grown man cry.",
             category=category8) 

session.add(Item3)
session.commit()

Item4 = Item(name="Sleek Mouse",
             description="Everything the body wants but nothing the body needs.",
             category=category8) 

session.add(Item4)
session.commit()


Item5 = Item(name="Trackball Mouse",
             description="For the self-hating. A punishment worse than death.",
             category=category8) 

session.add(Item5)
session.commit()


print "Filled Catalog!"

