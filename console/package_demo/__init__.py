from .we import we
from .are import are
from .package import package

def we_are_package():
    """Prints and returns 'we are package'"""
    outbound = we() + are() + package()
    print(outbound)

def uwu_at_user():
    """Greets user on package import"""
    print("Hello and thank you for importing me! uwu")

if __name__ == "__main__":
    we_are_package()

uwu_at_user()
