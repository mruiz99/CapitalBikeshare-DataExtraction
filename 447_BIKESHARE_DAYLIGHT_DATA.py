import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import time
import json

jan20bikedata=pd.read_csv("202001-capitalbikeshare-tripdata.csv")
feb20bikedata=pd.read_csv("202002-capitalbikeshare-tripdata.csv")
mar20bikedata=pd.read_csv("202003-capitalbikeshare-tripdata.csv")
may20bikedata=pd.read_csv("202005-capitalbikeshare-tripdata.csv")
jun20bikedata=pd.read_csv("202006-capitalbikeshare-tripdata.csv")
jul20bikedata=pd.read_csv("202007-capitalbikeshare-tripdata.csv")
aug20bikedata=pd.read_csv("202008-capitalbikeshare-tripdata.csv")
sep20bikedata=pd.read_csv("202009-capitalbikeshare-tripdata.csv")
oct20bikedata=pd.read_csv("202010-capitalbikeshare-tripdata.csv")
nov20bikedata=pd.read_csv("202011-capitalbikeshare-tripdata.csv")
dec20bikedata=pd.read_csv("202012-capitalbikeshare-tripdata.csv")

jan20bikedata=jan20bikedata[['Duration','Start date','End date','Member type']]
jan20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']

feb20bikedata=feb20bikedata[['Duration','Start date','End date','Member type']]
feb20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']

mar20bikedata=mar20bikedata[['Duration','Start date','End date','Member type']]
mar20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']

may20bikedata=may20bikedata[['started_at','ended_at','member_casual']]
may20bikedata.loc[:,'start']=may20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
may20bikedata.loc[:,'end']=may20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
may20bikedata.loc[:,'duration'] = pd.to_datetime(may20bikedata['end']) - pd.to_datetime(may20bikedata['start'])
may20bikedata.loc[:,'duration'] = may20bikedata['duration'].apply(lambda x: x.total_seconds())

jun20bikedata=jun20bikedata[['started_at','ended_at','member_casual']]
jun20bikedata.loc[:,'start']=jun20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
jun20bikedata.loc[:,'end']=jun20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
jun20bikedata.loc[:,'duration'] = pd.to_datetime(jun20bikedata['end']) - pd.to_datetime(jun20bikedata['start'])
jun20bikedata.loc[:,'duration'] = jun20bikedata['duration'].apply(lambda x: x.total_seconds())

jul20bikedata=jul20bikedata[['started_at','ended_at','member_casual']]
jul20bikedata.loc[:,'start']=jul20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
jul20bikedata.loc[:,'end']=jul20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
jul20bikedata.loc[:,'duration'] = pd.to_datetime(jul20bikedata['end']) - pd.to_datetime(jul20bikedata['start'])
jul20bikedata.loc[:,'duration'] = jul20bikedata['duration'].apply(lambda x: x.total_seconds())

aug20bikedata=aug20bikedata[['started_at','ended_at','member_casual']]
aug20bikedata.loc[:,'start']=aug20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
aug20bikedata.loc[:,'end']=aug20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
aug20bikedata.loc[:,'duration'] = pd.to_datetime(aug20bikedata['end']) - pd.to_datetime(aug20bikedata['start'])
aug20bikedata.loc[:,'duration'] = aug20bikedata['duration'].apply(lambda x: x.total_seconds())

sep20bikedata=sep20bikedata[['started_at','ended_at','member_casual']]
sep20bikedata.loc[:,'start']=sep20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
sep20bikedata.loc[:,'end']=sep20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
sep20bikedata.loc[:,'duration'] = pd.to_datetime(sep20bikedata['end']) - pd.to_datetime(sep20bikedata['start'])
sep20bikedata.loc[:,'duration'] = sep20bikedata['duration'].apply(lambda x: x.total_seconds())

oct20bikedata=oct20bikedata[['started_at','ended_at','member_casual']]
oct20bikedata.loc[:,'start']=oct20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
oct20bikedata.loc[:,'end']=oct20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
oct20bikedata.loc[:,'duration'] = pd.to_datetime(oct20bikedata['end']) - pd.to_datetime(oct20bikedata['start'])
oct20bikedata.loc[:,'duration'] = oct20bikedata['duration'].apply(lambda x: x.total_seconds())

