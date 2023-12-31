[![Testing](https://img.shields.io/github/actions/workflow/status/libranet/autoset-pwd/testing.yaml?branch=main&longCache=true&style=flat-square&label=tests&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/autoset-pwd/actions/workflows/testing.yaml)
[![Linting](https://img.shields.io/github/actions/workflow/status/libranet/autoset-pwd/linting.yaml?branch=main&longCache=true&style=flat-square&label=linting&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/autoset-pwd/actions/workflows/linting.yaml)
[![Read the Docs](https://readthedocs.org/projects/autoset-pwd/badge/?version=latest)](https://autoset-pwd.readthedocs.io/en/latest/)
[![Codecov](https://codecov.io/gh/libranet/autoset-pwd/branch/main/graph/badge.svg?token=AFP6UMXEN5)](https://codecov.io/gh/libranet/autoset-pwd)
[![PyPi Package](https://img.shields.io/pypi/v/autoset-pwd?color=%2334D058&label=pypi%20package)](https://pypi.org/project/autoset-pwd/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/libranet/autoset-pwd/blob/main/docs/license.md)



https://app.codecov.io/gh/libranet/autoset-pwd
# autoset-pwd

Automatically add the $PWD-directory to the ``PWD_DIR``-environment variable
via ``sitecustomize``-entrypoint.

## How does it work?

We register the ``autoset_pdw.entrypoint()``-function to the ``sitecustomize``-module that is installed by the
[sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)-package.

The registered function will look up ``os.getcwd()`` in your current working directory and
set it as ``PWD_DIR``-environment variable.


## Installation

Install via pip:

```bash
> bin/pip install autoset-pwd
```

Or add to your poetry-based project:

```bash
> poetry add autoset-pwd
```


## Validate & Usage
After installing this package there is nothing left to do explicitly.
We can validate that the plugin work correctly by starting a python-session and checking the ``PWD_DIR``-environment-variable:

```bash
> bin/python
```

```python
>>> import os
>>> print(os.getcwd())
    "<path-to-your-current-dir>"
```
>>> print(os.getenv("PwD_DIR"))
    "<path-to-your-current-dir>"


## Registered sitecustomize-entrypoint

The ``autoset_pwd``-function is registered as a ``sitecustomize``-entrypoint in our pyproject.toml_:

``` toml
    [tool.poetry.plugins]
    [tool.poetry.plugins."sitecustomize"]
    autoset_pwd = "autoset_pwd:entrypoint"
```

Sitecustomize and all its registered entrypoints will be executed at the start of *every* python-process.
For more information, please see [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)


## Compatibility

 [![Python Version](https://img.shields.io/pypi/pyversions/autoset-pwd?:alt:PyPI-PythonVersion)](https://pypi.org/project/autoset-pwd/)
 [![PyPI - Implementation](https://img.shields.io/pypi/implementation/autoset-pwd?:alt:PyPI-Implementation)](https://pypi.org/project/autoset-pwd/)

``autoset-pwd``  works on Python 3.8+, including PyPy3. Tested until Python 3.11,


## Notable dependencies

- [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)


