from setuptools import setup

with open('README.md', encoding="utf-8") as f:
    readme = f.read()

setup(
    name='giig',
    version='0.3.1',
    description='CLI for gitignore.io',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/lagerfeuer/gitignore',
    author='Lukas Deutz',
    author_email='lukas.deutz@mailfence.com',
    packages=['giig'],
    scripts=['bin/giig'],
    install_requires=['requests'],
    keywords='gitignore git cli',
    license='MIT',
    python_requires='>=3',
    classifiers=['Programming Language :: Python :: 3'],
)
