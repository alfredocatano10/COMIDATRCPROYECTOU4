from django.test import SimpleTestCase

#PRUBA O TESTEO DE QUE EXISTE LA PAGINA HOME, OBTENIENDO UNA RESPUESTA (SI ES 200 ES EXITOSO, SI ES 400 ES MAL)
class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
