from Scraper.WebScraper import WebScraper

class Collector:

    taskRepository = {
        'honda odyssey' : {
            "General Periodic Checks" : [ "Engine oil level", "Engine coolant level", "Brake fluid level", "Windshield washer system", "Lighting system", "Condition of tires and tire pressure" ],
            "Emissions Control System Maintenance" : ["Changing engine oil and replacing filters", "Replacing the engine air filter", "Replacing the fuel filter", "Replacing spark plugs" ]
            },
        'lincoln town car' : {
            "General Periodic Checks" : [ "Anti-backfire diverter valve", "Engine oil and coolant", "Valve, air pump and brake fluid", "Condition of tires and tire pressure" ],
            "Emissions Control System Maintenance" : ["Carburetor Fuel Filter", "Check spark plug and coil wires", "Check oil, air and fuel filter",  "Fuel tanks (including Liquid-Vapour separator)"]
            },
        'ford f150' : {
            "General Periodic Checks" : [ "Gas Cap", "Oil and coolant level", "Brake fluid level", "Oil, fuel and air filters", "Tire pressure" ],
            "Emissions Control System Maintenance" : ["Exhaust Gas Recirculation", "Replace the ecrankcase breather filter", "Replacing the oil, air and fuel filter", "Replacing spark plugs", "Refilling DEF (Diesel Exhaust Fluid)"]
            }
        }

    def __init__(self,carName):
        '''
        Constructor
        '''
        
        self.scraper = WebScraper(carName)
    
    def grabLink(self):
        return self.scraper.webpage
    
    def grabTasks(self, assetCategoryID):
        return self.taskRepository[assetCategoryID]

    def collect(self, assetCategoryID):
        compiledRecommendation = { "manual_link" : self.grabLink(), "task_list" : self.grabTasks(assetCategoryID) }
        return compiledRecommendation
        