#Author Md Anowar Hossen Faysal@30069394



# Import all classes and methods from the tkinter module

from tkinter import *

# Import the pandas module and assign it the alias "pd" for convenience
import pandas as pd

# Import the numpy module and assign it the alias "np" for convenience
import numpy as np

# Import the pyplot module from matplotlib and assign it the alias "plt" for convenience
import matplotlib.pyplot as plt

# Import the seaborn module and assign it the alias "sns" for convenience
import seaborn as sns


# Import the webbrowser module which provides a high-level interface to display web-based documents
import webbrowser


# Import the folium module which allows to create leaflet maps in python
import folium

# Import the plugins module of folium and assign it the alias "plugins" for convenience
import folium.plugins as plugins






# Create an instance of the Tk class and assign it to the variable "root"
root = Tk()

# Set the dimensions of the window to 1000 pixels width and 500 pixels height
root.geometry("1000x500")

# Set the title of the window to "Bedfordshire & Essex police force Crime Analysis"
root.title("Bedfordshire & Essex police force Crime Analysis")

# Set the window not to be resizable in width and height
root.resizable(False, False)




### read csv file at Bedfordshire data set
Bedfordshire=pd.read_csv('Data\Marge_Bedfordshire.csv')
print('Bedfordshire Police Data set',Bedfordshire.head(10))

### read csv file at Essex data set
Essex = pd.read_csv('Data\margedata_Essex.csv')
print('Essex police Data set',Essex.head(10))


#check Bedfordshire data set information
B_info=Bedfordshire.info()
print('Check Bedforshire information',B_info)

#check Essex data set information
E_info=Essex.info()
print('Check Essex information',E_info)


# check null value of Bedfordshire
B_Null=Bedfordshire.isnull().sum()
print('Bedfordshire_null_value:',B_Null)
# check null value of Essex
E_Null=Essex.isnull().sum()
print('Essex_null_value:',E_Null)


#Bedfordshire data frame
df_b = pd.DataFrame(Bedfordshire)
# rename the column name at the Bedfordshire data set
df_B = df_b.rename(columns={'Crime type': 'Crime_type', 'Last outcome category': 'Last_outcome_category'})


#essex data frame
df_e = pd.DataFrame(Essex)
# rename the column name at the Essex data set
df_E = df_e.rename(columns={'Crime type': 'Crime_type', 'Last outcome category': 'Last_outcome_category'})


# total crime count of bedfordshir
B_Total_crime_count=df_B['Crime_type'].value_counts(dropna=False).reset_index(name='B_Crime_Count')
B_Total_crime_count
print('Bedfordshire Total crime count: ',B_Total_crime_count.sum())


# total crime count of Essex
E_Total_crime_count=df_E['Crime_type'].value_counts(dropna=False).reset_index(name='E_Crime_Count')
print('Essex Total crime count: ',E_Total_crime_count.sum())





R_button1=IntVar()
R_button1.set("1")
R_button2=IntVar()
R_button2.set("0")
R_button3=IntVar()
R_button3.set("300")



############################################################## radio button selection ##############################################
def Radio_selection():
    s= R_button1.get()
    s1=R_button2.get()
    s3= R_button3.get()

############################################################## crime type radio button handle  ######################################
    if(s==1):
        print('All crime type')
    elif(s==2):
        print('violence & sex')
    elif(s==3):
        print('anti_social')
    elif(s==4):
        print('public order')
    elif(s==5):
        print('vehicle')
    elif(s==6):
        print('criminal')
    elif(s==7):
        print('Theft')
    elif(s==8):
        print('possession')
    elif(s==9):
        print('shoplifting')
    elif(s==10):
        print('drug')
    elif(s==11):
        print('other crime')
    elif(s==12):
        print('Bycle')
    elif(s==13):
        print('robbery')
    elif(s==14):
        print('other thrft')
    elif(s==15):
        print('burglary')
    

############################################################# select year radio button hnadle  ############################################
    if(s1==0):
        print('All year')
    elif(s1==2020):
        print('2020')
    elif(s1==2021):
        print('2021')
    elif(s1==2022):
        print('2022')



############################################################# police force radio button handle  #############################################
   
    if(s3==300):
        print('Badforshare')
    elif(s3==301):
        print('Essex')
    

