# Import pandas and matplotlib 

import pandas as pd 
import matplotlib.pyplot as plt 

# Load file csv
netflix_df= pd.read_csv(r"C:\Users\LENOVO\OneDrive\Bureau\netflix_data.csv")

# Subset data type "Movie"
netflix_subset= netflix_df[netflix_df["type"]=="Movie"]
netflix_movies= netflix_subset[["title","country","genre","release_year","duration"]]
short_movies= netflix_movies[netflix_movies["duration"]<60]

# ITERATE

colors=[]

for x,y in netflix_movies.iterrows():
    if y["genre"]=="Children":
       colors.append("green")
    elif   y["genre"]=="Documentaries":
       colors.append("red")
    elif y["genre"]=="Stand-Up":
       colors.append("yellow")
    else: 
        colors.append("black") 
print(colors[:10])   

# Plot
fig= plt.figure(figsize=(12,8))
plt.scatter(netflix_movies.release_year,netflix_movies.duration,c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()






