
from chalicelib import database_manager, config, utils
from chalice import BadRequestError
import requests


def get_all_modules():
    return utils.do_get_request(config.CLASSBOT_MODULES_URL, {'Authorization': config.CLASS_BOT_TOKEN})

def get_module_name(classroom_id):
    json_data = utils.do_get_request(config.CLASSBOT_MODULES_URL, {'Authorization': config.CLASS_BOT_TOKEN})
    for item in json_data : 
        if classroom_id == json_data[item]['ClassroomID'] :
            return item
    return None


def get_module_fellows(module_id):
    module_name = get_module_name(module_id)
    if not module_name : 
        raise BadRequestError('Module Not Found')
    json_data = utils.do_get_request(config.CLASSBOT_FELLOWS_URL, {
                                     'Authorization': config.CLASS_BOT_TOKEN})
    fellows = []
    for fellow in json_data:
        status = ''
        card = None
        progress = 0
      
        if module_name in json_data[fellow]["done"]:
            status = "finished"
            card = json_data[fellow]['done'][module_name]['card']
        elif module_name in json_data[fellow]["doingTech"]:
            status = "InProgress"
            card = json_data[fellow]['doingTech'][module_name]['card']
        elif module_name in json_data[fellow]["doingExcellence"]:
            status = "InProgress"
            card = json_data[fellow]['doingExcellence'][module_name]['card']
        if card:
            if card['badges']['checkItems'] != 0 :
                progress = (card['badges']['checkItemsChecked'] / card['badges']['checkItems']) * 100
            fellows.append({
                'avatar': {'url': 'static/img/avatars/1.jpg', 'status': status},
                'fellow': {'name': fellow},
                'progress': {'value': progress },
                'Status': {'value': status},
                'Deadline': 'Undefined' if  not card['due'] or 'T' not in card['due'] else  card['due'].split("T")[0] 
            })
    return fellows
