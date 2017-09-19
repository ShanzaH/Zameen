from zameen_scrape.database.connect import db
from zameen_scrape.database.models import ScrapedData

class ZameenScrapePipeline(object):

    def process_item(self, item, zameenspider):

            record = ScrapedData(title=item['title'], address=item['address'], price=item['price'],
                                 category = item['category'], bedrooms=item['bedrooms'], phone=item['phone'],
                                 area=item['area'], posted_on = item['posted_on'])
            db.add(record)
            db.commit()
            return item



