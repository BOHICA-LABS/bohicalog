################################################
 BOHICA Logging Library |release| Documentation
################################################

.. image:: https://github.com/BOHICA-Labs/bohicalog/workflows/Tests/badge.svg
   :target: https://github.com/BOHICA-Labs/bohicalog/actions?query=workflow%3ATests

.. image:: https://img.shields.io/pypi/v/bohicalog
   :target: https://pypi.org/project/bohicalog

.. image:: https://img.shields.io/pypi/pyversions/bohicalog
   :target: https://pypi.org/project/bohicalog

.. image:: https://img.shields.io/pypi/l/bohicalog
   :target: https://github.com/BOHICA-Labs/bohicalog/blob/main/LICENSE

.. image:: https://readthedocs.org/projects/bohicalog/badge/?version=latest
   :target: https://bohicalog.readthedocs.io/en/latest/?badge=latest

.. image:: https://codecov.io/gh/BOHICA-Labs/bohicalog/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/BOHICA-Labs/bohicalog/branch/main

.. image:: https://img.shields.io/badge/Cookiecutter-snekpack-blue
   :target: https://github.com/cthoyt/cookiecutter-python-package

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: https://github.com/BOHICA-Labs/bohicalog/blob/main/.github/CODE_OF_CONDUCT.md

.. image:: https://wakatime.com/badge/user/db8a3ca7-6189-459a-a0a4-ba68105a41ee/project/07a61305-1b3b-4cfd-82d8-ba80283fb7b9.svg
   :target: https://wakatime.com/projects/bohicalog

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   install/installation

.. toctree::
   :maxdepth: 1
   :caption: Usage

   usages/basic_usage
   usages/command_line_usage
   usages/telegram_usage

.. toctree::
   :maxdepth: 1
   :caption: Modules

   modules/bohicalog_module

.. toctree::
   :maxdepth: 1
   :caption: Handlers

   handlers/telegram_module

.. toctree::
   :maxdepth: 1
   :caption: Command Line

   cli/cli_module

.. toctree::
   :maxdepth: 1
   :caption: Development

   develop/workflow
   develop/cicd

********************
 Indices and Tables
********************

-  :ref:`genindex`
-  :ref:`modindex`
-  :ref:`search`

**************
 Cookiecutter
**************

This package was created with the `cookiecutter
<https://github.com/cookiecutter/cookiecutter>`_ package using
`cookiecutter-snekpack
<https://github.com/cthoyt/cookiecutter-snekpack>`_ template. It comes
with the following:

-  Standard `src/` layout
-  Declarative setup with `setup.cfg` and `pyproject.toml`
-  Reproducible tests with `pytest` and `tox`
-  A vanity CLI via python entrypoints
-  Version management with `bumpversion`
-  Documentation build with `sphinx`
-  Testing of code quality with `flake8` in `tox`
-  Testing of documentation coverage with `docstr-coverage` in `tox`
-  Testing of documentation format and build in `tox`
-  Testing of package metadata completeness with `pyroma` in `tox`
-  Testing of MANIFEST correctness with `check-manifest` in `tox`
-  Testing of optional static typing with `mypy` in `tox`
-  A `py.typed` file so other packages can use your type hints
-  Automated running of tests on each push with GitHub Actions
-  Configuration for `ReadTheDocs <https://readthedocs.org/>`_
-  A good base `.gitignore` generated from `gitignore.io
   <https://gitignore.io>`_.
-  A pre-formatted README with badges
-  A pre-formatted LICENSE file with the MIT License (you can change
   this to whatever you want, though)
-  A pre-formatted CONTRIBUTING guide
-  Automatic tool for releasing to PyPI with ``tox -e finish``
-  A copy of the `Contributor Covenant
   <https://www.contributor-covenant.org>`_ as a basic code of conduct
