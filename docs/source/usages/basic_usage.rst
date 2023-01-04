###############
 Basic Example
###############

The following example shows how to use the library to create a simple
logger

.. code:: python

   from bohicalog import logger

   logger.debug("hello")
   logger.info("info")
   logger.warning("warn")
   logger.error("error")

   # This is how you'd log an exception
   try:
       raise Exception("this is a demo exception")
   except Exception as e:
       logger.exception(e)

   # JSON logging
   import bohicalog

   bohicalog.json()

   logger.info("JSON test")

   # Start writing into a logfile
   bohicalog.logfile("/tmp/bohicalog-demo.log")

   # Set a minimum loglevel
   bohicalog.loglevel(bohicalog.WARNING)

   ...

If you execute the above code, you'll get the following output:

.. program-output:: python basic_example.py
   :cwd: ../_examples
   :shell:
   :prompt:
