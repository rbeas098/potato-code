import json


def load_potatos_from_file():
    with open('recources/potatos.json') as json_file:
        data = json.load(json_file)
        potatos = data["potatos"] 
        return potatos 

def get_potato_name(): 
    name = input("potato name: ") 
    return name
  
def return_potato_by_name(potatos, name):
  for potato in potatos:
       if name == potato["name"]:
        return potato 
       
  raise Exception("potao couldn't be found check spelling or try again!")