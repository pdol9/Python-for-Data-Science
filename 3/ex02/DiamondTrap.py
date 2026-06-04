from S1E7 import Baratheon, Lannister


"""
In a diamond inheritance hierarchy, the child class inherits attributes that
are initialized by its parent classes. When those inherited attributes are
later exposed through properties, care must be taken to avoid recursive access.

The recursion problem occurs when a property's getter or setter tries to access
or assign the same property name that triggered it. Since every access goes
through the property mechanism, the getter or setter repeatedly calls itself,
leading to infinite recursion and eventually a recursion error.

The purpose of using a property is to control access to an attribute while
preserving the appearance of normal attribute access. To avoid recursion,
the property must operate on the underlying stored value rather than invoking
the property again. In practice, this means the property's implementation must
bypass the property mechanism when reading or writing the actual data.

In this exercise, the properties are used to manage physical characteristics
inherited from the parent classes. They provide controlled access to those
inherited attributes while ensuring that updates modify the underlying values
directly instead of repeatedly triggering the property's own getter or setter.
This allows the child class to change inherited characteristics safely without
causing recursive calls.
"""


class King(Baratheon, Lannister):
    """This is a new false king."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.__dict__["eyes"]

    def set_eyes(self, value):
        self.__dict__["eyes"] = value

    eyes = property(get_eyes, set_eyes)

    def get_hairs(self):
        return self.__dict__["hairs"]

    def set_hairs(self, value):
        self.__dict__["hairs"] = value

    hairs = property(get_hairs, set_hairs)
