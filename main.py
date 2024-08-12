import requests
from datetime import datetime


pixela_endpoint="https://pixe.la/v1/users"
USERNAME="pooji02"
PASSWORD="habit_tracker0"
parameters={
    "token":PASSWORD,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)
graph_id="walk12345"
graph_parameters={
    "id":graph_id,
    "name":"Study tracker",
    "unit":"hours",
    "type":"float",
    "color":"kuro",
}
headers={
    "X-USER-TOKEN":PASSWORD,
}
# response=requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs",json=graph_parameters,headers=headers)
# print(response.text)
date=datetime.now()

pixel_parameters={
    "date":date.strftime("%Y%m%d"),
    "quantity":input("enter the hours u studied?"),

}
response=requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}",json=pixel_parameters,headers=headers)
print(response.text)