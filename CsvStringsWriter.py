import csv


class CsvStringsWriter:
    def __init__(self, path):
        self.path = path

    def write(self, language, strings):
        with open(self.path, newline="\n", mode="w") as file:
            writer = csv.writer(file, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            self.__write_header(writer, language)

            for string in strings.items():
                writer.writerow(string)

    def __write_header(self, writer, language):
        writer.writerow(("", language))
