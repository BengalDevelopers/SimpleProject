#from distutils.core import setup
#from distutils.extension import Extension
#import numpy
#from Cython.Build import cythonize


#extensions = [
#    Extension("cloop_array", ["cloop_array.pyx"],
#        include_dirs=[numpy.get_include()]),
#]
#
#setup(
#    cmdclass={'build_ext': build_ext},
#    ext_modules=cythonize(extensions),
#)
#


from distutils.core import setup, Extension
import numpy
from Cython.Distutils import build_ext

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("dataFrameCSimulation", sources=["cloop_array.pyx"], include_dirs=[numpy.get_include()])],
)

