import webapp2
import routes
import config

app = webapp2.WSGIApplication(config=config.webapp2_config)
routes.add_routes(app)
