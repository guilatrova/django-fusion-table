#DOCS: https://developers.google.com/resources/api-libraries/documentation/fusiontables/v1/python/latest/index.html

class FusionTableService:
    TABLE_NAME = 'Latrova_Sherpany_FTABLE'
    DEFAULT_DESCRIPTION = 'Guilherme Magalhães Latrova: https://github.com/guilatrova'

    def __init__(self, google_service):
        self.service = google_service

    def _create_table(self, name, description):
        body = {
            'name': name,
            'description': description,
            'isExportable': True,
            'columns': [
                {
                    'name': 'Address',
                    'type': 'STRING'
                },
                {
                    'name': 'Latitude',
                    'type': 'NUMBER'
                },
                {
                    'name': 'Longitude',
                    'type': 'NUMBER'
                }
            ]
        }

        return self.service.table().insert(body=body).execute()

    def retrieve_or_create_table():
        '''
        Returns the id of a table that matches default NAME. If it doesn't exists, 
        then creates one and returns id.
        '''
        result = self.service.table().list.execute()
        tables = result['items']
        table_id = next(table['tableId'] for table in tables if table['name'] == self.TABLE_NAME)
        if table_id is None:
            return self._create_table(self.TABLE_NAME, self.DEFAULT_DESCRIPTION)['tableId']

    def save_location(self, table_id, location):
        sql = "INSERT INTO {} (Address, Latitude, Longitude) VALUES ('{}', {}, {})".\
            format(table_id, location.address, location.lat, location.lon)

        return self.service.query().sql(sql=sql).execute()
