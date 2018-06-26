
from chalicelib import database_manager, config, utils
import requests
from chalice import BadRequestError


def get_all_fellows():
    r = requests.get(config.CLASSBOT_FELLOWS_URL, headers={
                     'Authorization': config.CLASS_BOT_TOKEN})
    return r.json()

def get_fellow(email) :
    json_data = utils.do_get_request(config.CLASSBOT_FELLOWS_URL, {
                                    'Authorization': config.CLASS_BOT_TOKEN})
    for item in json_data:
        if email == json_data[item]['id']:
            return json_data[item]
    raise BadRequestError('Fellow not recognized')


