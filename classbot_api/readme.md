# Dashboard_api 
This part of the project presents the API consumed by the dashboard.

### Tech
This project uses the following technologies:
* [Python] - backend programming language
* [DynamoDB]- NoSQL cloud database service 
* [Chalice]- python serverless microframework for AWS.

### deploy project
> Configuration file must be updated
```python
CLASSBOT_FELLOWS_URL = 'FELLOWS_DATA _URL'
CLASSBOT_MODULES_URL = 'MODULES_DATA_URL'
CLASS_BOT_TOKEN = 'AUTHORIZATION_TOKEN' 
```

Then run command: 
```
$ chalice deploy
```
```
> our credentials must be updated before running chalice deploy
   