########################################################  function of the graphical analysis of bar chart ##################################
def Bar_selection():
    print('Bar Selection')

    # Bedfordshire data set
    if R_button3.get() == 300 and R_button2.get() == 0:
        Bedfordshire_All_crime_filter_2020_to_2022 = df_B['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        All_year_Crime_filter=df_B.query("(Month >= '2020-01' and Month <= '2022-06')")
        print("Bedfordshire_All_crime_filter_2020_to_2022",Bedfordshire_All_crime_filter_2020_to_2022)
        Bedfordshie_BarChart_all(Bedfordshire_All_crime_filter_2020_to_2022,All_year_Crime_filter)

    if R_button3.get() == 300 and R_button2.get() == 2020:
        Bedfordshire_Individual_crime_filter_2020 = df_B.query("Month >= '2020-01' and Month <= '2020-12'")
        barChart(Bedfordshire_Individual_crime_filter_2020)

    if R_button3.get() == 300 and R_button2.get() == 2021:
        Bedfordshire_Individual_crime_filter_2021 = df_B.query("Month >= '2021-01' and Month <= '2021-12'")
        barChart1(Bedfordshire_Individual_crime_filter_2021)
        

    if R_button3.get() == 300 and R_button2.get() == 2022:
        Bedfordshire_Individual_crime_filter_2022 = df_B.query("Month >= '2022-01' and Month <= '2022-06'")
        barChart2(Bedfordshire_Individual_crime_filter_2022)


        # Essex  data set
    if R_button3.get() == 301 and R_button2.get() == 0:
        Essex_crime_filter_2020_to_2022 = df_E['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        Essex_All_year_Crime_filter=df_E.query("(Month >= '2020-01' and Month <= '2022-06')")
        print(Essex_crime_filter_2020_to_2022)
        Essex_BarChart_all(Essex_crime_filter_2020_to_2022,Essex_All_year_Crime_filter)
    
    if R_button3.get() == 301 and R_button2.get() == 2020:
        print('ok')
        Essex_Individual_crime_filter_2020 = df_E.query("Month >= '2020-01' and Month <= '2020-12'")
        BarChart_Essex2020(Essex_Individual_crime_filter_2020)

    if R_button3.get() == 301 and R_button2.get() == 2021:
        Essex_Individual_crime_filter_20201 = df_E.query("Month >= '2021-01' and Month <= '2021-12'")
        BarChart_Essex2021(Essex_Individual_crime_filter_20201)
    
    if R_button3.get() == 301 and R_button2.get() == 2022:
        Essex_Individual_crime_filter_20202 = df_E.query("Month >= '2022-01' and Month <= '2022-06'")
        BarChart_Essex2022(Essex_Individual_crime_filter_20202)
       
 # Bedfordshire crime_filter_2020_to_2022 and Bedfordshire All_year_Crime_filter and draw bar chart 
    
def Bedfordshie_BarChart_all(Bedfordshire_All_crime_filter_2020_to_2022, All_year_Crime_filter):
    print('Barchart Bedfordshire All crime type')
    if R_button1.get() == 1:
        # count_all_crimetype=Bedfordshire_All_crime_filter_2020_to_2022['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        # print(count_all_crimetype)

        x= Bedfordshire_All_crime_filter_2020_to_2022['Crime_type']
        y = Bedfordshire_All_crime_filter_2020_to_2022['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Bedfordshire All Crime type 2020 to 2022')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show() 


    if R_button1.get() == 2:
        crime_filter2= All_year_Crime_filter.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Violence and sexual offences 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 3:
        crime_filter3= All_year_Crime_filter.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Anti-social behaviour 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= All_year_Crime_filter.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Public order 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= All_year_Crime_filter.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Vehicle crime 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 6:
        crime_filter6= All_year_Crime_filter.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Criminal damage and arson 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 7:
        crime_filter7= All_year_Crime_filter.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Theft from the person 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 8:
        crime_filter8= All_year_Crime_filter.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Possession of weapons 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 9:
        crime_filter9= All_year_Crime_filter.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Shoplifting 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= All_year_Crime_filter.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Drugs 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= All_year_Crime_filter.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Other crime 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 12:
        crime_filter12= All_year_Crime_filter.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Bicycle theft 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 13:
        crime_filter13= All_year_Crime_filter.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Robbery 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= All_year_Crime_filter.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Other theft 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 15:
        crime_filter15= All_year_Crime_filter.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Bedfordshire Burglary 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

# Bedfordshire_Individual_crime_filter_2020 and Barchart draw
def barChart(Bedfordshire_Individual_crime_filter_2020):
    print('Success 2020')

    if R_button1.get() == 1:
        count2020=Bedfordshire_Individual_crime_filter_2020['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        print(count2020)

        x= count2020['Crime_type']
        y = count2020['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Bedfordshire All Crime type 2020')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show()       


    if R_button1.get() == 2:
        crime_filter2= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)

        plt.title(label='Bedfordshire Violence and sexual offences 2020')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 3:
        crime_filter3= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Anti-social behaviour 2020')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Public order 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Vehicle crime 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 6:
        crime_filter6= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Criminal damage and arson 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 7:
        crime_filter7= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Theft from the person 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 8:
        crime_filter8= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Possession of weapons 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 9:
        crime_filter9= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Shoplifting 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Drugs 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Other crime 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 12:
        crime_filter12= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Bicycle theft 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 13:
        crime_filter13= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Robbery 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Other theft 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 15:
        crime_filter15= Bedfordshire_Individual_crime_filter_2020.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Burglary 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()
 
# Bedfordshire_Individual_crime_filter_2021 and Barchart draw
def barChart1(Bedfordshire_Individual_crime_filter_2021):
    print('Success 2021')

    if R_button1.get() == 1:
        count2021=Bedfordshire_Individual_crime_filter_2021['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        print(count2021)

        x= count2021['Crime_type']
        y = count2021['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Bedfordshire All Crime type 2021')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show()  




    if R_button1.get() == 2:
        crime_filter2= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print('ok')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Violence and sexual offences 2021')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 3:
        crime_filter3= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Anti-social behaviour 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Public order 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Vehicle crime 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 6:
        crime_filter6= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Criminal damage and arson 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 7:
        crime_filter7= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Theft from the person 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 8:
        crime_filter8= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Possession of weapons 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 9:
        crime_filter9= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Shoplifting 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Drugs 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Other crime 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 12:
        crime_filter12= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Bicycle theft 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 13:
        crime_filter13= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Robbery 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Other theft 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 15:
        crime_filter15= Bedfordshire_Individual_crime_filter_2021.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Burglary 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

# Bedfordshire_Individual_crime_filter_2022 and Barchart draw
def barChart2(Bedfordshire_Individual_crime_filter_2022):
    print('Success 20202')

    if R_button1.get() == 1:
        count2022=Bedfordshire_Individual_crime_filter_2022['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        print(count2022)

        x= count2022['Crime_type']
        y = count2022['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Bedfordshire All Crime type 2022')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show()  

    if R_button1.get() == 2:
        crime_filter2= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print('ok')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Violence and sexual offences 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 3:
        crime_filter3= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Anti-social behaviour 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Public order 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Bedfordshire Vehicle crime 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 6:
        crime_filter6= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Criminal damage and arson 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 7:
        crime_filter7= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Theft from the person 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 8:
        crime_filter8= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Possession of weapons 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 9:
        crime_filter9= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Shoplifting 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Drugs 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Other crime 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 12:
        crime_filter12= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Bicycle theft 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 13:
        crime_filter13= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Robbery 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Other theft 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 15:
        crime_filter15= Bedfordshire_Individual_crime_filter_2022.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Bedfordshire Burglary 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()



#  Essex_crime_filter_2020_to_2022 and Essex_All_year_Crime_filter and draw bar chart
def Essex_BarChart_all(Essex_crime_filter_2020_to_2022,Essex_All_year_Crime_filter):
    print('Barchart Essex All crime type')
    if R_button1.get() == 1:
        # count_all_crimetype=Bedfordshire_All_crime_filter_2020_to_2022['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        # print(count_all_crimetype)

        x= Essex_crime_filter_2020_to_2022['Crime_type']
        y = Essex_crime_filter_2020_to_2022['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Essex All Crime type 2020 to 2022')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show() 


    if R_button1.get() == 2:
        crime_filter2= Essex_All_year_Crime_filter.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Violence and sexual offences 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 3:
        crime_filter3= Essex_All_year_Crime_filter.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Anti-social behaviour 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= Essex_All_year_Crime_filter.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Public order 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= Essex_All_year_Crime_filter.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Vehicle crime 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 6:
        crime_filter6= Essex_All_year_Crime_filter.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Criminal damage and arson 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 7:
        crime_filter7= Essex_All_year_Crime_filter.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Theft from the person 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 8:
        crime_filter8= Essex_All_year_Crime_filter.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Possession of weapons 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 9:
        crime_filter9= Essex_All_year_Crime_filter.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Shoplifting 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= Essex_All_year_Crime_filter.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Drugs 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= Essex_All_year_Crime_filter.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Other crime 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 12:
        crime_filter12= Essex_All_year_Crime_filter.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Bicycle theft 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 13:
        crime_filter13= Essex_All_year_Crime_filter.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Robbery 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= Essex_All_year_Crime_filter.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Other theft 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 15:
        crime_filter15= Essex_All_year_Crime_filter.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.xticks(rotation=90)
        plt.title(label='Essex Burglary 2020- 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

# Essex_Individual_crime_filter_2020 and Barchart draw
def BarChart_Essex2020(Essex_Individual_crime_filter_2020):
    print('Success 2020')

    if R_button1.get() == 1:
        count2020=Essex_Individual_crime_filter_2020['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        print(count2020)

        x= count2020['Crime_type']
        y = count2020['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Essex All Crime type 2020')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show()       


    if R_button1.get() == 2:
        crime_filter2= Essex_Individual_crime_filter_2020.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)

        plt.title(label='Essex Violence and sexual offences 2020')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 3:
        crime_filter3= Essex_Individual_crime_filter_2020.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Anti-social behaviour 2020')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= Essex_Individual_crime_filter_2020.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Public order 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= Essex_Individual_crime_filter_2020.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Vehicle crime 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 6:
        crime_filter6= Essex_Individual_crime_filter_2020.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Criminal damage and arson 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 7:
        crime_filter7= Essex_Individual_crime_filter_2020.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Theft from the person 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 8:
        crime_filter8= Essex_Individual_crime_filter_2020.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Possession of weapons 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 9:
        crime_filter9= Essex_Individual_crime_filter_2020.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Shoplifting 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= Essex_Individual_crime_filter_2020.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Drugs 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= Essex_Individual_crime_filter_2020.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Other crime 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 12:
        crime_filter12= Essex_Individual_crime_filter_2020.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Bicycle theft 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 13:
        crime_filter13= Essex_Individual_crime_filter_2020.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Robbery 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= Essex_Individual_crime_filter_2020.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Other theft 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 15:
        crime_filter15= Essex_Individual_crime_filter_2020.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Burglary 2020')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

# Essex_Individual_crime_filter_2021 and Barchart draw
def BarChart_Essex2021(Essex_Individual_crime_filter_20201):

    print('Success 2021')

    if R_button1.get() == 1:
        count2021=Essex_Individual_crime_filter_20201['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        print(count2021)

        x= count2021['Crime_type']
        y = count2021['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Essex All Crime type 2021')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show()  




    if R_button1.get() == 2:
        crime_filter2= Essex_Individual_crime_filter_20201.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print('ok')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Violence and sexual offences 2021')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 3:
        crime_filter3= Essex_Individual_crime_filter_20201.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Anti-social behaviour 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= Essex_Individual_crime_filter_20201.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Public order 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= Essex_Individual_crime_filter_20201.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Vehicle crime 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 6:
        crime_filter6= Essex_Individual_crime_filter_20201.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Criminal damage and arson 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 7:
        crime_filter7= Essex_Individual_crime_filter_20201.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Theft from the person 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 8:
        crime_filter8= Essex_Individual_crime_filter_20201.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Possession of weapons 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 9:
        crime_filter9= Essex_Individual_crime_filter_20201.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Shoplifting 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= Essex_Individual_crime_filter_20201.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Drugs 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= Essex_Individual_crime_filter_20201.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Other crime 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 12:
        crime_filter12= Essex_Individual_crime_filter_20201.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Bicycle theft 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 13:
        crime_filter13= Essex_Individual_crime_filter_20201.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Robbery 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= Essex_Individual_crime_filter_20201.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Other theft 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 15:
        crime_filter15= Essex_Individual_crime_filter_20201.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Burglary 2021')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

# Essex_Individual_crime_filter_2022 and Barchart draw
def BarChart_Essex2022(Essex_Individual_crime_filter_20202):
    print('Success 20202')

    if R_button1.get() == 1:
        count2022=Essex_Individual_crime_filter_20202['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
        print(count2022)

        x= count2022['Crime_type']
        y = count2022['counts']
        plt.figure(figsize= (20,8))
        # count.plot(kind='barh')
        plt.barh(x,y)
        plt.title(label=' Essex All Crime type 2022')
        plt.ylabel("Crime Type")
        plt.xlabel("Frequency")
        plt.show()  

    if R_button1.get() == 2:
        crime_filter2= Essex_Individual_crime_filter_20202.query("Crime_type =='Violence and sexual offences'")
        count2=crime_filter2['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print('ok')
        print(count2)
        x= count2['Month']
        y = count2['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Violence and sexual offences 2022')
        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 3:
        crime_filter3= Essex_Individual_crime_filter_20202.query("Crime_type =='Anti-social behaviour'")
        count3=crime_filter3['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count3)
        x= count3['Month']
        y = count3['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Anti-social behaviour 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 4:
        crime_filter4= Essex_Individual_crime_filter_20202.query("Crime_type =='Public order'")
        count4=crime_filter4['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count4)
        x= count4['Month']
        y = count4['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Public order 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 5:
        crime_filter5= Essex_Individual_crime_filter_20202.query("Crime_type =='Vehicle crime'")
        count5=crime_filter5['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count5)
        x= count5['Month']
        y = count5['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label='Essex Vehicle crime 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 6:
        crime_filter6= Essex_Individual_crime_filter_20202.query("Crime_type =='Criminal damage and arson'")
        count6=crime_filter6['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count6)
        x= count6['Month']
        y = count6['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Criminal damage and arson 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 7:
        crime_filter7= Essex_Individual_crime_filter_20202.query("Crime_type =='Theft from the person'")
        count7=crime_filter7['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count7)
        x= count7['Month']
        y = count7['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Theft from the person 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 8:
        crime_filter8= Essex_Individual_crime_filter_20202.query("Crime_type =='Possession of weapons'")
        count8=crime_filter8['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count8)
        x= count8['Month']
        y = count8['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Possession of weapons 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 9:
        crime_filter9= Essex_Individual_crime_filter_20202.query("Crime_type =='Shoplifting'")
        count9=crime_filter9['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count9)
        x= count9['Month']
        y = count9['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Shoplifting 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 10:
        crime_filter10= Essex_Individual_crime_filter_20202.query("Crime_type =='Drugs'")
        count10=crime_filter10['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count10)
        x= count10['Month']
        y = count10['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Drugs 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 11:
        crime_filter11= Essex_Individual_crime_filter_20202.query("Crime_type =='Other crime'")
        count11=crime_filter11['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count11)
        x= count11['Month']
        y = count11['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Other crime 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 12:
        crime_filter12= Essex_Individual_crime_filter_20202.query("Crime_type =='Bicycle theft'")
        count12=crime_filter12['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count12)
        x= count12['Month']
        y = count12['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Bicycle theft 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 13:
        crime_filter13= Essex_Individual_crime_filter_20202.query("Crime_type =='Robbery'")
        count13=crime_filter13['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count13)
        x= count13['Month']
        y = count13['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Robbery 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()

    if R_button1.get() == 14:
        crime_filter14= Essex_Individual_crime_filter_20202.query("Crime_type =='Other theft'")
        count14=crime_filter14['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count14)
        x= count14['Month']
        y = count14['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Other theft 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()


    if R_button1.get() == 15:
        crime_filter15= Essex_Individual_crime_filter_20202.query("Crime_type =='Burglary'")
        count15=crime_filter15['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
        print(count15)
        x= count15['Month']
        y = count15['counts']
        plt.figure(figsize= (15,8))
        # count.plot(kind='barh')
        plt.bar(x,y)
        plt.title(label=' Essex Burglary 2022')

        plt.ylabel("Frequency")
        plt.xlabel("Year & Month")
        plt.show()








# Compare both forces all year and all crime

############################################# Compare_Bedfordshire_essex all year and all crime  #################################################
def Compare_Bedfordshire_essex():
    print("Compare_Bedfordshire_essex all year and all crime ")
# Bedfordshire Data for the first pie chart
    B_I_count=df_B['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
    B_I_count

    # all crime types
    labels= B_I_count.Crime_type
    labels
    print(labels)

    # bedfordshire crime data count
    B_I_count=df_B['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
    B_I_count.counts

    # bedfordshire crime data sum
    Bedfordshire_sum= B_I_count.counts.sum()
    Bedfordshire_sum

    # bedfordshire value crime value percenage and round
    Bedfordshire_percenatge = round((B_I_count.counts / Bedfordshire_sum)*100)
    Bedfordshire_percenatge

    # Essex crime data count
    E_I_count=df_E['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='counts')
    E_I_count.counts

    #essex all crime sum
    Essex_sum= E_I_count.counts.sum()
    Essex_sum

    # Essex all crime value percentange and round
    Essex_percenatge = round((E_I_count.counts / Essex_sum)*100)
    Essex_percenatge


    # Bar char 

    X = labels
    YBedfordshire = Bedfordshire_percenatge
    ZEssex = Essex_percenatge

    X_axis = np.arange(len(X))
    plt.subplots(figsize=(15, 8))
    plt.bar(X_axis - 0.2, YBedfordshire, 0.4, label = 'Bedfordshire')
    plt.bar(X_axis + 0.2, ZEssex, 0.4, label = 'Essex')

    plt.xticks(X_axis, X, rotation=60, fontsize=8)
    plt.xlabel("Crime types")
    plt.ylabel("Frequency")
    plt.title("Compare Bedfordshire & Essex all crime and all year")

    
    # Adding percentage above the bars 
    for i, v in enumerate(YBedfordshire):
        plt.text(i - 0.3, v + 1, str(v) + '%', rotation=90)
    for i, v in enumerate(ZEssex):
        plt.text(i + 0.1, v + 1, str(v) + '%', rotation=90)

    plt.show()

   
########################################################## compare Breakdown of crime Bedfordshire & Essex  ####################################
def Compare_breakdown_crime():
    #bedfordshire month and 
    Compare_Bedfordshire=df_B.groupby(['Month'])['Crime_type'].count().reset_index(name='Count_crime')
    Compare_Bedfordshire=Compare_Bedfordshire.sort_values(by='Month', ascending=True)
    Compare_Bedfordshire
    print("Bedfordshire_break down of crime:",Compare_Bedfordshire)

    Compare_Essex=df_E.groupby(['Month'])['Crime_type'].count().reset_index(name='Count_crime')
    Compare_Essex=Compare_Essex.sort_values(by='Month', ascending=True)
    Compare_Essex
    print("Essex_break down of crime:",Compare_Essex)

    # Bedfordshire Data for the first line chart
    x1= Compare_Bedfordshire['Month']
    y1 = Compare_Bedfordshire['Count_crime']

    # Essex Data for the second line chart
    x2= Compare_Essex['Month']
    y2 = Compare_Essex['Count_crime']
    # Create a figure and a subplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

    # Plot the first line chart
    ax1.plot(x1, y1, label='Line 1', marker='o', linewidth=3)
    # set individual plot title
    ax1.set_title('Bedfordshire')
    # Set the x-axis labels and rotate them
    ax1.set_xticklabels(x1, rotation=90)


    # Plot the second line chart
    ax2.plot(x2, y2, label='Line 2', marker='o', linewidth=3)
    # set individual plot title
    ax2.set_title('Essex')
    # Set the x-axis labels and rotate them
    ax2.set_xticklabels(x2, rotation=90)
    # Add a title
    fig.suptitle('Compare Bedfordshire & Essex 2020 to 2022')

    # Show the plot
    plt.show()

######################################################### covid time crime handling #######################################################
def Compare_Covid_crime():
    print(" covid ")

    # covid19 bedfordshire & essex

    B_covid=df_B.query("(Month >= '2020-03' and Month <= '2021-12')")
    B_covid
    E_covid= df_E.query("(Month >= '2020-03' and Month <= '2021-12')")
    E_covid

    #Bedfordshire_covid value monthly count and Essex_covid count and ascending order

    Bedfordshire_covid=B_covid['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
    Bedfordshire_covid=Bedfordshire_covid.sort_values(by='Month', ascending=True)
    Bedfordshire_covid
    print('Bedfordshire_covid',Bedfordshire_covid)

    Essex_covid=E_covid['Month'].value_counts(dropna=False).rename_axis('Month').reset_index(name='counts')
    Essex_covid=Essex_covid.sort_values(by='Month', ascending=True)
    Essex_covid
    print('Essex_covid',Essex_covid)

    # Data for the first line chart
    x1= Bedfordshire_covid['Month']
    y1 = Bedfordshire_covid['counts']

    # Data for the second line chart
    x2= Essex_covid['Month']
    y2 = Essex_covid['counts']
    # Create a figure and a subplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Plot the first line chart
    ax1.plot(x1, y1, label='Line 1', marker='o', linewidth=3)
    # set individual plot title
    ax1.set_title('Bedfordshire')
    # Set the x-axis labels and rotate them
    ax1.set_xticklabels(x1, rotation=90)


    # Plot the second line chart
    ax2.plot(x2, y2, label='Line 2', marker='o', linewidth=3)
    # set individual plot title
    ax2.set_title('Essex')
    # Set the x-axis labels and rotate them
    ax2.set_xticklabels(x2, rotation=90)
    # Add a title
    fig.suptitle('Compare Bedfordshire & Essex Covid time crime')

    # Show the plot
    plt.show()

##################################################################summer and winter crime handling###########################################
def Compare_Summer_Winter_crime():
    print("winter & Morning")


        # summer bedfordshire & essex

    B_summer=df_B.query("(Month >= '2020-06' and Month <= '2020-08') or (Month >= '2021-06' and Month <= '2021-08') or (Month >= '2022-06')")
    B_summer
    E_summer= df_E.query("(Month >= '2020-06' and Month <= '2020-08') or (Month >= '2021-06' and Month <= '2021-08') or (Month >= '2022-06')")
    E_summer


    # Winter  bedfordshire & essex

    B_Winter= df_B.query("(Month == '2020-12') or (Month == '2021-01') or (Month == '2021-02') or (Month == '2021-12') or (Month == '2022-01') or (Month == '2022-02')")
    print(B_Winter)
    E_Winter= df_E.query("(Month == '2020-12') or (Month == '2021-01') or (Month == '2021-02') or (Month == '2021-12') or (Month == '2022-01') or (Month == '2022-02')")
    E_Winter

        # Bedfordshire summer crime data monthly groupby and count
    Bedfordshire_summer=B_summer.groupby(['Month'])['Crime_type'].count().reset_index(name='Count_crime')
    Bedfordshire_summer=Bedfordshire_summer.sort_values(by='Month', ascending=True)
    Bedfordshire_summer
    # Bedfordshire summer crime data sum
    Bedfordshire_summer_crime_count= Bedfordshire_summer.Count_crime.sum()
    print('Bedfordshire_summer_crime_count=',Bedfordshire_summer_crime_count)
    print('Bedfordshire_summer',Bedfordshire_summer)

    # Essex summer crime data monthly groupby and count
    Essex_summer=E_summer.groupby(['Month'])['Crime_type'].count().reset_index(name='Count_crime')
    Essex_summer=Essex_summer.sort_values(by='Month', ascending=True)
    Essex_summer
    # Essex summer crime data sum
    Essex_summer_crime_count= Essex_summer.Count_crime.sum()
    print('Essex_summer_crime_count',Essex_summer_crime_count)

    print('Essex_summer',Essex_summer)

    #Bedfordshire_Winter crime data monthly count and ascending order
    Bedfordshire_Winter=B_Winter.groupby(['Month'])['Crime_type'].count().reset_index(name='Count_crime')
    Bedfordshire_Winter=Bedfordshire_Winter.sort_values(by='Month', ascending=True)
    Bedfordshire_Winter
    #  Bedfordshire winter crime data sum
    Bedfordshire_Winter_crime_count= Bedfordshire_Winter.Count_crime.sum()
    print('Bedfordshire_Winter_crime_count=',Bedfordshire_Winter_crime_count)
    print('Compare_Bedfordshire_Winter',Bedfordshire_Winter)


    #Essex_Winter crime data monthly count and ascending order
    Essex_Winter=E_Winter.groupby(['Month'])['Crime_type'].count().reset_index(name='Count_crime')
    Essex_Winter=Essex_Winter.sort_values(by='Month', ascending=True)
    Essex_Winter
    # Essex winter crime data sum
    Essex_Winter_crime_count= Essex_Winter.Count_crime.sum()
    print('Essex_Winter_crime_count=',Essex_Winter_crime_count)

    print('Essex_Winter',Essex_Winter)


    # data bedfordshire
    B_summer_count = Bedfordshire_summer_crime_count
    B_winter_count = Bedfordshire_Winter_crime_count

    # data Essex
    E_summer_count = Essex_summer_crime_count
    E_winter_count = Essex_Winter_crime_count

    # labels for the slices
    labels = ['Summer', 'Winter']

    # bedforshire data for the slices
    counts_bedforshire = [B_summer_count, B_winter_count]

    # essex data for the slices
    counts_essex = [E_summer_count, E_winter_count]

    # Create a figure with a width of 30 inches and a height of 25  inches
    plt.figure(figsize=(10, 7))

    # create bedfordshire pie chart
    plt.subplot(2, 2, 1)
    plt.pie(counts_bedforshire, labels=labels, autopct='%1.1f%%')
    plt.title('Bedfordshire Summer and Winter')
    plt.legend(labels, loc='upper center', bbox_to_anchor=(0.5, -0.04), ncol=2, fontsize='x-large')

    # create essex pie chart
    plt.subplot(2, 2, 2)
    plt.pie(counts_essex, labels=labels, autopct='%1.1f%%')
    plt.title('Essex Summer and winter')
    plt.legend(labels, loc='upper center', bbox_to_anchor=(0.5, -0.04), ncol=2, fontsize='x-large')

    # Add a title
    plt.suptitle('Compare Bedfordshire & Essex for Summer and winter')
    # show the plot
    plt.show()


####################################################################Last outcome catagory handling ######################################

def lastoutcome():

    print("Last coutcome catagory comapre")
    # bedfordshire last coutcome null value hendling
    df_B_lastcoucome = df_B[['Last_outcome_category']].fillna('No Outcome')
    df_B_lastcoucome

    #bedfordshire last coutcome count
    Bedfordshire_lastoutcome_count = df_B_lastcoucome['Last_outcome_category'].value_counts(dropna=False).rename_axis('Last_outcome_category').reset_index(name='counts')
    # Sort_Bedfordshire_lastoutcome_count=Bedfordshire_lastoutcome_count.sort_values(by='Last_outcome_category', ascending=True)
    # Sort_Bedfordshire_lastoutcome_count
    Bedfordshire_lastoutcome_count
    

    labels= Bedfordshire_lastoutcome_count.Last_outcome_category
    labels

    Bedfordshire_lastoutcome_count.counts

    # #bedfordshire last coutcome all count value sum
    Bedfordshire_lastoutcome_count.counts.sum()

    # #bedfordshire last coutcome all count value percentage convert

    Bedfordshire_lastoutcome_percenatge = round((Bedfordshire_lastoutcome_count.counts /Bedfordshire_lastoutcome_count.counts.sum())*100, 2)
    Bedfordshire_lastoutcome_percenatge
    print('Bedfordshire_lastoutcome_percenatge', Bedfordshire_lastoutcome_percenatge)

    #essex lastcoucome null value handling
    df_E_lastcoucome = df_E[['Last_outcome_category']].fillna('No Outcome')
    df_E_lastcoucome

    #Essex last coutcome count
    Essex_lastoutcome_count = df_E_lastcoucome['Last_outcome_category'].value_counts(dropna=False).rename_axis('Last_outcome_category').reset_index(name='counts')
    # Sort_Essex_lastoutcome_count= Essex_lastoutcome_count.sort_values(by='Last_outcome_category', ascending=True)
    Essex_lastoutcome_count

    # essex all last outcome indivudial count
    Essex_lastoutcome_count.counts

    # essex all last outcome valuye sum
    Essex_lastoutcome_count.counts.sum()

    # #bedfordshire last coutcome all count value percentage convert

    Essex_lastoutcome_percenatge = round((Essex_lastoutcome_count.counts /Essex_lastoutcome_count.counts.sum())*100, 2)
    Essex_lastoutcome_percenatge
    print('Essex_lastoutcome_percenatge', Essex_lastoutcome_percenatge)

    # Group bar chart for last outcome catagory

    X = labels
    YBedfordshire = Bedfordshire_lastoutcome_percenatge
    ZEssex = Essex_lastoutcome_percenatge

    X_axis = np.arange(len(X))
    plt.subplots(figsize=(15, 7))
    plt.bar(X_axis - 0.2, YBedfordshire, 0.4, label = 'Bedfordshire')
    plt.bar(X_axis + 0.2, ZEssex, 0.4, label = 'Essex')

    plt.xticks(X_axis, X, rotation=60, fontsize=7)
    plt.xlabel("Crime types")
    plt.ylabel("Frequency")
    plt.title("Compare Bedfordshire & Essex Last coucome catagory and all year")

    plt.legend()

    for i, v in enumerate(YBedfordshire):
        plt.text(i - 0.3, v + 1, str(v) + '%', rotation=90)
    for i, v in enumerate(ZEssex):
        plt.text(i + 0.1, v + 1, str(v) + '%', rotation=90)
    plt.show()



################################################## bedfordshire Heap map  ########################################################
df_columnB = list(zip(df_B['Latitude'],df_B['Longitude']))
def Bedfordshire_generateHeatMap(default_location=[52.062475, -0.52502],default_zoom_start=8):
    base_map = folium.Map(location=default_location,control_scale=True,zoom_start=default_zoom_start )
    heatmap=plugins.HeatMap(df_columnB,radius=4,blur=3)
    base_map.add_child(heatmap)
    base_map.save("map.html")
    webbrowser.open("map.html")
    return base_map



#handle Longitude and Latitude null value
df_E.fillna({'Longitude':0, 'Latitude': 0}, inplace=True)
df_E

######################################################### Essex heat map ###########################################################
df_columnE = list(zip(df_E['Latitude'],df_E['Longitude']))
def Essex_generateHeatMap(default_location=[51.57207, 0.48171],default_zoom_start=8):
    base_map = folium.Map(location=default_location,control_scale=True,zoom_start=default_zoom_start )
    heatmap=plugins.HeatMap(df_columnE,radius=4,blur=3)
    base_map.add_child(heatmap)
    base_map.save("map2.html")
    webbrowser.open("map2.html")
    return base_map



#############################################correlation metrix bedfordshire and essex crime####################################
def Correlation_matrix():
    print('Heat map of the Bedfordshire')

        # count bedfordshire crime
    B_C_count=df_B['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='B_Count')
    # print(B_C_count)
    # Creating the first dataframe of corelation metrix
    df1 = pd.DataFrame(B_C_count.B_Count)

    # count essex crime
    E_C_count=df_E['Crime_type'].value_counts(dropna=False).rename_axis('Crime_type').reset_index(name='E_Count')
    # print(E_C_count)
    # Creating the second dataframe 
    df2 = pd.DataFrame(E_C_count.E_Count)


    # Print the first dataframe
    print(df1, "\n")
    
    # Print the second dataframe
    print(df2)

    # data set in one data frmae
    data = {'Bedfordshir': B_C_count.B_Count,
            'Essex': E_C_count.E_Count,
            }

    df3= pd.DataFrame(data)
    print(df3)

    Bedfordshire_essex_corr = df3.corr()
    print(Bedfordshire_essex_corr)

    
    # generate heatmap of correlation matrix 
    sns.heatmap(Bedfordshire_essex_corr, annot = True, fmt='.2g',cmap= 'coolwarm')
    plt.title("Heatmap")
    plt.show()

        # Create a new Toplevel window
    # new_window = Toplevel(root)
    # new_window.title("Heatmap Window")

    # Add the heatmap to the new Toplevel window
    # canvas = FigureCanvasTkAgg(plt.gcf(), master=new_window)
    # canvas.draw()
    # canvas.get_tk_widget().pack()


######################################### Function for closing window  #######################################################

def Close():
    root.destroy()


#heading
Label(text ="Bedfordshire & Essex Police Analysis", bg="#1c2541", fg="#5bc0be", font=("calibri", 33), width="300", height="2").pack()




####################################################1st Card view##############################################################


f= Frame(root, bg="#1c2541", highlightbackground="#1c2541", highlightthickness=1, width=300, height=370)
f.place(x=10,y=118)

Label(f,text="Crime Type",font=("Gabriola", 30,"bold"), fg="#5bc0be", bg="#1c2541").place(x=65,y=0)

Radiobutton(f, text="All Crime",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=1,command=lambda: print(R_button1.get())).place(x=10,y=70)
Radiobutton(f, text="Violence and sexual offences",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=2, command=lambda: print(R_button1.get())).place(x=10,y=100)
Radiobutton(f, text="Anti-social behaviour",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=3, command=lambda: print(R_button1.get())).place(x=10,y=130)
Radiobutton(f, text="Public order",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=4, command=lambda: print(R_button1.get())).place(x=10,y=160)
Radiobutton(f, text="Vehicle crime",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=5, command=lambda: print(R_button1.get())).place(x=10,y=190)
Radiobutton(f, text="Criminal damage and arson",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=6, command=lambda: print(R_button1.get())).place(x=10,y=220)
Radiobutton(f, text="Theft from the person",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=7, command=lambda: print(R_button1.get())).place(x=10,y=240)
Radiobutton(f, text="Possession of weapons",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=8, command=lambda: print(R_button1.get())).place(x=10,y=270)
Radiobutton(f, text="Shoplifting",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=9, command=lambda: print(R_button1.get())).place(x=195,y=70)
Radiobutton(f, text="Drugs",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=10, command=lambda: print(R_button1.get())).place(x=195,y=100)
Radiobutton(f, text="Other crime",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=11, command=lambda: print(R_button1.get())).place(x=195,y=130)
Radiobutton(f, text="Bicycle theft",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=12, command=lambda: print(R_button1.get())).place(x=195,y=160)
Radiobutton(f, text="Robbery",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=13, command=lambda: print(R_button1.get())).place(x=195,y=190)
Radiobutton(f, text="Other theft",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=14, command=lambda: print(R_button1.get())).place(x=195,y=210)
Radiobutton(f, text="Burglary",fg="#5bc0be",bg="#1c2541", variable=R_button1, value=15, command=lambda: print(R_button1.get())).place(x=195,y=240)



##################################################second card view#############################################################
f2= Frame(root, bg="#1c2541", highlightbackground="#1c2541", highlightthickness=1, width=300, height=370)
f2.place(x=350,y=118)

#Select year analysis
Label(f2,text="Select year",font=("Gabriola", 17,"bold"), fg="#5bc0be", bg="#1c2541").place(x=0,y=0)

Radiobutton(f2, text="All Year",fg="#5bc0be",bg="#1c2541",variable=R_button2, value=0, command=lambda: print(R_button2.get())).place(x=10,y=50)
Radiobutton(f2, text="2020",fg="#5bc0be",bg="#1c2541", variable=R_button2, value=2020, command=lambda: print(R_button2.get())).place(x=10,y=70)
Radiobutton(f2, text="2021",fg="#5bc0be",bg="#1c2541", variable=R_button2, value=2021, command=lambda: print(R_button2.get())).place(x=10,y=90)
Radiobutton(f2, text="2022",fg="#5bc0be",bg="#1c2541", variable=R_button2, value=2022, command=lambda: print(R_button2.get())).place(x=10,y=110)

#Bedfordshire & Bedfordshire police force analysis
Label(f2,text="Bedfordshire & Essex police",font=("Gabriola", 17,"bold"), fg="#5bc0be", bg="#1c2541").place(x=0,y=140)
Radiobutton(f2, text="Bedfordshire",fg="#5bc0be",bg="#1c2541", variable=R_button3, value=300, command=lambda: print(R_button3.get())).place(x=10,y=180)
Radiobutton(f2, text="Essex",fg="#5bc0be",bg="#1c2541", variable=R_button3, value=301, command=lambda: print(R_button3.get())).place(x=10,y=200)
Label(f2,text="Graphical Analysis",font=("Gabriola", 17,"bold"), fg="#5bc0be", bg="#1c2541").place(x=0,y=230)
Button(f2, text="Bar Chart", command=Bar_selection).place(x=10,y=290)

#################################################################third card view##################################################
f3= Frame(root, bg="#1c2541", highlightbackground="white", highlightthickness=1, width=300, height=370)
f3.place(x=690,y=118)

Label(f3,text="Compare both force all year & all crime",font=("Gabriola", 15,"bold"), fg="#5bc0be", bg="#1c2541").place(x=0,y=0)

Label(f3,text="Compare all crime",font=("Gabriola", 14, ), fg="#5bc0be", bg="#1c2541").place(x=0,y=35)
Button(f3, text="Bar Chart", command=Compare_Bedfordshire_essex).place(x=232,y=42)

Label(f3,text="Compare breakdown of crime ",font=("Gabriola", 14,), fg="#5bc0be", bg="#1c2541").place(x=0,y=70)
Button(f3, text="Line chart", command=Compare_breakdown_crime).place(x=232,y=80)

Label(f3,text="Compare during covid time crime ",font=("Gabriola", 14, ), fg="#5bc0be", bg="#1c2541").place(x=0,y=100)
Button(f3, text="Line chart", command=Compare_Covid_crime).place(x=232,y=110)

Label(f3,text=" Compare Summer and Winter crime",font=("Gabriola", 14, ), fg="#5bc0be", bg="#1c2541").place(x=0,y=130)
Button(f3, text="Pie chart", command=Compare_Summer_Winter_crime).place(x=232,y=140)


Label(f3,text="Compare Last outcome category",font=("Gabriola", 14,), fg="#5bc0be", bg="#1c2541").place(x=0,y=160)
Button(f3, text="Bar Chart", command=lastoutcome).place(x=232,y=170)

Label(f3,text="Heat Map",font=("Gabriola", 15,"bold"), fg="#5bc0be", bg="#1c2541").place(x=0,y=190)

Button(f3, text="Bedfordshire", command=Bedfordshire_generateHeatMap).place(x=5,y=230)
Button(f3, text="Essex", command=Essex_generateHeatMap).place(x=100,y=230)

Label(f3,text="Corrlation of Bedforshire & Essex",font=("Gabriola", 15,"bold"), fg="#5bc0be", bg="#1c2541").place(x=0,y=255)

Button(f3, text="Corrlation Matrix", command=Correlation_matrix).place(x=5,y=295)

Button(f3, text="Exit", command=Close, bg='red', fg="#5bc0be").place(x=250,y=325)


###############################footer##########################################

footer_label = Label(root, text="30069394@Copyright@2023", width="300")
footer_label.pack(side="bottom")

root.mainloop()


    