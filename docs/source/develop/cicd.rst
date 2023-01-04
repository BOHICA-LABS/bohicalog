#################
 CI / CD Pipeline
#################

The bohicalog module is built and tested automatically by the CI / CD pipeline.
The pipeline is defined in the .gitlab-ci.yml file. The pipeline is triggered by a push to the master branch.
The pipeline consists of the following stages:

-  lint: runs the linter(s) on the code
-  docs: runs the linter(s) on the documentation
-  test: runs the unit tests

*******************
 Github Action File
*******************

The full test.yml is listed below:

.. literalinclude:: ../../../.github/workflows/tests.yml
    :language: yaml
    :linenos:
