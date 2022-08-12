# populating questions data from the API - open trivia database
import requests

BASE_API_OPENTDB_END_POINT = "https://opentdb.com/api.php"
# https://opentdb.com/api.php?amount=10&type=boolean
parameters_opentdb = {
    "amount": 10,
    "type": "boolean",
}

request = requests.get(url=BASE_API_OPENTDB_END_POINT, params=parameters_opentdb)
request.raise_for_status() # check if an error occured

question_data =  request.json()['results']