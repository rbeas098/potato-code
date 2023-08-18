import json
def opens_load_potatatos():
     open('Load.json')
     with open('Load.json') as json_file:
       data = json.load(json_file)
       
def get_potato(data, json_file): 
    potatos = json_file["potatos"] 
    name = input("potato name: ") 
    for potato in potatos:
     if name == "name":
        return potato 
     else:
        print("this potato dose not exist try again!")