import webapp2
import config
import routes

from tests import test_base

app = webapp2.WSGIApplication(routes.get_routes(), config=config.webapp2_config)

class TestAuthHandler(test_base.BaseTestCase):
    def tearDown(self):
        super(TestAuthHandler, self).tearDown()
        app.error_handlers = {}

    def test_redirect_if_no_session(self):
        rsp = app.get_response('/secure/')
        self.assertEqual(rsp.status_int, 302)

    def test_create_user_and_login(self):
        req = webapp2.Request.blank('/', POST={'username': 'hello', 'password': 'earth'},
            headers=[('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8')])
        req.app = app
        rsp = req.get_response(app)
        self.assertEqual(rsp.status_int, 302)

        rsp = app.get_response('/login/', POST={'username': 'hello', 'password': 'earth'},
            headers=[('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8')])
        self.assertEqual(rsp.status_int, 302)