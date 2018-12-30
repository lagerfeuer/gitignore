# gitignore
Python 3 gitignore fetcher based on [gitignore.io](http://gitignore.io)

## Install

```sh
# pip3 install giig
```

## Usage

```python
usage: giig [-h] [--list] [--search SEARCH] [--file FILE] [lang [lang ...]]

Download .gitignore files from gitignore.io

positional arguments:
  lang                  language, IDE or OS to include in the .gitignore file

optional arguments:
  -h, --help            show this help message and exit
  --list, -l            list all language, IDE or OS options
  --search SEARCH, -s SEARCH
                        search list of options and print matches
  --file FILE, -f FILE  specify which file to write to
```

### Use as library

```python
import giig

# get list of languages, IDEs, etc.
giig.get_list()

# get list of languages, IDEs, etc.
giig.search(term)

# get gitignore for one/several languages, IDEs, etc.
# where options is a list of terms
giig.get_ignore(options)
```

## Todo

* [ ] make giig print to stdout without `-f`
* [ ] add cache (don't need to query gitignore.io everytime)
