
import pandas as pd
import matplotlib as plt
area_df = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')



import matplotlib.pyplot as plt 

transparency = 0.55 
ax = area_df.plot(kind='area', alpha=transparency, stacked=False, figsize=(20, 10)) 
ax.set_title('Plot Title') 
ax.set_ylabel('Vertical Axis Label') 
ax.set_xlabel('Horizontal Axis Label') 



