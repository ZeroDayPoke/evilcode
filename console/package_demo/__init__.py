from .we import we
from .are import are
from .package import package

def we_are_package():
    """Prints and returns 'we are package'"""
    outbound = we() + are() + package()
    print(outbound)
