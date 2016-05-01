import cython

import numpy as np
# cimport the Cython declarations for numpy
cimport numpy as np
# Using the Numpy-C-API from Cython
np.import_array()

# create the wrapper code, with numpy type annotations
def simulationModelUsingCython(yearHourRange, int simulationModelSize,float mu, float sigma):    
    cdef int modelSize = simulationModelSize
    cdef int i = 0
    cdef int x = 0
    cdef list dataframelist =[]
    cdef np.ndarray dynamicOnesArray = np.ones(modelSize)
    from timeSeriesModule.timeSeries import timeSeries	
    ts = timeSeries()
    for x in dynamicOnesArray:
        dataframelist.append(ts.getYearlyDataSeries(yearHourRange, mu, sigma))
    return dataframelist
