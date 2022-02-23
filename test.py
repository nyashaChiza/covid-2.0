from covid import Covid
covid = Covid(source="worldometers")
data = covid.get_status_by_country_name("zimbabwe")
zim_cases  = {'total_cases':data.get('total_cases'),'recovered':data.get('recovered'),'active':data.get('active_cases'),'deaths':data.get('deaths')}
print(zim_cases)