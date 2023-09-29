# Changelog

All notable changes to this project will be documented in this file.


## Unreleased (YYYY-MM-DD)

- No changes yet.


## 1.0.6 (2023-04-30)

- Remove range-pinning ``python = ">=3.8.0,<4.0"``, only specify bottom-range ``">=3.8.0"``

- Remove rang-pinned dependencies ``tox``, ``nox``.


## 1.0.5 (2023-04-12)

- Remove ``autoset_pwd.cancel``-function

- Depend on ``sitecustomize-entrypoints>=1.1.0``


## 1.0.4 (2023-03-29)

- Update **gh-action-pypi-publish** to **@v1.8.3**


## 1.0.3 (2023-03-29)

- Fix poetry installation in github-release-action.

- Add poetry version-pinning in github-release-action.


## 1.0.2 (2023-03-29)

- Add github-actions for [linting](https://github.com/libranet/autoset-pwd/actions/workflows/linting.yaml) and [testing](https://github.com/libranet/autoset-pwd/actions/workflows/testing.yaml).
- Add boilerplate-files to comply with Github's [_Community Standards_](https://github.com/libranet/autoset-pwd/community)

- Refactored make-file.

- Fix some typo's in docstrings.


## 1.0.1 (2023-03-19)

- Test releasing via ``poetry-release``.


## 1.0 (23-03-19)

- Add ``readthedocs.yaml``.

- Package created by [Wouter Vanden Hove <wouter@libranet.eu>]
