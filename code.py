import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import random as rr
from sklearn import svm

df = pd.read_csv('train.data')
df1 = df.T.values.tolist()
feature_2=[]
train_seq=df1[1]

single=""
def mass_aa(s):
    mass = {
    'A':71.08, 'R':156.2,'N': 114.1, 'D': 115.1 , 'C' :103.1, 'E': 129.1, 'Q':128.1 ,'G':57.05,'H':137.1,'I':113.2,'L':113.2,'K':128.09,'M':131.04,'F':147.06,'P':97.12,'S':87.08,'T':101.1,'W':186.2,'Y':163.2,'V':99.13,
    'a':71.08, 'r':156.2,'n': 114.1, 'd': 115.1 , 'c' :103.1, 'e': 129.1, 'q':128.1 ,'g':57.05,'h':137.1,'i':113.2,'l':113.2,'k':128.09,'m':131.04,'f':147.06,'p':97.12,'s':87.08,'t':101.1,'w':186.2,'y':163.2,'v':99.13,'X':0
    }
    m=0
    m_list = []
    for i in s:
        if(i!="X"):
            m+=mass[i]
    
        
    return m
def iso(s):
    isoelectric = {
    'G':5.97,'A':6.00,'S':5.68,'P':6.30,'V':5.96,'T':6.16,'C':5.07,'I':6.02,'L':5.98,'N':5.41,'D':2.77,'Q':5.66,'K':9.74,'E':3.22,'M':5.74,'H':7.59,'F':5.48,'R':10.76,'Y':5.66,'W':5.89,
    'g':5.97,'a':6.00,'s':5.68,'p':6.30,'v':5.96,'t':6.16,'c':5.07,'i':6.02,'l':5.98,'n':5.41,'d':2.77,'q':5.66,'k':9.74,'e':3.22,'m':5.74,'h':7.59,'f':5.48,'r':10.76,'y':5.66,'w':5.89
    }   
    is_=0
    for i in s:
        if(i!="X"):
            is_+=isoelectric[i]
    
    return is_

def polarity(s):
    isoelectric = {
    'G':0.66,'A':0.75,'S':0.76,'P':0.67,'V':0.86,'T':0.63,'C':0.31,'I':0.89,'L':0.92,'N':0.87,'D':0.93,'Q':0.79,'K':0.76,'E':0.82,'M':0.58,'H':0.53,'F':0.83,'R':0.68,'Y':0.64,'W':0.58,
    'g':0.66,'a':0.75,'s':0.76,'p':0.67,'v':0.86,'t':0.63,'c':0.31,'i':0.89,'l':0.92,'n':0.87,'d':0.93,'q':0.79,'k':0.76,'e':0.82,'m':0.58,'h':0.53,'f':0.83,'r':0.68,'y':0.64,'w':0.58,"X":0
    }   
    is_=0
    for i in s:
        is_+=isoelectric[i]
    is_list =[]
    is_list.append(is_) 
    return is_


def charge(s):

    charge = {
    'A':0,'V':0,'Y':0, 'R':1,'H':0.5,'I':0,'L':0,'S':0,'T':0,'W':0,'K':1,'N':0,'D':-1,'C':0,'Q':0,'E':-1,'G':0,'M':0,'F':0,'P':0
    }    
    c=0

    for i in s:
        if(i!="X"):
            c+=charge[i]
    c_list =[]
    c_list.append(c)
    return c 
def hydro_aa(ss):
    hydro = {
    'A':0.74,'C':0.91,'D':0.62,'E':0.62,'F':0.88,'G':0.72,'H':0.78,'I':0.88,'K':0.52,'L':0.85,'M':0.85,'N':0.63,'P':0.64,'Q':0.62,'R':0.64,'S':0.66,'T':0.70,'V':0.86,'W':0.85,'Y':0.76,
    'a':0.74,'c':0.91,'d':0.62,'e':0.62,'f':0.88,'g':0.72,'h':0.78,'i':0.88,'k':0.52,'l':0.85,'m':0.85,'n':0.63,'p':0.64,'q':0.62,'r':0.64,'s':0.66,'t':0.70,'v':0.86,'w':0.85,'y':0.76
    }
    h=0
    for i in ss:
        if(i!="X"):
            h+=hydro[i]
    h_list=[]
    h_list.append(h)    
    return h 


for i in train_seq:
    single+=i
single="XXXXXX"+single+"XXXXXX"
AA_ = "ARNDCEQGHILKMFPSTWYVX"

feature1=[]
feature=[]

for i in range(0,len(single)-12):
    t=single[i:i+13]
    if(t[6].isupper()==True):
        feature.append(-1)
    elif(t[6].islower()==True):
        feature.append(1)

    
    d=[]
    
    t=t.upper()

    for k in range(len(t)):
        for j in range(len(AA_)):
            if AA_[j] == t[k]:
                d.append(1)
            else:
                d.append(0)
    #d.append(mass_aa(t))
    d.append(hydro_aa(t))
    d.append(iso(t))
    d.append(charge(t))
    d.append(polarity(t))
    feature1.append(d)
    #for j in ma:
        #d.append(j)
    
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(feature1,feature)
print("////////////////////////////////")
#s = svm.SVC()
#s.fit(feature1, feature)


df = pd.read_csv('test.txt')
df1 = df.T.values.tolist()

df2 = pd.read_csv('test1.txt')
data_list = df2.T.values.tolist()
residue=data_list[1]



protein =""
for i in residue:
    protein+=i
#print(protein)
protein="XXXXXX"+protein+"XXXXXX"

feature1=[]
for i in range(0,len(protein)-12):
    t=protein[i:i+13]
        
    d=[]
    
    t=t.upper()

    for k in range(len(t)):
        for j in range(len(AA_)):
            if AA_[j] == t[k]:
                d.append(1)
            else:
                d.append(0)
    #d.append(mass_aa(t))
    d.append(hydro_aa(t))
    d.append(iso(t))
    d.append(charge(t)) 
    d.append(polarity(t))
    feature1.append(d)
vector = regressor.predict(feature1)
for i in range(0,len(vector)):
    if(vector[i]>0):
        vector[i]=1

#vector = s.predict(feature1)
arr=[]
aaaa=4



list1=data_list[0]
list2=vector
for i in range(0,len(list2)):
    if(list2[i]==1):
        print("????")


dict = {'ID': list1, 'Lable': list2}
print(len(list1))
print(len(list2))
df = pd.DataFrame(dict)
df.to_csv('sample.txt', index=False)















