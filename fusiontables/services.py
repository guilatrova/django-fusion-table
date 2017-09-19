from djgmaps.settings import TABLE_ID

class FusionTableService:    
    '''
    Handles requests and queries to Fusion Tables API.
    Uses google api client, for more details check here:
    https://developers.google.com/resources/api-libraries/documentation/fusiontables/v1/python/latest/index.html/ 
    '''

    def __init__(self, google_service):
        self.service = google_service

    def save_location(self, location):
        sql = "INSERT INTO {} (Address, Location) VALUES ('{}', '{},{}')".\
            format(self.TABLE_ID, location['address'], location['lat'], location['lon'])

        return self.service.query().sql(sql=sql).execute()

    def clear_table(self):
        sql = "DELETE FROM {}".format(self.TABLE_ID)

        return self.service.query().sql(sql=sql).execute()