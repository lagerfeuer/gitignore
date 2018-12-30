# gitignore
Python 3 gitignore fetcher based on [gitignore.io](http://gitignore.io)

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

## Todo

[ ] add cache (don't need to query gitignore.io everytime)
