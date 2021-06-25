from django.test import SimpleTestCase

#--------------------------------------------------------------------
# PRUEBA QUE TESTEA EL ESTADO DE LA RESPUESTA DE LA PAGINA PRINCIPAL
#--------------------------------------------------------------------

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)