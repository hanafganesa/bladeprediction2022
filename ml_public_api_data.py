import json
from urllib import response
import requests

url = 'http://1d36-34-86-206-143.ngrok.io/blade_predict'

# new
input_data_for_model = {
    'pcut_position' : -884745,
    'psvol_position' : 13251
}

# new
# input_data_for_model = {
#     'pcut_position' : -884606,
#     'psvol_position' : 11128
# }

# new
# input_data_for_model = {
#     'pcut_position' : -838818,
#     'psvol_position' : 35097
# }

# worn
# input_data_for_model = {
#     'pcut_position' : -837652,
#     'psvol_position' : 37043
# }

# worn
# input_data_for_model = {
#     'pcut_position' : -832132,
#     'psvol_position' : 45396
# }

# worn
# input_data_for_model = {
#     'pcut_position' : -784738,
#     'psvol_position' : 111366
# }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)