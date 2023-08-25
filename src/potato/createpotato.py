
import json

def handle_float_input(key: str):
    while True:
        input_data = input(f"enter the {key}: ")

        try:
            return float(input_data)
        
        except ValueError as error:
            print(error)
            print(f"{key} should be a number, you entered: {input_data}. Try again >:(")

        except Exception as error:
            print("Something really bad happend, stopping program")
            raise error

# asks the user for potate info and makes a potato
def input_potato_info():
    new_potato = {}

    name = input("enter potato name:")
    new_potato["name"] = name

    size = handle_float_input("size")
    new_potato["size"] = size

    shape = input("potato shape: ")
    new_potato["shape"] = shape

    surface_area = handle_float_input("surface_area")
    new_potato["surface_area"] = surface_area

    density = handle_float_input("density")
    new_potato["density"] = density

    bulk_density = handle_float_input("bulk_density")
    new_potato["bulk_density"] = bulk_density
    return new_potato

# loads all potatoes from a file
def load_potatoes_from_file():
    with open('homework/potatoes.json') as json_file:
        data = json.load(json_file)
        return data
    
def save_potato_to_file(potato):
    potato_file = load_potatoes_from_file()
    potato_file["potatoes"].append(potato)

    with open('recources/potatos.json', 'w') as outfile:
        json.dump(potato_file, outfile, indent=4)

if __name__ == "__main__":
    new_potato = input_potato_info()
    
    print("The new potato is: ")
    print(new_potato)

    print("Saving to file")
    save_potato_to_file(new_potato)
