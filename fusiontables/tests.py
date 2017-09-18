from django.test import TestCase
from fusiontables.services import FusionTableService

class Test(TestCase):
    def test_google(self):
        service = FusionTableService()
        r = service.create_table('test', 'only a test')
        a = r        