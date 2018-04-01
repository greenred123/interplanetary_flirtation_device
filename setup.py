from setuptools import setup

setup(
    name='ifd',
    packages=['ifd'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pycups',
        'glob2'
    ],
)