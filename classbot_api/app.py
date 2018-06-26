from chalice import Chalice
from chalicelib import feedback_controller, fellows_controller, modules_controller,utils
import requests

app = Chalice(app_name='classbot_api')
app.debug = True



@app.route('/module/progress', methods=['POST'], cors=True)
def fellow_modules():
   json_body = app.current_request.json_body
   return modules_controller.get_module_fellows(json_body["module_id"])

@app.route('/modules', methods=['GET'], cors=True)
def modules():
   return modules_controller.get_all_modules()

@app.route('/fellow/{email}', methods=['GET'],cors=True)
def get_fellow_by_email(email):
    return fellows_controller.get_fellow(email)

@app.route('/fellows', methods=['GET'],cors=True)
def get_fellows():
    return fellows_controller.get_all_fellows()

