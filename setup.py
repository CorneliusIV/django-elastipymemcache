#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io

from setuptools import find_packages, setup

import django_elastipymemcache

setup(
    name="django-elastipymemcache",
    version="0.0.1",
    description="Django cache backend for Amazon ElastiCache (memcached)",
    keywords="elasticache amazon cache pymemcache memcached aws",
    author="HarikiTech",
    author_email="harikitech+noreply@googlegroups.com",
    url="http://github.com/harikitech/django-elastipymemcache",
    license="MIT",
    long_description=io.open("README.rst").read(),
    platforms="any",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "pymemcache==4.0.0",
        "Django>=3.2",
    ],
)