nov20bikedata=nov20bikedata[['started_at','ended_at','member_casual']]
nov20bikedata.loc[:,'start']=nov20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
nov20bikedata.loc[:,'end']=nov20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
nov20bikedata.loc[:,'duration'] = pd.to_datetime(nov20bikedata['end']) - pd.to_datetime(nov20bikedata['start'])
nov20bikedata.loc[:,'duration'] = nov20bikedata['duration'].apply(lambda x: x.total_seconds())

dec20bikedata=dec20bikedata[['started_at','ended_at','member_casual']]
dec20bikedata.loc[:,'start']=dec20bikedata['started_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
dec20bikedata.loc[:,'end']=dec20bikedata['ended_at'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S'))
dec20bikedata.loc[:,'duration'] = pd.to_datetime(dec20bikedata['end']) - pd.to_datetime(dec20bikedata['start'])
dec20bikedata.loc[:,'duration'] = dec20bikedata['duration'].apply(lambda x: x.total_seconds())

may20bikedata=may20bikedata[['duration','started_at','ended_at','member_casual']]
may20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']
jun20bikedata=jun20bikedata[['duration','started_at','ended_at','member_casual']]
jun20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']
jul20bikedata=jul20bikedata[['duration','started_at','ended_at','member_casual']]
jul20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']
aug20bikedata=aug20bikedata[['duration','started_at','ended_at','member_casual']]
aug20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']
sep20bikedata=sep20bikedata[['duration','started_at','ended_at','member_casual']]
sep20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']
oct20bikedata=oct20bikedata[['duration','started_at','ended_at','member_casual']]
oct20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']
nov20bikedata=nov20bikedata[['duration','started_at','ended_at','member_casual']]
nov20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']
dec20bikedata=dec20bikedata[['duration','started_at','ended_at','member_casual']]
dec20bikedata.columns=['Duration (seconds)','Start date','End date','Member type']

jan20grouped=jan20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
feb20grouped=feb20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
mar20grouped=mar20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
may20grouped=may20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
jun20grouped=jun20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
jul20grouped=jul20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
aug20grouped=aug20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
sep20grouped=sep20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
oct20grouped=oct20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
nov20grouped=nov20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()
dec20grouped=dec20bikedata.groupby('Member type')['Duration (seconds)'].agg('sum').reset_index()

jan20grouped.loc[:,'Total minutes'] = round(jan20grouped['Duration (seconds)']/60,2)
feb20grouped.loc[:,'Total minutes'] = round(feb20grouped['Duration (seconds)']/60,2)
mar20grouped.loc[:,'Total minutes'] = round(mar20grouped['Duration (seconds)']/60,2)
may20grouped.loc[:,'Total minutes'] = round(may20grouped['Duration (seconds)']/60,2)
jun20grouped.loc[:,'Total minutes'] = round(jun20grouped['Duration (seconds)']/60,2)
jul20grouped.loc[:,'Total minutes'] = round(jul20grouped['Duration (seconds)']/60,2)
aug20grouped.loc[:,'Total minutes'] = round(aug20grouped['Duration (seconds)']/60,2)
sep20grouped.loc[:,'Total minutes'] = round(sep20grouped['Duration (seconds)']/60,2)
oct20grouped.loc[:,'Total minutes'] = round(oct20grouped['Duration (seconds)']/60,2)
nov20grouped.loc[:,'Total minutes'] = round(nov20grouped['Duration (seconds)']/60,2)
dec20grouped.loc[:,'Total minutes'] = round(dec20grouped['Duration (seconds)']/60,2)

jan20bikedata.loc[:,'date'] = jan20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
feb20bikedata.loc[:,'date'] = feb20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
mar20bikedata.loc[:,'date'] = mar20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
may20bikedata.loc[:,'date'] = may20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
jun20bikedata.loc[:,'date'] = jun20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
jul20bikedata.loc[:,'date'] = jul20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
aug20bikedata.loc[:,'date'] = aug20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
sep20bikedata.loc[:,'date'] = sep20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
oct20bikedata.loc[:,'date'] = oct20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
nov20bikedata.loc[:,'date'] = nov20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))
dec20bikedata.loc[:,'date'] = dec20bikedata['Start date'].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d'))

datejan20=jan20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datefeb20=feb20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datemar20=mar20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datemay20=may20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datejun20=jun20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datejul20=jul20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
dateaug20=aug20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datesep20=sep20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
dateoct20=oct20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datenov20=nov20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()
datedec20=dec20bikedata.groupby('date')['Duration (seconds)'].agg('sum').reset_index()

