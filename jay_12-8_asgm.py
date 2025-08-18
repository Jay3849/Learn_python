''' You run a maintenance service team that operates every first and third weekend of each month throughout the year. Each operation 
cycle lasts 16 hours. The team efficiency depends on the region’s climate and availability of tools, and both factors vary throughout
the year.
 
# Total professionals: 140
# Technicians: 95
# Supervisors: 45
# Operational schedule:
# Operates 2 weekends per month → 24 sessions per year
# Each session is 16 hours
# Base hourly efficiency rate = 12 units per hour
# Efficiency based on climate:
# Dry Season (Jan, Feb, Mar, Dec): 88%
# Rainy Season (Apr, May, Jun, Jul, Aug): 75%
# Cool Season (Sep, Oct, Nov): 82%
# Tool availability impact:
# Dry Season → 100% tools available
# Rainy Season → Only 85% tools available
# Cool Season → 90% tools available
# Supervisor efficiency is 10% higher than technicians
# This applies after climate and tool adjustment
 
# Create a program to calculate the total annual service efficiency units delivered by your maintenance team, considering:
# Climate conditions
# Tool availability
# Role-based efficiency boost
# Session frequency and duration
'''


def calculate_units(hours_per_session, technicians, supervisors):
    sessions_per_month = 2
    base_efficiency = 12  

    session_data = {
        'dry_session': {
            "months": ['Jan', 'Feb', 'Mar', 'Dec'],
            'climate_eff': 0.88,
            'tools_avail': 1.00
        },
        'rainy_session': {
            "months": ['Apr', 'May', 'Jun', 'Jul', 'Aug'],
            'climate_eff': 0.75,
            'tools_avail': 0.85
        },
        'cool_session': {
            "months": ['Sep', 'Oct', 'Nov'],
            'climate_eff': 0.82,
            'tools_avail': 0.90
        }
    }

    total_units = 0

    for season, data in session_data.items():
        months = len(data["months"])
        total_sessions = months * sessions_per_month
        total_hours = total_sessions * hours_per_session

   
        tech_units = technicians * base_efficiency * total_hours
        tech_units *= data["climate_eff"] * data["tools_avail"]

  
        sup_units = supervisors * base_efficiency * total_hours
        sup_units *= data["climate_eff"] * data["tools_avail"] * 1.10


        total_units += (tech_units + sup_units)

    return round(total_units, 2)



hours_per_session = int(input("Enter hours per session: "))
technicians = int(input("Enter number of technicians: "))
supervisors = int(input("Enter number of supervisors: "))


result = calculate_units(hours_per_session, technicians, supervisors)
print("Total Annual Service Efficiency Units:", result)
