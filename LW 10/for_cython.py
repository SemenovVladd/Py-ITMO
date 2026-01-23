from Cython.Build import cythonize
from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

setup(
    name="iterc",
    ext_modules=cythonize("iterc.pyx", annotate=True,
                          compiler_directives={"language_level": 3}),
)