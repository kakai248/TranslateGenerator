import csv
from collections import OrderedDict


class CsvStringsReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, newline="\n", mode="r") as file:
            reader = csv.reader(file, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            lines = list(reader)

            languages = self.__read_header(lines[0])

            for row in lines[1:]:
                label = row[0]

                for i, string in enumerate(row[1:]):
                    languages[list(languages.keys())[i]][label] = string

            return languages

    def __read_header(self, row):
        languages = OrderedDict()
        for language in row[1:]:
            languages[language] = OrderedDict()
        return languages
