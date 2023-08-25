import sys 
import potato

arg = sys.argv 
def search_potao():
    searchbar = open('src/potato/searchbar.py')
    searchbar.opens_load_potatatos()
    search_potao()
print(arg)

def list_example():
   
    my_list = ["a string", "another string", "a third string"]

    var = my_list[1]
    another_var = my_list[0]

   
    new_string = f"Var is: '{var}'"
    print(new_string) 
def parse_arguments(args):
 list_= args[1]
 list_2 = args[2]
 list_all = f"{list_} {list_2}"
 return list_all
def create_potato():
    
    new_potato = createpotato.input_potato_info()
    createpotato.save_potato_to_file
 
def main(args):
    command = parse_arguments(args)
    if command == "create potato":
        create_potato()
    elif command == "load potatos":
        import json 

        with open('homework/potatoes.json') as json_file:
            data = json.load(json_file)
            print(data)

main(arg)


 