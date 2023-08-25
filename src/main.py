import sys 
from potato.searchbar import load_potatos_from_file, get_potato_name, return_potato_by_name

'''
Run me with this

python3 src/main.py search potato
python3 src/main.py create potato
python3 src/main.py load potatos
'''

arg = sys.argv 
def search_potato():
    potatos = load_potatos_from_file()
    name = get_potato_name()
    potato = return_potato_by_name(potatos,name)
    return potato

def parse_arguments(args):
 list_= args[1]
 list_2 = args[2]
 list_all = f"{list_} {list_2}"
 return list_all

def create_potato():
  raise Exception("not implemented yet")
 
def main(args):
    command = parse_arguments(args)
    if command == "create potato":
        create_potato()
    elif command == "load potatos":
        list_all = load_potatos_from_file()
        print(list_all)
    elif command == "search potato":
        potato = search_potato()
        print(potato)


        
main(arg)


 