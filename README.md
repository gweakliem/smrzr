# smrzr

[![PyPI](https://img.shields.io/pypi/v/smrzr.svg)](https://pypi.org/project/smrzr/)
[![Changelog](https://img.shields.io/github/v/release/gweakliem/smrzr?include_prereleases&label=changelog)](https://github.com/gweakliem/smrzr/releases)
[![Tests](https://github.com/gweakliem/smrzr/actions/workflows/test.yml/badge.svg)](https://github.com/gweakliem/smrzr/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/gweakliem/smrzr/blob/master/LICENSE)

Summarizes a web page using an LLM

## Installation

Install this tool using `pip`:
```bash
pip install smrzr
```
## Usage

Basic usage, get a summary of Roosevelt's "Citizenship in a Republic" speech:

```bash
smrzr "https://www.presidency.ucsb.edu/documents/address-the-sorbonne-paris-france-citizenship-republic"
```

For the full set of options, run:
```bash
smrzr --help
```
You can also use:
```bash
python -m smrzr --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd smrzr
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```

To run the tests:
```bash
pytest
```
