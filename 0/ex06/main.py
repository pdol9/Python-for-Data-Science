nums = [1,2,3,4,5]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # [2, 4]

words = ["a", "", "b", ""]
nonempty = filter(None, words)
print(list(nonempty))  # ['a', 'b']

def is_alpha(s):
    return s.isalpha()

items = ["abc","123","a1"]
print(list(filter(is_alpha, items)))  # ['abc']

print("Print filter ___doc___ :")
print(filter.__doc__)

def test():
    """ This is a simple description of a function and doc feature! """

print("Print test function ___doc___ :")
print(test.__doc__)
