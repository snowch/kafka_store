#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'docopt',
    'google-api-python-client',
    'mock',
    'mysqlclient',
    'fastavro',
    'confluent_kafka',
    'smyte_pylib',
]

test_requirements = [
    'pytest',
]

setup(
    name='kafka_store',
    version='0.1.0',
    description="Kafka Store provides an easy way of archiving data from Kafka",
    long_description=readme + '\n\n' + history,
    author="Josh Yudaken",
    author_email='josh@smyte.com',
    url='https://github.com/smyte/kafka_store',
    packages=[
        'kafka_store',
    ],
    package_dir={'kafka_store':
                 'kafka_store'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='kafka_store',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
