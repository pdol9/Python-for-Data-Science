def all_thing_is_obj(object: any) -> int:
    if type(object) is str:
        print(object + " is in the kitchen : " + str(str))
    elif type(object) is list:
        print("List : " + str(list))
    elif type(object) is tuple:
        print("Tuple : " + str(tuple))
    elif type(object) is set:
        print("Set : " + str(set))
    elif type(object) is dict:
        print("Dict : " + str(dict))
    else:
        print("Type not found")
    return 42

#    elif type(object) is None:
