import os, json


def opens_load_potatatos():
     open('recources/potatos.json')
     with open('recources/potatos.json') as json_file:
       data = json.load(json_file)
opens_load_potatatos()    
def get_potato(data, json_file, key): 
    potatos = json_file["potatos"] 
    name = input("potato name: ") 
    for potato in potatos:
       if name == potato["name"]:
        return potato 
       else:
         print("this potato dose not exist try again!")
    get_potato()