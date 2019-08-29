import os
import sys

from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib'] 

from distutils.core import setup, Extension

setsc = Extension("guppy.sets.setsc",
                  [
                      "src/sets/sets.c",
                      "src/sets/bitset.c",
                      "src/sets/nodeset.c"
                      ]
                  )

heapyc = Extension("guppy.heapy.heapyc",
                   [
        	       'src/heapy/heapyc.c',
                       'src/heapy/stdtypes.c'
                       ]
                   )

def doit():
    if not sys.version.startswith('2.'):
        print('''\
setup.py: Error: This guppy package only supports Python2.
You can find the recommended Python3 version here:
https://github.com/zhuyifei1999/guppy3''')

        exit(1)
    setup(name="guppy",
          version="0.1.11",
          description="Guppy-PE -- A Python Programming Environment",
          long_description="""
Guppy-PE is a library and programming environment for Python2,
currently providing in particular the Heapy subsystem, which supports
object and heap memory sizing, profiling and debugging. It also
includes a prototypical specification language, the Guppy
Specification Language (GSL), which can be used to formally specify
aspects of Python programs and generate tests and documentation from a
common source.

Note that his package is for Python2 only. There is a fork that is
ported and recommended for Python3 at:
https://github.com/zhuyifei1999/guppy3

The guppy top-level package contains the following subpackages:

doc
       Documentation files. These are in a package so they get installed
       at a well-defined place, especially to support interactive help.

etc
       Support modules. Contains especially the Glue protocol module.

gsl
       The Guppy Specification Language implementation. This can
       be used to create documents and tests from a common source.

heapy
       The heap analysis toolset. It can be used to find information
       about the objects in the heap and display the information
       in various ways.

sets 
       Bitsets and 'nodesets' implemented in C.
""",
          author="Sverker Nilsson",
          author_email="sn@sncs.se",
          url="https://svenil.github.io/guppy-pe/",
          license='MIT',
          packages=[
            "guppy",
            "guppy.doc",
            "guppy.etc",
            "guppy.gsl",
            "guppy.heapy",
            "guppy.heapy.test",
            "guppy.sets",
            ],
          package_data={"guppy.doc" : ["*.html","*.jpg"]},
          ext_modules=[setsc, heapyc],
          classifiers=[
              "Programming Language :: Python :: 2",
              "License :: OSI Approved :: MIT License",
              "Operating System :: OS Independent",
          ]
    )

doit()

