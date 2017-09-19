from sqlalchemy import Column, String, Integer
from zameen_scrape.database.connect import Base


class ScrapedData(Base):
    __tablename__ = 'zameen'

    price = Column(Integer, primary_key=True)
    address = Column(String(1000))
    beds = Column(Integer)
    title = Column(String(1000))
    area = Column(String(300))
    phone = Column(Integer)
    posted_on = Column(String(500))
    category = Column(String)

    def __init__(self, price, address, bedrooms, title, area, phone, posted_on, category):
        self.price = price
        self.title = title
        self.address = address
        self.bedrooms = bedrooms
        self.area = area
        self.phone = phone
        self.posted_on = posted_on
        self.category = category

    def __repr__(self):
        return "<Zameen: price='%s', title='%s', address='%s', bedrooms='%d', area='%s', phone='%s', posted_on='%s', " \
               "category='%d'>" % (self.price, self.title, self.address, self.bedrooms, self.area, self.phone,
                                   self.posted_on, self.category)
