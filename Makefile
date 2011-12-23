FLAGS= --datastore_path=./db
PORT=   8080
ADDRESS=localhost
DEV_APPSERVER=python /usr/local/google_appengine/dev_appserver.py

serve-sample-auth:
	$(DEV_APPSERVER) sample-app-auth/ --port $(PORT) --address $(ADDRESS) $(FLAGS)
