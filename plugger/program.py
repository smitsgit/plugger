from stevedore.extension import ExtensionManager
from stevedore.driver import DriverManager


def main():
    extensions: ExtensionManager = DriverManager('pytimed', 'yaml', invoke_on_load=True)

    for ext in extensions:
        print(ext.obj)


if __name__ == '__main__':
    main()
