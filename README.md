## Dependencies

 - Docker

## Steps to run the project.

 - Build docker:
	 - `docker build -t pronto_city_service -f Dockerfile.development .`
 - Run docker:
	 -  `docker run  -it -v "$(pwd)":/opt/city-service:cached -p 5000:5000 pronto_city_service /bin/bash -l`
 - Start the app:
	 - `NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python app.py`
