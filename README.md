TranslateGenerator
=========================

Python script to convert between CSV and Android/iOS localization files.

Uses Python 3.6.

Usage
-------
To convert from Android/iOS to CSV, use the importer:

```python TranslateGenerator.py -m importer -i <strings file> -o <csv file> -l <base language>```

`<base language>` could be `en`

NOTE: Do not edit the first line generated by the importer as the exporter will generate the folder languages based on that line.


To convert from CSV to Android/iOS, use the exporter:

```python TranslateGenerator.py -m exporter -i <csv file> -o <dir to save strings files>```

TODO
-------
- iOS reader/writer

License
-------

    Copyright 2018 Ricardo Carrapiço

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
