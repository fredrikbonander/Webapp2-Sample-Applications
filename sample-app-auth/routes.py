from webapp2_extras.routes import RedirectRoute
from web.handlers import LoginHandler
from web.handlers import LogoutHandler
from web.handlers import SecureRequestHandler
from web.handlers import CreateUserHandler

# Using redirect route instead of simple routes since it supports strict_slash
# Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
# RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute

_routes = [
    RedirectRoute('/login/', LoginHandler, name='login', strict_slash=True),
    RedirectRoute('/logout/', LogoutHandler, name='logout', strict_slash=True),
    RedirectRoute('/secure/', SecureRequestHandler, name='secure', strict_slash=True),
    RedirectRoute('/', CreateUserHandler, name='create-user', strict_slash=True)
]

def get_routes():
    return _routes

def add_routes(app):
    for r in _routes:
        app.router.add(r)
