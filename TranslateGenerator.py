import argparse
import sys

from AndroidStringsReader import AndroidStringsReader
from AndroidStringsWriter import AndroidStringsWriter
from CsvStringsReader import CsvStringsReader
from CsvStringsWriter import CsvStringsWriter

MODE_IMPORTER = "importer"
MODE_EXPORTER = "exporter"


def read_android_file(path):
    reader = AndroidStringsReader(path)
    return reader.read()


def write_android_file(path, languages):
    writer = AndroidStringsWriter(path)
    writer.write(languages)


def reader_csv_file(path):
    reader = CsvStringsReader(path)
    return reader.read()


def write_csv_file(path, language, strings):
    writer = CsvStringsWriter(path)
    writer.write(language, strings)


def importer(input, output, language):
    strings = read_android_file(input)
    write_csv_file(output, language, strings)


def exporter(input, output):
    csv_strings = reader_csv_file(input)
    write_android_file(output, csv_strings)


def main(argv):
    parser = argparse.ArgumentParser(prog=argv[0],
                                     description='Convert between CSV and Android/iOS translations files.')
    parser.add_argument('--mode', '-m', action='store', choices=[MODE_IMPORTER, MODE_EXPORTER],
                        help='The mode, either importer (Android/iOS to CSV) or exporter (CSV to Android/iOS)')
    parser.add_argument('--input', '-i', action='store')
    parser.add_argument('--output', '-o', action='store')
    parser.add_argument('--language', '-l', nargs='?', action='store', help='The language of the input')

    args = parser.parse_args(argv[1:])

    if args.mode == MODE_IMPORTER:
        if not args.language:
            raise argparse.ArgumentTypeError('Language is needed for importer mode.')

        importer(args.input, args.output, args.language)
    elif args.mode == MODE_EXPORTER:
        exporter(args.input, args.output)
    else:
        raise argparse.ArgumentTypeError('You must choose a mode.')


if __name__ == '__main__':
    main(sys.argv)
