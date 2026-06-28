import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random student identifier.

    Creates and returns a string composed of fifteen randomly
    selected lowercase alphabetic characters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represent a student with automatically generated credentials.

    Stores basic student information and derives additional
    attributes such as a login name and a unique identifier
    during object initialization.
    """
    # Attributes Declaration
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Initialize derived student attributes after object creation.

        Generates the student's login from the provided name and
        surname and assigns a unique random identifier.
        """
        self.login = self.name[0] + self.surname.lower()
        self.id = generate_id()


# 'login' and 'id' are marked with 'init=False' because they are
# not supplied by the user during object creation. Their values
# are derived automatically after the dataclass has initialized
# the user-provided attributes.

# Dataclasses call '__post_init__()' immediately after the
# generated '__init__()' method finishes. At this point,
# 'name' and 'surname' already exist and can safely be used
# to compute dependent attributes such as 'login'.

# A 'default_factory' cannot be used for 'login' because its
# value depends on instance attributes. The object must exist
# before those attributes can be accessed.

# The student identifier is generated separately for each
# instance to ensure that every student receives a unique id.
