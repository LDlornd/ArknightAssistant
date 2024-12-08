import click
import json
import requests

from skyland import get_cred_by_token, init_token, get_binding_list, get_user_info, do_sign



token = init_token()
token = token[0]

cred = get_cred_by_token(token)

# do_sign(cred)

player_list = get_binding_list()

uid = player_list[-1]["uid"]

user_data = get_user_info(uid)

with open("data.json", "w") as f:
    json.dump(user_data, f, indent=4, ensure_ascii=False)