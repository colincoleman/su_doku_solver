from setuptools import setup, find_packages

setup(
    name="sudoku",
    package_dir={'': 'src'},
    packages=find_packages(where='src')
)
