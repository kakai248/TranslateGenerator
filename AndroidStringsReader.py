import re
from collections import OrderedDict


class AndroidStringsReader:
    REGEX = r'\s*<string name=\"(\w+)\"[^>]*>(.*)</string>.*$'
    TRANSLATABLE_REGEX = r'.*?translatable=\"(true|false)\".*$'

    def __init__(self, path):
        self.path = path
        self.regex = re.compile(AndroidStringsReader.REGEX)
        self.translatable_regex = re.compile(AndroidStringsReader.TRANSLATABLE_REGEX)

    def read(self):
        strings = OrderedDict()
        with open(self.path, newline="\n", mode="r") as file:
            for line in file.readlines():
                parsed_line = self.__parse_line(line)
                if parsed_line is not None:
                    strings[parsed_line[0]] = parsed_line[1]

        return strings

    def __parse_line(self, line):
        matcher = self.regex.match(line)
        if matcher:
            translatable_matcher = self.translatable_regex.match(line)
            if translatable_matcher:
                translatable = translatable_matcher.group(1)
                if translatable == 'false':
                    return None

            return [matcher.group(1), matcher.group(2)]
        return None
