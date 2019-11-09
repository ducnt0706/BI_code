import numpy as np
import csv
import statistics
# 0.get data
# TODO: reaturn header
def getdheader():
    f=open("Melbourne_housing_FULL.csv","r")
    dataname=[]
    for row in csv.reader(f,delimiter=','): 
        dataname.append(row)
    return dataname[:1]
# TODO:return data with header
def getdata_full():
    f=open("Melbourne_housing_FULL.csv","r")
    dataname=[]
    for row in csv.reader(f,delimiter=','): 
        dataname.append(row)
    return dataname

# TODO:return data without header
def getdata():
    f=open("Melbourne_housing_FULL.csv","r")
    dataname=[]
    for row in csv.reader(f,delimiter=','): 
        dataname.append(row)
    dataname=dataname[1:]
    return dataname

# TODO: beautiful print data
def niceprint(datatest):    
    for mylist in datatest:
        print(mylist,"\n")

# 1.Remove column
def deletecolumn(dataname,index):
    for mylist in dataname:
        mylist.remove(mylist[index])

# 2.Remove rows has empty fields ?
def deleterow_empty(dataname):
    empty_row=lambda row: False if row[4] == '' or row[10] == '' or row[11] == '' or row[12] == '' or row[13] == '' or row[14] == '' or row[15] == '' or row[18] == '' else True
    result_data=list(filter(empty_row,dataname))
    return result_data
      
# 3.Collect values (boundary,mean,median,..)
# TODO: return mean of cloumn
def find_mean(dataname,index):
    mylist=[]
    for sublist in dataname:
        mylist.append(sublist[index])
    myarr=np.asarray(mylist,dtype=int)
    mylist=myarr.tolist()
    return statistics.mean(mylist)
# TODO: return max of cloumn
def find_max(dataname,index):
    mylist=[]
    for sublist in dataname:
        mylist.append(sublist[index])
    myarr=np.asarray(mylist,dtype=int)
    mylist=myarr.tolist()
    return max(mylist)
       
# 4.Covert Upercase <-> Lowercase
# TODO:Upercase by upper()
def upper_column(dataname,index):
    for row in dataname:
        try:
            row[index]=row[index].upper()
        except:
            print('Check your type of value')

# TODO:Replace abbreviation to normal
def change_assigntotext_row3(dataname):
    for row in dataname:
        if row[3]=='h':
            row[3]='house'
        if row[3]=='u':
            row[3]='duplex'
        if row[3]=='t':
            row[3]='townhouse'

# 5.Cut long texts
def cutlong_text_row16(dataname):
    for row in dataname:
        catgories=row[16].split(' ')                          #covert to list
        council_data=lambda x: False if x=='Council'else True # find data='Council'
        catgories=list(filter(council_data,catgories))        #filter data
        row[16]=' '.join(catgories)                           #covert to string
                               
# Submit. Save file in csv
def save_cleandata(newdataname):
    # I.getdata
    olddataname=getdata()
    # II.clean file
    #1. delete empty rows
    resultdata=deleterow_empty(olddataname)
    #2. Truncate long texts
    cutlong_text_row16(resultdata)
    #3. Upercase column
    upper_column(resultdata,6)
    #4. Change symboys to text
    change_assigntotext_row3(resultdata)
    # III.save file
    csv_file=open(newdataname,mode='w')
    writer=csv.writer(csv_file)
    header=['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date', 'Distance', 'Postcode', 'Bedroom', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount']
    writer.writerow(header)
    for row in resultdata:
        writer.writerow(row)
    csv_file.close()


# ------------------------------------------------DONE---------------------------------------
# The one thing, u must do, is  run this file ok!
save_cleandata('housingdata_clean.csv') # Create file csv that be cleaned


    




