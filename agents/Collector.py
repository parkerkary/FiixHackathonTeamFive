class Collector:

    taskRepository = {
        'mercedes' : {
            "General Periodic Checks" : [ "Engine oil level", "Engine coolant level", "Brake fluid level", "Windshield washer system", "Lighting system", "Condition of tires and tire pressure" ],
            "Emissions Control System Maintenance" : ["Changing engine oil and replacing filters", "Replacing the engine air filter", "Replacing the fuel filter", "Replacing spark plugs", "Refilling DEF (Diesel Exhaust Fluid)"]
            }
        }
    
    smList = ["SM1002", "SM365", "SM45"]

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def grabLink(self):
        return "http://www.somelink.to.something.com"
    
    def grabTasks(self, assetCategoryID):
        return self.taskRepository
    
    def grabExistingScheduledMaintenances(self, assetCategoryID):
        return self.smList
    
    
    def collect(self, assetCategoryID):
        compiledRecommendation = { "manual_link" : self.grabLink(), "task_list" : self.grabTasks(assetCategoryID), "sm_list" : self.grabExistingScheduledMaintenances(assetCategoryID) }
        return compiledRecommendation
        