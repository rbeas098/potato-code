
import sys    

def parse_arguments(args):
    '''
    This function takes in a list of strings and returns a string that is the command to run
    '''
    list_= args[1]
    list_2 = args[2]
    list_all = f"{list_} {list_2}"

    return list_all

def main(args):
    command = parse_arguments(args)
    if command == "get potato":
        pass
    else:
      print("bad command")

main(sys.argv)
