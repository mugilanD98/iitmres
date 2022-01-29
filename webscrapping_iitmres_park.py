#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[3]:


import pandas as pd


# In[4]:


html_text=requests.get('https://www.renewablesindia.in/').text


# In[5]:


soup= BeautifulSoup(html_text,'lxml')


# In[6]:


location=soup.find('h1',class_='hand').text


# In[7]:


location


# In[8]:


location=location.strip()


# In[9]:


renewable=soup.find_all('div',class_='card-heading-1')


# In[10]:


renew_india=[]
for i in range(0,3):
    renew_india.append(renewable[i].text)


# In[11]:


renew_india.append(location)


# In[12]:


renew_india


# In[13]:


#chandigar


# In[14]:


html_text=requests.get('https://www.renewablesindia.in/?region=6&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location2=soup.find('h1',class_='hand').text
location2=location2.strip()

renewable=soup.find_all('div',class_='card-heading-1')

renew_chandigar=[]
for i in range(0,3):
    renew_chandigar.append(renewable[i].text)
    
renew_chandigar.append(location2)    


# In[15]:


#Northern Region


# In[16]:


html_text=requests.get('https://www.renewablesindia.in/?region=Northern&selection_type=region').text

soup= BeautifulSoup(html_text,'lxml')

location3=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Northern_Region=[]
for i in range(0,3):
    renew_Northern_Region.append(renewable[i].text)
    
location3=location3.strip()
renew_Northern_Region.append(location3)


# In[17]:


#Delhi


# In[18]:


html_text=requests.get('https://www.renewablesindia.in/?region=10&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location4=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Delhi=[]
for i in range(0,3):
    renew_Delhi.append(renewable[i].text)
    
location4=location4.strip()
renew_Delhi.append(location4)


# In[19]:


#Haryana


# In[20]:


html_text=requests.get('https://www.renewablesindia.in/?region=13&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location5=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Haryana=[]
for i in range(0,3):
    renew_Haryana.append(renewable[i].text)
    
location5=location5.strip()
renew_Haryana.append(location5)


# In[21]:


#Himachal Pradesh


# In[22]:


html_text=requests.get('https://www.renewablesindia.in/?region=14&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location6=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Himachal_Pradesh=[]
for i in range(0,3):
    renew_Himachal_Pradesh.append(renewable[i].text)
    
location6=location6.strip()
renew_Himachal_Pradesh.append(location6)    


# In[23]:


#Jammu & Kashmir


# In[24]:


html_text=requests.get('https://www.renewablesindia.in/?region=15&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location7=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Jammu_and_Kashmir=[]
for i in range(0,3):
    renew_Jammu_and_Kashmir.append(renewable[i].text)
    
location7=location7.strip()
renew_Jammu_and_Kashmir.append(location7)    


# In[25]:


#Punjab


# In[26]:


html_text=requests.get('https://www.renewablesindia.in/?region=28&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location8=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Punjab=[]
for i in range(0,3):
    renew_Punjab.append(renewable[i].text)
    
location8=location8.strip()
renew_Punjab.append(location8)    


# In[27]:


#Rajasthan


# In[28]:


html_text=requests.get('https://www.renewablesindia.in/?region=29&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location9=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Rajasthan=[]
for i in range(0,3):
    renew_Rajasthan.append(renewable[i].text)
    
location9=location9.strip()
renew_Rajasthan.append(location9)    


# In[29]:


#Uttar Pradesh


# In[30]:


html_text=requests.get('https://www.renewablesindia.in/?region=34&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location10=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Uttar_Pradesh=[]
for i in range(0,3):
    renew_Uttar_Pradesh.append(renewable[i].text)
    
location10=location10.strip()
renew_Uttar_Pradesh.append(location10)    


# In[31]:


#Uttarakhand 


# In[32]:


html_text=requests.get('https://www.renewablesindia.in/?region=35&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location11=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Uttarakhand=[]
for i in range(0,3):
    renew_Uttarakhand.append(renewable[i].text)
    
location11=location11.strip()
renew_Uttarakhand.append(location11)    


# In[33]:


#Western Region


# In[34]:


html_text=requests.get('https://www.renewablesindia.in/?region=Western&selection_type=region').text

soup= BeautifulSoup(html_text,'lxml')

location12=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Western_Region=[]
for i in range(0,3):
    renew_Western_Region.append(renewable[i].text)
    
location12=location12.strip()
renew_Western_Region.append(location12)    


# In[35]:


#Chhattisgarh


# In[36]:


html_text=requests.get('https://www.renewablesindia.in/?region=7&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location13=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Chhattisgarh=[]
for i in range(0,3):
    renew_Chhattisgarh.append(renewable[i].text)
    
location13=location13.strip()
renew_Chhattisgarh.append(location13)    


# In[37]:


#Gujarat 


# In[38]:


html_text=requests.get('https://www.renewablesindia.in/?region=12&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location14=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Gujarat=[]
for i in range(0,3):
    renew_Gujarat.append(renewable[i].text)
    
location14=location14.strip()
renew_Gujarat.append(location14)    


# In[39]:


#Madhya Pradesh


# In[40]:


html_text=requests.get('https://www.renewablesindia.in/?region=20&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location15=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Madhya_Pradesh=[]
for i in range(0,3):
    renew_Madhya_Pradesh.append(renewable[i].text)
    
location15=location15.strip()
renew_Madhya_Pradesh.append(location15)    


# In[41]:


#Maharashtra


# In[42]:


html_text=requests.get('https://www.renewablesindia.in/?region=21&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location16=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Maharashtra=[]
for i in range(0,3):
    renew_Maharashtra.append(renewable[i].text)
    
location16=location16.strip()
renew_Maharashtra.append(location16)    


# In[43]:


#Daman & Diu


# In[44]:


html_text=requests.get('https://www.renewablesindia.in/?region=9&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location17=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Daman_and_Diu=[]
for i in range(0,3):
    renew_Daman_and_Diu.append(renewable[i].text)
    
location17=location17.strip()
renew_Daman_and_Diu.append(location17)    


# In[45]:


#Dadra & Nagar Haveli


# In[46]:


html_text=requests.get('https://www.renewablesindia.in/?region=8&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location18=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Dadra_Nagar_Haveli=[]
for i in range(0,3):
    renew_Dadra_Nagar_Haveli.append(renewable[i].text)
    
location18=location18.strip()
renew_Dadra_Nagar_Haveli.append(location18)    


# In[47]:


#Goa


# In[48]:


html_text=requests.get('https://www.renewablesindia.in/?region=11&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location19=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Goa=[]
for i in range(0,3):
    renew_Goa.append(renewable[i].text)
    
location19=location19.strip()
renew_Goa.append(location19)    


# In[49]:


#Southern Region


# In[50]:


html_text=requests.get('https://www.renewablesindia.in/?region=Southern&selection_type=region').text

soup= BeautifulSoup(html_text,'lxml')

location20=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Southern_Region=[]
for i in range(0,3):
    renew_Southern_Region.append(renewable[i].text)
    
location20=location20.strip()
renew_Southern_Region.append(location20)        


# In[51]:


#Andhra Pradesh 


# In[52]:


html_text=requests.get('https://www.renewablesindia.in/?region=2&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location21=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Andhra_Pradesh=[]
for i in range(0,3):
    renew_Andhra_Pradesh.append(renewable[i].text)
    
location21=location21.strip()
renew_Andhra_Pradesh.append(location21)    


# In[53]:


#Telangana


# In[54]:


html_text=requests.get('https://www.renewablesindia.in/?region=32&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location22=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Telangana=[]
for i in range(0,3):
    renew_Telangana.append(renewable[i].text)
    
location22=location22.strip()
renew_Telangana.append(location22)    


# In[55]:


#Karnataka


# In[56]:


html_text=requests.get('https://www.renewablesindia.in/?region=17&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location23=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Karnataka=[]
for i in range(0,3):
    renew_Karnataka.append(renewable[i].text)
    
location23=location23.strip()
renew_Karnataka.append(location23)    


# In[57]:


#Tamil_Nadu


# In[58]:


html_text=requests.get('https://www.renewablesindia.in/?region=31&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location24=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Tamil_Nadu=[]
for i in range(0,3):
    renew_Tamil_Nadu.append(renewable[i].text)
    
location24=location24.strip()
renew_Tamil_Nadu.append(location24)    


# In[59]:


#Puducherry


# In[60]:


html_text=requests.get('https://www.renewablesindia.in/?region=27&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location25=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Puducherry=[]
for i in range(0,3):
    renew_Puducherry.append(renewable[i].text)
    
location25=location25.strip()
renew_Puducherry.append(location25)    


# In[61]:


#Lakshadweep


# In[62]:


html_text=requests.get('https://www.renewablesindia.in/?region=19&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location26=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Lakshadweep=[]
for i in range(0,3):
    renew_Lakshadweep.append(renewable[i].text)
    
location26=location26.strip()
renew_Lakshadweep.append(location26)    


# In[63]:


#Eastern_Region


# In[64]:


html_text=requests.get('https://www.renewablesindia.in/?region=Eastern&selection_type=region').text

soup= BeautifulSoup(html_text,'lxml')

location27=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Eastern_Region=[]
for i in range(0,3):
    renew_Eastern_Region.append(renewable[i].text)
    
location27=location27.strip()
renew_Eastern_Region.append(location27)    


# In[65]:


#Bihar


# In[66]:


html_text=requests.get('https://www.renewablesindia.in/?region=5&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location28=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Bihar=[]
for i in range(0,3):
    renew_Bihar.append(renewable[i].text)
    
location28=location28.strip()
renew_Bihar.append(location28)    


# In[67]:


#Jharkhand


# In[68]:


html_text=requests.get('https://www.renewablesindia.in/?region=16&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location29=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Jharkhand=[]
for i in range(0,3):
    renew_Jharkhand.append(renewable[i].text)
    
location29=location29.strip()
renew_Jharkhand.append(location29)    


# In[69]:


#Odisha


# In[70]:


html_text=requests.get('https://www.renewablesindia.in/?region=26&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location30=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Odisha=[]
for i in range(0,3):
    renew_Odisha.append(renewable[i].text)
    
location30=location30.strip()
renew_Odisha.append(location30)    


# In[71]:


#WestBengal


# In[72]:


html_text=requests.get('https://www.renewablesindia.in/?region=36&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location31=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_WestBengal=[]
for i in range(0,3):
    renew_WestBengal.append(renewable[i].text)
    
location31=location31.strip()
renew_WestBengal.append(location31)    


# In[73]:


#Sikkim


# In[74]:


html_text=requests.get('https://www.renewablesindia.in/?region=30&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location32=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Sikkim=[]
for i in range(0,3):
    renew_Sikkim.append(renewable[i].text)
    
location32=location32.strip()
renew_Sikkim.append(location32)    


# In[75]:


#Andaman_and_Nicobar


# In[76]:


html_text=requests.get('https://www.renewablesindia.in/?region=1&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location33=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Andaman_and_Nicobar=[]
for i in range(0,3):
    renew_Andaman_and_Nicobar.append(renewable[i].text)
    
location33=location33.strip()
renew_Andaman_and_Nicobar.append(location33)    


# In[77]:


#North_eastern_Region


# In[78]:


html_text=requests.get('https://www.renewablesindia.in/?region=North-Eastern&selection_type=region').text

soup= BeautifulSoup(html_text,'lxml')

location34=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_North_eastern_Region=[]
for i in range(0,3):
    renew_North_eastern_Region.append(renewable[i].text)
    
location34=location34.strip()
renew_North_eastern_Region.append(location34)    


# In[79]:


#Arunachal_Pradesh


# In[80]:


html_text=requests.get('https://www.renewablesindia.in/?region=3&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location35=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Arunachal_Pradesh=[]
for i in range(0,3):
    renew_Arunachal_Pradesh.append(renewable[i].text)
    
location35=location35.strip()
renew_Arunachal_Pradesh.append(location35)    


# In[81]:


#Assam


# In[82]:


html_text=requests.get('https://www.renewablesindia.in/?region=4&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location36=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Assam=[]
for i in range(0,3):
    renew_Assam.append(renewable[i].text)
    
location36=location36.strip()
renew_Assam.append(location36)    


# In[83]:


#Manipur


# In[84]:


html_text=requests.get('https://www.renewablesindia.in/?region=22&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location37=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Manipur=[]
for i in range(0,3):
    renew_Manipur.append(renewable[i].text)
    
location37=location37.strip()
renew_Manipur.append(location37)    


# In[85]:


#Meghalaya


# In[86]:


html_text=requests.get('https://www.renewablesindia.in/?region=23&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location38=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Meghalaya=[]
for i in range(0,3):
    renew_Meghalaya.append(renewable[i].text)
    
location38=location38.strip()
renew_Meghalaya.append(location38)    


# In[87]:


#Mizoram


# In[88]:


html_text=requests.get('https://www.renewablesindia.in/?region=24&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location39=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Mizoram=[]
for i in range(0,3):
    renew_Mizoram.append(renewable[i].text)
    
location39=location39.strip()
renew_Mizoram.append(location39)    


# In[89]:


#Nagaland 


# In[90]:


html_text=requests.get('https://www.renewablesindia.in/?region=25&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location40=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Nagaland=[]
for i in range(0,3):
    renew_Nagaland.append(renewable[i].text)
    
location40=location40.strip()
renew_Nagaland.append(location40)    


# In[91]:


#Tripura


# In[92]:


html_text=requests.get('https://www.renewablesindia.in/?region=33&selection_type=state').text

soup= BeautifulSoup(html_text,'lxml')

location41=soup.find('h1',class_='hand').text

renewable=soup.find_all('div',class_='card-heading-1')

renew_Tripura=[]
for i in range(0,3):
    renew_Tripura.append(renewable[i].text)
    
location41=location41.strip()
renew_Tripura.append(location41)    


# In[93]:


renew_india,renew_Northern_Region,renew_chandigar,renew_Delhi,renew_Haryana,renew_Himachal_Pradesh,renew_Jammu_and_Kashmir,renew_Punjab,renew_Rajasthan,renew_Uttar_Pradesh,renew_Uttarakhand,renew_Western_Region,renew_Chhattisgarh,renew_Gujarat,renew_Madhya_Pradesh,renew_Maharashtra,renew_Daman_and_Diu,renew_Dadra_Nagar_Haveli,renew_Goa,renew_Southern_Region,renew_Andhra_Pradesh,renew_Telangana,renew_Karnataka,renew_Tamil_Nadu,renew_Puducherry,renew_Lakshadweep,renew_Eastern_Region,renew_Bihar,renew_Jharkhand,renew_Odisha,renew_WestBengal,renew_Sikkim,renew_Andaman_and_Nicobar,renew_North_eastern_Region,renew_Arunachal_Pradesh,renew_Assam,renew_Manipur,renew_Meghalaya,renew_Mizoram,renew_Nagaland,renew_Tripura


# In[99]:


data=[renew_india,renew_Northern_Region,renew_chandigar,renew_Delhi,renew_Haryana,renew_Himachal_Pradesh,renew_Jammu_and_Kashmir,renew_Punjab,renew_Rajasthan,renew_Uttar_Pradesh,renew_Uttarakhand,renew_Western_Region,renew_Chhattisgarh,renew_Gujarat,renew_Madhya_Pradesh,renew_Maharashtra,renew_Daman_and_Diu,renew_Dadra_Nagar_Haveli,renew_Goa,renew_Southern_Region,renew_Andhra_Pradesh,renew_Telangana,renew_Karnataka,renew_Tamil_Nadu,renew_Puducherry,renew_Lakshadweep,renew_Eastern_Region,renew_Bihar,renew_Jharkhand,renew_Odisha,renew_WestBengal,renew_Sikkim,renew_Andaman_and_Nicobar,renew_North_eastern_Region,renew_Arunachal_Pradesh,renew_Assam,renew_Manipur,renew_Meghalaya,renew_Mizoram,renew_Nagaland,renew_Tripura]


# In[100]:


data


# In[101]:


scrdata=pd.DataFrame(data,columns=['co2','solar','wind','location'])


# In[102]:


scrdata


# In[ ]:




