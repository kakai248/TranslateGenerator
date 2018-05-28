import pathlib


class AndroidStringsWriter:
    LANGUAGE_DIR = 'values-'
    LANGUAGE_FILE = 'strings.xml'

    def __init__(self, path):
        self.path = path
        self.basePath = pathlib.Path(self.path)

    def write(self, languages):
        for language, strings in languages.items():
            language_dir_path = self.basePath.joinpath(AndroidStringsWriter.LANGUAGE_DIR + language)
            language_dir_path.mkdir(parents=True, exist_ok=True)

            language_file_path = language_dir_path.joinpath(AndroidStringsWriter.LANGUAGE_FILE)

            with open(language_file_path, newline="\n", mode="w") as file:
                file.write("<resources>\n")

                for s in strings.items():
                    file.write("    <string name=\"%s\">%s</string>\n" % (s[0], s[1]))

                file.write("</resources>\n")
