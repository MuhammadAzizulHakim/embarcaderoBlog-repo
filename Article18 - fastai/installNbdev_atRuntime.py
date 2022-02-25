import pip
import importlib

def import_with_auto_install(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
    return importlib.import_module(package)

# Example
if __name__ == '__main__':
    nbdev = import_with_auto_install('nbdev')
    print(nbdev)