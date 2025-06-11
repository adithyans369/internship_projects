import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('TkAgg')  # or 'Qt5Agg' if available

df=pd.read_csv("weather_data.csv")
fig,ax1=plt.subplots()
bar_width=0.4
x=range(len(df['Time']))
ax1.bar([i - bar_width/2 for i in x], df['Temperature'],
        width=bar_width, color='yellow')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature(degreecelsius)')
ax1.set_xticks(x)
ax1.set_xticklabels(df['Time'])

ax2=ax1.twinx()
ax2.bar([i + bar_width/2 for i in x], df['Humidity'],
        width=bar_width, color='orange')
ax2.set_ylabel('Humidity(%)')

plt.title("Temperature and Humidity over Time")

plt.tight_layout()
plt.show()
