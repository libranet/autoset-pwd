:py:mod:`autoset_pwd`
========================

.. py:module:: autoset_pwd

.. autoapi-nested-parse::

   autoset_pwd.__init__.



Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   autoset_pwd.entrypoint
   autoset_pwd.get_bindir
   autoset_pwd.cancel



Attributes
~~~~~~~~~~

.. autoapisummary::

   autoset_pwd.__version__
   autoset_pwd.__copyright__


.. py:data:: __version__
   :value: '1.0.2a0'



.. py:data:: __copyright__
   :value: 'Copyright 2023 Libranet - MIT License.'



.. py:function:: entrypoint()

   Prepend python-bindir to PATH.


.. py:function:: get_bindir()

   Return the bindit form the isolated virtual environment.


.. py:function:: cancel()

   No-op function that can be used the cancel a registered entrypoint.

   Imagine you have multiple sitecustomize-entrypoints. If these entrypoints
   are registered via third-party packages, you cannot control the order of execution.

   Now suppose some of these entrypoints need an environment-variable that first need to be set
   by ``autoset_pwd`` needs to be executed before the others

   entrypoint 1:  foo.needs_envvar:bar
   entrypoint 2:  autoset_pwd.entrypoint:autoset_pwd

   in your project's pyproject.toml:

   [tool.poetry.plugins."sitecustomize"]

   # cancel the first registration using the original name
   autoset_pwd = "autoset_pwd.entrypoint:cancel"

   # re-register the same function under different name
   zz_autoset_pwd = "autoset_pwd.entrypoint:autoset_pwd"



