# 'https://api.ipify.org?format=json'

# import frappe
# # from dotenv import dotenv_values
# # import os
# # import time
# import requests
# import pycountry
# # import json
# # api_url = "https://jsonplaceholder.typicode.com/todos/1"
# # response = requests.get(api_url)
# # response.json()

# @frappe.whitelist(allow_guest=True)
# def client():
#     try:
#         api_url = 'https://api.ipify.org?format=json'
#         response = requests.get(api_url)
#         json_response = response.json()
#         pairs = json_response .items()
#         for key, value in pairs:
#             str_ip = value
#         url_country = requests.get("https://ip-api.com/json/str_ip").json()

#         # headers = {
#         #     "X-RapidAPI-Host": "ip-geolocation-and-threat-detection.p.rapidapi.com",
#         #     "X-RapidAPI-Key": "3912149b58msh765147a63610416p1f51dbjsn0bde5af0e51e"
#         # }

#         # v_response = requests.get(url_country)
#         # jt_response = v_response.json()
        
#         # tr_response = DbIpCity.get(str_ip, api_key='free')
        
#     except Exception as error:
#         frappe.clear_messages()
#         frappe.local.response["success"] = False
#         frappe.local.response["error"] = error
#         return

#     frappe.response["success"] = True
#     frappe.response["site"] =  url_country



from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))