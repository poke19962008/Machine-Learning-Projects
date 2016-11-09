import re
def compileRe(pattern, dotall=True):
    flags = (re.MULTILINE | re.DOTALL) if dotall else re.MULTILINE
    return re.compile(pattern, flags)

'''
    py: 0-44
    c: 45-54
    cpp: 55-92
    java: 93-107
    rb: 108-115
'''

# tokenizer for source code
tokenizer = compileRe(r'[\w\']+|[\"\"!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~\"\"\\]')

# List of language based markers
markerList = [
    # PY markers
    compileRe(r'^(\s*from\s+[\.\w]+)?\s*import\s+[\*\.,\w]+(,\s*[\*\.,\w]+)*(\s+as\s+\w+)?$'),
    compileRe(r'^\s*def\s+\w+\((.*?):$', dotall=False),
    compileRe(r'^\s*if\s(.*?):$(.*?)(^\s*else:)?$', dotall=False),
    compileRe(r'^\s*if\s(.*?):$(.*?)(^\s*elif:)?$', dotall=False),
    compileRe(r'^\s*try:$(.*?)^\s*except(.*?):'),
    compileRe(r'True|False'),
    compileRe(r'==\s*(True|False)'),
    compileRe(r'is\s+(None|True|False)'),
    compileRe(r'^\s*if\s+(.*?)\s+in[^:\n]+:$', dotall=False),
    compileRe(r'^\s*pass$'),
    compileRe(r'print\((.*?)\)$', dotall=False),
    compileRe(r'^\s*for\s+\w+\s+in\s+(.*?):$'),
    compileRe(r'^\s*class\s+\w+\s*(\([.\w]+\))?:$', dotall=False),
    compileRe(r'^\s*@(staticmethod|classmethod|property)$'),
    compileRe(r'__repr__'),
    compileRe(r'"(.*?)"\s+%\s+(.*?)$', dotall=False),
    compileRe(r"'(.*?)'\s+%\s+(.*?)$", dotall=False),
    compileRe(r'^\s*raise\s+\w+Error(.*?)$'),
    compileRe(r'"""(.*?)"""'),
    compileRe(r"'''(.*?)'''"),
    compileRe(r'\s*# (.*?)$'),
    compileRe(r'^\s*import re$'),
    compileRe(r're\.\w+'),
    compileRe(r'^\s*import time$'),
    compileRe(r'time\.\w+'),
    compileRe(r'^\s*import datetime$'),
    compileRe(r'datetime\.\w+'),
    compileRe(r'^\s*import random$'),
    compileRe(r'random\.\w+'),
    compileRe(r'^\s*import math$'),
    compileRe(r'math\.\w+'),
    compileRe(r'^\s*import os$'),
    compileRe(r'os\.\w+'),
    compileRe(r'^\s*import os.path$'),
    compileRe(r'os\.path\.\w+'),
    compileRe(r'^\s*import sys$'),
    compileRe(r'sys\.\w+'),
    compileRe(r'^\s*import argparse$'),
    compileRe(r'argparse\.\w+'),
    compileRe(r'^\s*import subprocess$'),
    compileRe(r'subprocess\.\w+'),
    compileRe(r'^\s*if\s+__name__\s*=\s*"__main__"\s*:$'),
    compileRe(r"^\s*if\s+__name__\s*=\s*'__main__'\s*:$"),
    compileRe(r'self\.\w+(\.\w+)*\((.*?)\)'),

    # C marker.
    compileRe(r'^\s*#\s*include\s+("|<)[^">]+("|>)$'),
    compileRe(r'^\s*#\s*include\s+<[^\.>]+>$'),
    compileRe(r'^\s*#\s*ifn?def\s+\w+$'),
    compileRe(r'^\s*#\s*if\s+(.*?)$'),
    compileRe(r'^\s*#\s*if\s+defined\((.*?)$'),
    compileRe(r'^\s*#\s*define \w+(.*?)$'),
    compileRe(r'^\s*#\s*endif$'),
    compileRe(r'^\s*#\s*undef\s+\w+$'),
    compileRe(r'^\s*#\s*else$'),
    compileRe(r'^\s*#\s*pragma(.*?)$'),

    # CPP marker
    compileRe(r'^\s*template\s*<[^>]>$'),
    compileRe(r'size_t'),
    compileRe(r'\w*\s*::\s*\w+'),
    compileRe(r'\w+\s*::\s*\w+\((.*?)\);'),
    compileRe(r'\w+\s*::\s*\w+\([^\{]+\s*\{(.*?)\w+::\w+\('),
    compileRe(r'(std::)?cout\s*<<(.*?);'),
    compileRe(r'(std::)?cin\s*>>(.*?);'),
    compileRe(r'std::\w+'),
    compileRe(r'std::\w+\((.*?)\)'),

    compileRe(r'static_assert\((.*?);'),
    compileRe(r'static_cast<[^>]>'),
    compileRe(r'dynamic_cast<[^>]>'),
    compileRe(r'nullptr'),
    compileRe(r'//(.*?)$'),

    compileRe(r'switch\s*\((.*?)\);'),
    compileRe(r'&\(?\w+'),
    compileRe(r'\w+&'),
    compileRe(r'\s[A-Z0-9_]+\((.*?);'),

    compileRe(r'\)\s*=\s*0;$'),
    compileRe(r'~\w+\((.*?)\}'),
    compileRe(r'^\s*public:(.*?)};'),
    compileRe(r'^\s*private:(.*?)};'),
    compileRe(r'^\s*protected:(.*?)};'),
    compileRe(r'\sm_\w+'),
    compileRe(r'return\s+(.*?);$'),

    compileRe(r'^\s*class\s*\w+\s*:\s*public\s+\w+\s*\{(.*?)\)'),
    compileRe(r'^\s*virtual\s+[^\(]+\((.*?)\)'),
    compileRe(r'^\w*struct\s*(\w+\s*)?{'),
    compileRe(r'\w+->\w+'),

    compileRe(r'^\s*namespace\s+\w+\s*\{(.*?)\};(.*?)$'),
    compileRe(r'const\s+static|static\s+const'),
    compileRe(r'typedef\s+(.*?)\s+\w+\s*;$'),
    compileRe(r'(i|u)(int)?\d+(_t)?'),
    compileRe(r'\*\w+->'),
    compileRe(r'(const\s+)?char\s*\*'),
    compileRe(r'int\s+\w+'),
    compileRe(r'void\s+\w+'),
    compileRe(r'auto'),

    # JAVA markers
    compileRe(r'\sstatic\s+final\s'),
    compileRe(r'(public|protected|private)\s+synchronized\s'),
    compileRe(r'synchronized\s*\([^\{]+\{(.*?)\}'),
    compileRe(r'ArrayList<[\.\w+]*>'),
    compileRe(r'HashMap<[\.\w+]*>'),
    compileRe(r'HashSet<[\.\w+]*>'),
    compileRe(r'System(\.\w+)+'),
    compileRe(r'new\s+\w+(.*?);'),
    compileRe(r'try\s*\{(.*?)catch[^\{]+\{'),
    compileRe(r'[Ll]ogg(ing|er)'),
    compileRe(r'^\s*package\s+\w+(\.\w+)*;$'),
    compileRe(r'^\s*import\s+\w+(\.\w+)*;$'),
    compileRe(r'(public|private|protected)\s+[^\{]*\{(.*?)\}$'),
    compileRe(r'@Override'),
    compileRe(r'throw new \w+\((.*?)\);\s*$'),

    # RB markers
    compileRe(r'^\s*def\s*[^:]+$(.*?)end$'),
    compileRe(r'@[\.:\w+]'),
    compileRe(r'\s:\w+'),
    compileRe(r'#\{(.*?)\}'),
    compileRe(r'^\s*include\s+[\.\w+]+$'),
    compileRe(r'^\s*alias\s[\.\w]+\s+[\.\w]+(.*?)$'),
    compileRe(r'^\s*class\s+[\.\w+]+(\s*<\s*[\.\w]+(::[\.\w]+)*)?(.*?)$'),
    compileRe(r'^\s*module\s+[\.\w+]+\s*[\.\w]+(::[\.\w]+)*(.*?)$')
]
