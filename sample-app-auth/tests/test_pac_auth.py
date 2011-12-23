import config
import routes
import webapp2
from tests import test_base
from webapp2_extras import auth

app = webapp2.WSGIApplication(config=config.webapp2_config)
routes.add_routes(app)

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