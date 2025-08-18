# We run a business which execute on every quarter of every month throughout year. Every time when we are working we work for 24 hours.
# When hours finished we calculate our productivity form total work. To calculate productivity we depends on season. If It’s winter then 
# productivity is highest 90% of total, if it is summer the productivity is 80% of total and when monsoon productivity is 85% of total.
# Same thing apply to attendance. As per season people are absent on work. During winter attendance is 98%. During summer attendance is
# 85% and during monsoon attendance is 70%. We have total 169 professionals more or less who work with us. Out of 126 are males and 
# remain are females at this time. Male productivity is 5% higher than female. Every hours productivity rate is 10 or any we adjust as
# per market. Now, we need to calculate total productivity of year. Our calculation work with given algorithm with number of male and 
# female professionals and productivity rate we provide.  



# 4 times month 
# 12 * 4 = 48 

# 1 session = 24 hours 

# productivity logic 
# 3 seasons

# winter = 90%


# summer = 80%

# monsoon = 85%

# male productivity is 5% higher than female 

# productivity rate = 10 

# attendence

# winter = 98%


# summer = 85%

# monsoon = 70%


# total working professionals = 169 

# males = 126

# females = 169 - 126 = 43 



# output = total productivity of year

# input = male professionals , female professionals, productivate rate 




hours_per_session = 24
session_per_month = 4
total_month = 12 

session_data = {
 'winter' :
 {
  'productivity':0.90,
  'attendence':0.98,
  'months':['Nov','Dec','Jan','Feb']

 },
 'summer' :
 {
  'productivity':0.80,
  'attendence':0.85,
  'months':['Mar','Apr','May','Jun']

 },
 'monsoon' :
 {
  'productivity':0.85,
  'attendence':0.70,
  'months':['Jul','Aug','Sep','Oct']

 },
}


male_productivity_rate = 1.05
female_productivity_rate = 1

months_to_season = {}
for sesons , data in session_data.items():
    for month in data['months']:
        months_to_season[month] = sesons



months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']



def claculate_productivity(total_working_professionals,male_professionals, hourly_productivity_rate):
    total_productivity = 0
    female_professionals = total_working_professionals - male_professionals 
    for month in months:
        season = months_to_season[month]
        data = session_data[season]
        
        males_rate =  male_professionals * data['attendence']
        female_rate = female_professionals * data['attendence']

        male_productivity = males_rate * hours_per_session * hourly_productivity_rate * male_productivity_rate
        female_productivity = female_rate * hours_per_session * hourly_productivity_rate * female_productivity_rate

        total_session_productivity = (male_productivity + female_productivity) * data['productivity']

        monthly_productivity = total_session_productivity * session_per_month

        total_productivity += monthly_productivity

        return total_productivity
    


total_working_professionals = 180
male_professionals = 126
hourly_productivity_rate = 10

output = claculate_productivity(total_working_professionals,male_professionals, hourly_productivity_rate)
print(output)
    
    
    
    
    
    
    


    




    
    
      
    
    
    
    
    
    
    
    



