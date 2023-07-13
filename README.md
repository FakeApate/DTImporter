# Unreal Engine 4 Data Extraction and JSON Conversion

This Python module facilitates the extraction of datatables and enums from an Unreal Engine 4 game and converts them into a single JSON file. The resulting JSON file can be used for creating a database from the game's data. How the initial extraction from the ue4 '.pak' file happens is not part of this project. **Hint: F-Model**

## Table of Contents

- [Unreal Engine 4 Data Extraction and JSON Conversion](#unreal-engine-4-data-extraction-and-json-conversion)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Usage

Check out export.py in the module or the unit test.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, please submit a pull request. Ensure that your code adheres to the project's coding style and that tests pass successfully. Also run a code coverage and paste it into the request.

Current Coverage:

```text
(dtimporter-py3.11) PS E:\DTImporter> coverage report
Name                            Stmts   Miss  Cover
---------------------------------------------------
dtimporter\__init__.py              1      0   100%
dtimporter\baseclass.py             9      0   100%
dtimporter\datatable.py            18      0   100%
dtimporter\export.py               21      0   100%
dtimporter\factory.py              53      3    94%
dtimporter\userdefinedenum.py      19      0   100%
---------------------------------------------------
TOTAL                             121      3    98%
```

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
