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
        'ford f450' : {
            "General Periodic Checks" : [ "Gas Cap", "Oil and coolant level", "Brake fluid level", "Oil, fuel and air filters", "Tire pressure" ],
            "Emissions Control System Maintenance" : ["Exhaust Gas Recirculation", "Replace the ecrankcase breather filter", "Replacing the oil, air and fuel filter", "Replacing spark plugs", "Refilling DEF (Diesel Exhaust Fluid)"]
            },
        'bugatti veyron limited edition ' : {
            "General Periodic Checks" : [ "Engine oil level", "Engine coolant level", "Brake fluid level", "Windshield washer system", "Lighting system", "Condition of tires and tire pressure" ],
            "Emissions Control System Maintenance" : ["Changing engine oil and replacing filters", "Replacing the engine air filter", "Replacing the fuel filter", "Replacing spark plugs" ]
            },
        'jeep grand cherokee' : {
            "General Periodic Checks" : [ "Anti-backfire diverter valve", "Engine oil and coolant", "Valve, air pump and brake fluid", "Condition of tires and tire pressure" ],
            "Emissions Control System Maintenance" : ["Carburetor Fuel Filter", "Check spark plug and coil wires", "Check oil, air and fuel filter",  "Fuel tanks (including Liquid-Vapour separator)"]
            },
        'tesla model s' : {
            "General Periodic Checks" : [ "Key fob battery", "Charging and EV Inlet door", "Battery modules & Fuel Cell", "Brake fluid replacement", "Cabin air filter replacement" ],
            "Emissions Control System Maintenance" : ["Remote Climate Control Module", "Regenerative braking (RGB)", "Replacing the oil, air and fuel filter", "Replacing spark plugs", "Refilling DEF (Diesel Exhaust Fluid)"]
            },
        'lamborghini aventador' : {
            "General Periodic Checks" : [ "Air Filter", "Injection & Ignition", "Brake fluid & Clutch wear", "Spark plugs", "Lighting system", "Condition of tires and tire pressure" ],
            "Emissions Control System Maintenance" : ["Changing engine oil and replacing filters", "Activated Charcoal filters", "Dust filters in Air Conditioning", "Oxygen sensor" ]
            },
        'rolls royce ghost' : {
            "General Periodic Checks" : [ "Oil and Coolant", "Gearbox oil filter", "Ignition and fuel hoses", "Tires and tire pressure" ],
            "Emissions Control System Maintenance" : ["Carburetor Fuel Filter", "Check spark plug and coil wires", "Check oil, air and fuel filter",  "Fuel tanks (including Liquid-Vapour separator)"]
            },
        'audi tt rs plus' : {
            "General Periodic Checks" : [ "Gas Cap", "Oil and coolant level", "Brake fluid level", "Oil, fuel and air filters", "Tire pressure" ],
            "Emissions Control System Maintenance" : ["Exhaust Gas Recirculation", "Replace the ecrankcase breather filter", "Replacing the oil, air and fuel filter", "Replacing spark plugs", "Refilling DEF (Diesel Exhaust Fluid)"]
            },
        'smart' : {
            "General Periodic Checks" : [ "Battery pack", "Assess the brake wear", "Radiator fluid top-ups and fixes", "Replace cabin air filter", "Spark plugs and wires", "Check tires" ]
            }
        }

    triggers = [
        "Meter Reading - 5000 (Miles)",
        "Time Schedule - Every 2 (Months)",
        "Event - Break down",
        "Event - Puncture"
    ]

    def __init__(self,carName):
        '''
        Constructor
        '''
        
        self.scraper = WebScraper(carName)
    
    def grabLink(self):
        return self.scraper.webpage
    
    def grabTasks(self, assetCategoryID):
        return self.taskRepository[assetCategoryID.lower()]

    def collect(self, assetCategoryID):
        compiledRecommendation = { "manual_link" : self.grabLink(), "task_list" : self.grabTasks(assetCategoryID), "triggers" : self.triggers }
        return compiledRecommendation
        