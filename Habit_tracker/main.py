import requests
from datetime import datetime

# https://pixe.la/
# https://docs.pixe.la/

#===============================================================================
# user defined variables !!
# dont forget to adjust them !!
PIXELA_API_SELF_MADE_TOKEN = 'Sdfagda2423262246afaaw42'
PIXELA_API_SELF_MADE_USER_NAME = 'bobi-the-tester1'
PIXELA_API_SELF_MADE_GRAPH_NAME = 'graph1'
#===============================================================================

# ===== 1. CREATE A USER =========
PIXELA_API_END_POINT = 'https://pixe.la/v1/users'

PIXELA_API_PARAMS = {
    'token': PIXELA_API_SELF_MADE_TOKEN,
    'username': PIXELA_API_SELF_MADE_USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# creating a user
# response = requests.post(url=PIXELA_API_END_POINT, json=PIXELA_API_PARAMS)
# print(response.text)

# ===== 2. CREATE A graph =========
# creating a graph
PIXELA_API_GRAPH_END_POINT = f"{PIXELA_API_END_POINT}/{PIXELA_API_SELF_MADE_USER_NAME}/graphs"

PIXELA_API_GRAPH_CONFIGURATION_PARAMS = {
    'id': PIXELA_API_SELF_MADE_GRAPH_NAME,
    'name': 'Study time',
    'unit': 'Min',
    'type': 'float',
    'color':'sora', # blue
}

PIXELA_API_HEADERS = {
    'X-USER-TOKEN': PIXELA_API_SELF_MADE_TOKEN,
}

# creating a graph
# response = requests.post(url=PIXELA_API_GRAPH_END_POINT, 
#                         json=PIXELA_API_GRAPH_CONFIGURATION_PARAMS,
#                         headers=PIXELA_API_HEADERS)
# print(response.text)



# ===== 3. Get the graph =========
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph.html
# ! This is also /v1/users/<username>/graphs/<graphID> API.
graph_url = f"https://pixe.la/v1/users/{PIXELA_API_SELF_MADE_USER_NAME}/graphs/{PIXELA_API_SELF_MADE_GRAPH_NAME}.html"
print(graph_url)


# =========== 4. Post value to the graph ============
# post value to the graph
PIXELA_API_ADD_PIXEL_END_POINT = f'{PIXELA_API_END_POINT}/{PIXELA_API_SELF_MADE_USER_NAME}/graphs/{PIXELA_API_SELF_MADE_GRAPH_NAME}'

# formating date automaticaly using datetime modul from python
# aim to get the format '20220810' - so yyyyMMdd
current_day = datetime.now()
any_radom_day = datetime(year=2022, month=8, day=11)
print(current_day.strftime("%Y%m%d"))


PIXELA_API_ADD_PIXEL_PARAMS = {
    'date': current_day.strftime("%Y%m%d"),
    'quantity': '1560.25',
}

PIXELA_API_HEADERS = {
    'X-USER-TOKEN': PIXELA_API_SELF_MADE_TOKEN,
}

# respons = requests.post(url=PIXELA_API_ADD_PIXEL_END_POINT, 
#                        json=PIXELA_API_ADD_PIXEL_PARAMS,
#                        headers=PIXELA_API_HEADERS)
# print(respons.text)


# ===== 5. Get the graph - Browse again! - check =========
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph.html
# ! This is also /v1/users/<username>/graphs/<graphID> API.
graph_url = f"https://pixe.la/v1/users/{PIXELA_API_SELF_MADE_USER_NAME}/graphs/{PIXELA_API_SELF_MADE_GRAPH_NAME}.html"
print(graph_url)


#===== 6.1. Updating a pixel ====================
# updating a pixel

# format
date_to_update = datetime(year=2022, month=8, day=11).strftime("%Y%m%d")

PIXELA_API_ADD_PIXEL_END_POINT = f'{PIXELA_API_END_POINT}/{PIXELA_API_SELF_MADE_USER_NAME}/graphs/{PIXELA_API_SELF_MADE_GRAPH_NAME}/{date_to_update}'

PIXELA_API_UPDATE_PIXEL_PARAMS = {
    'quantity': '760.25',
}

PIXELA_API_HEADERS = {
    'X-USER-TOKEN': PIXELA_API_SELF_MADE_TOKEN,
}

# responde = requests.put(url=PIXELA_API_ADD_PIXEL_END_POINT,
#                         json=PIXELA_API_UPDATE_PIXEL_PARAMS,
#                         headers=PIXELA_API_HEADERS)

# print(responde.text)


#===== 6.2. Delete a pixel ====================
# deleting a pixel from the given date
# format
date_to_update = datetime(year=2022, month=8, day=11).strftime("%Y%m%d")

PIXELA_API_DELETE_PIXEL_END_POINT = f'{PIXELA_API_END_POINT}/{PIXELA_API_SELF_MADE_USER_NAME}/graphs/{PIXELA_API_SELF_MADE_GRAPH_NAME}/{date_to_update}'

PIXELA_API_HEADERS = {
    'X-USER-TOKEN': PIXELA_API_SELF_MADE_TOKEN,
}

# responde = requests.delete(url=PIXELA_API_DELETE_PIXEL_END_POINT,
#                         headers=PIXELA_API_HEADERS)

# print(responde.text)