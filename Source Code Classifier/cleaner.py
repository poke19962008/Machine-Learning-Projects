import re

def clean(sc, ext):
    if ext == 'cpp':
        pattern = re.compile(
            r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        return re.sub(pattern, "", sc)


# if __name__ == '__main__':
