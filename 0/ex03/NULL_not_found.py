# Write a function that prints the object type of all types of "Null"
# Return 0 if it goes well and 1 in case of error.

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        # NaN is the only value not equal to itself: object != object
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