sunriseAPI=[]
sunriseAPIjan=[]
sunriseAPIfeb=[]
sunriseAPImar=[]
sunriseAPImay=[]
sunriseAPIjun=[]
sunriseAPIjul=[]
sunriseAPIaug=[]
sunriseAPIsep=[]
sunriseAPIoct=[]
sunriseAPInov=[]
sunriseAPIdec=[]

janlst=[]
feblst=[]
marlst=[]
maylst=[]
junlst=[]
jullst=[]
auglst=[]
seplst=[]
octlst=[]
novlst=[]
declst=[]

count=0
day=0

for num in datejan20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIjan.append(day)
    count+=1
janlst.append(day)
janSer=pd.Series(sunriseAPIjan)

count=0
day=0
for num in datefeb20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIfeb.append(day)
    count+=1
feblst.append(day)
febSer=pd.Series(sunriseAPIfeb)

count=0
day=0
for num in datemar20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPImar.append(day)
    count+=1
marlst.append(day)
marSer=pd.Series(sunriseAPImar)

count=0
day=0
for num in datemay20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPImay.append(day)
    count+=1
maylst.append(day)
maySer=pd.Series(sunriseAPImay)

count=0
day=0
for num in datejun20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIjun.append(day)
    count+=1
junlst.append(day)
junSer=pd.Series(sunriseAPIjun)

count=0
day=0
for num in datejul20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIjul.append(day)
    count+=1
jullst.append(day)
julSer=pd.Series(sunriseAPIjul)

count=0
day=0
for num in dateaug20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIaug.append(day)
    count+=1
auglst.append(day)
augSer=pd.Series(sunriseAPIaug)

count=0
day=0
for num in datesep20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIsep.append(day)
    count+=1
seplst.append(day)
sepSer=pd.Series(sunriseAPIsep)

count=0
day=0
for num in dateoct20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIoct.append(day)
    count+=1
octlst.append(day)
octSer=pd.Series(sunriseAPIoct)

count=0
day=0
for num in datenov20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPInov.append(day)
    count+=1
novlst.append(day)
novSer=pd.Series(sunriseAPInov)

count=0
day=0
for num in datedec20['date']:
    sunsetrise=f"https://api.sunrise-sunset.org/json?lat=38.9072&lng=-77.0369&date={num}&formatted=0"
    #time.sleep(0.15)
    test=requests.get(sunsetrise)
    print(test,count)
    month = json.loads(test.text)
    month = pd.json_normalize(month['results'])
    day+=month['day_length'].iloc[0]
    sunriseAPIdec.append(day)
    count+=1
declst.append(day)
decSer=pd.Series(sunriseAPIdec)

allmonths=["JANUARY","FEBRUARY","MARCH","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
alltimes=[janlst[0],feblst[0],marlst[0],maylst[0],junlst[0],jullst[0],
          auglst[0],seplst[0],octlst[0],novlst[0],declst[0]]
casual=[jan20grouped['Total minutes'].iloc[0],feb20grouped['Total minutes'].iloc[0],mar20grouped['Total minutes'].iloc[0],
              may20grouped['Total minutes'].iloc[0],jun20grouped['Total minutes'].iloc[0],jul20grouped['Total minutes'].iloc[0],
              aug20grouped['Total minutes'].iloc[0],sep20grouped['Total minutes'].iloc[0],oct20grouped['Total minutes'].iloc[0],
              nov20grouped['Total minutes'].iloc[0],dec20grouped['Total minutes'].iloc[0]]
members=[jan20grouped['Total minutes'].iloc[1],feb20grouped['Total minutes'].iloc[1],mar20grouped['Total minutes'].iloc[1],
              may20grouped['Total minutes'].iloc[1],jun20grouped['Total minutes'].iloc[1],jul20grouped['Total minutes'].iloc[1],
              aug20grouped['Total minutes'].iloc[1],sep20grouped['Total minutes'].iloc[1],oct20grouped['Total minutes'].iloc[1],
              nov20grouped['Total minutes'].iloc[1],dec20grouped['Total minutes'].iloc[1]]

df=pd.DataFrame({"months":allmonths,"total seconds":alltimes,"casual bikers":casual,"bikeshare members":members})

df.loc[:,'total daylight']=round(df['total seconds']/60,2)
df.loc[:,'total bikers']=round(df['casual bikers']+df['bikeshare members'],2)

df=df[['months','casual bikers','bikeshare members','total daylight','total bikers']]