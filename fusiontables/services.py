#DOCS: https://developers.google.com/resources/api-libraries/documentation/fusiontables/v1/python/latest/index.html

class FusionTableService:
    TABLE_ID = '1hIFxlOCg1zPTwrc9Mgo0-q5__PnmLdcVnDnGLYRW'

    def __init__(self, google_service):
        self.service = google_service

    def save_location(self, location):
        sql = "INSERT INTO {} (Address, Location) VALUES ('{}', '{},{}')".\
            format(self.TABLE_ID, location['address'], location['lat'], location['lon'])

        return self.service.query().sql(sql=sql).execute()

    def clear_table(self):
        sql = "DELETE FROM {}".format(self.TABLE_ID)

        return self.service.query().sql(sql=sql).execute()