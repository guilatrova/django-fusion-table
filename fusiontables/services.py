class FusionTableService:
    def __init__(self, google_service):
        self.service = google_service

    def create_table(self, name, description):
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