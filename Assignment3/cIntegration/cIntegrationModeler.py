class cIntegrationModeler:
    
    def multiDataFrameGeneratorFunc(self, yearHourRange, simulationModelSize, mu, sigma):
        import dataFrameCSimulation 
        results = dataFrameCSimulation.simulationModelUsingCython(yearHourRange, simulationModelSize, mu, sigma)
        return results
    


    

