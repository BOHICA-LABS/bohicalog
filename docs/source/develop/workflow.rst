#########
 Workflow
#########

The bohicalog module has codified its workflow using tox.

************
 Quick Start
************

To get started, you need to install tox:

.. code:: bash

    $ pip install tox

Then, you can run the tests using tox:

.. code:: bash

    $ tox

For example, by default it will:

.. code:: bash

    $ tox
    lint: commands[0]> black .
    All done! ✨ 🍰 ✨
    28 files left unchanged.
    lint: commands[1]> isort .
    Skipped 4 files
    lint: commands[2]> nbqa isort .
    No notebooks found in given path(s)
    lint: OK ✔ in 0.76 seconds
    manifest: commands[0]> check-manifest
    ...
    lint: OK (0.76=setup[0.02]+cmd[0.18,0.10,0.45] seconds)
    manifest: FAIL code 1 (8.50=setup[0.01]+cmd[8.49] seconds)
    pyroma: OK (0.50=setup[0.01]+cmd[0.48] seconds)
    flake8: FAIL code 1 (1.48=setup[0.01]+cmd[1.47] seconds)
    mypy: OK (0.13=setup[0.01]+cmd[0.12] seconds)
    doc8: FAIL code 1 (0.22=setup[0.01]+cmd[0.21] seconds)
    docstr-coverage: OK (0.16=setup[0.01]+cmd[0.15] seconds)
    docs-test: FAIL code 2 (4.97=setup[2.85]+cmd[0.01,0.01,2.10] seconds)
    py: OK (2.93=setup[2.43]+cmd[0.31,0.06,0.13] seconds)
    evaluation failed :( (19.78 seconds)

The above is defined by the tox section of the tox.ini file.

*************
 Tox Commands
*************

The tox.ini file also defines a number of environments, which can be ran individually:

-  doctests: runs document tests, xdoctest
-  coverge-clean: cleans up the coverage files, coverage erase
-  lint: runs linting, black, isort, nbqa isort
-  doclint: runs linting on the documentation. This will fail on custom directives, rstfmt
-  manifest: checks the manifest, check-manifest
-  flake8: runs flake8 linting
-  pyroma: runs pyroma to check the package friendliness of the project, pyroma
-  mypy: runs mypy type checking, mypy
-  doc8: runs doc8 to check the documentation, doc8
-  docstr-coverage: runs docstr-coverage to check the documentation coverage, docstr-coverage
-  docs: builds the documentation, sphinx
-  docs-test: Test building the documentation in an isolated environment, sphinx
-  coverage-report: generates a coverage report, coverage report
-  bumpversion: bumps the version, bumpversion
-  build: builds the package, python setup.py sdist bdist_wheel
-  release: releases the package, twine
-  testrelease: releases the package to test.pypi.org, twine
-  finish: finishes the release, bumpversion

To run a specific environment, you can use the -e flag:

.. code:: bash

    $ tox -e lint

*****************
 Release Workflow
*****************

The release workflow is defined below:

1.  tox -e lint
2.  tox -e manifest
3.  tox -e pyroma
4.  tox -e flake8
5.  tox -e mypy
6.  tox -e doc8
7.  tox -e docstr-coverage
8.  tox -e docs-test
9.  tox -e py
10.  tox
11.  tox -e bumpversion -- {major, minor} <-- Only if required, finish automatically bumps
     the minor version after each release
12.  tox -e finish

Ensure you have the following environment variables set:

-  TWINE_USERNAME
-  TWINE_PASSWORD
-  TELEGRAM_BOT_TOKEN
-  TELEGRAM_BOT_CHAT_ID

Execute steps 1-10 to ensure that the code is ready for release.
If any of the steps fail, fix the issues and repeat the steps.

If the release is a major or minor release, execute step 11 to bump the version.
If the release is a patch release, skip step 11.

Execute step 12 to finish the release. This will automatically bump the version to the next minor version.
This is to ensure that the version is always ahead of the latest release.


************
 Tox File
************

The full tox.ini is listed below:

.. literalinclude:: ../../../tox.ini
    :language: ini
    :linenos:
