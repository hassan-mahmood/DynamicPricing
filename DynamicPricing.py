
# coding: utf-8

# In[31]:


import numpy as np
import matplotlib.pyplot as plt
import random



# In[32]:


def drawplot(A,B,xmin,xmax,ymin,ymax,Alabel,Blabel,xlab,ylab,titleval):
    plt.figure()
    index = np.array(range(xmin+1,xmax))
    bar_width = 0.4
    opacity = 0.8

    rects1 = plt.bar(index, A, bar_width,
                     alpha=opacity,
                     color='black',
                     label=Alabel)

    rects2 = plt.bar(index + bar_width, B, bar_width,
                     alpha=opacity,
                     color='w',edgecolor='black',
                     label=Blabel)

    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(titleval)
    #plt.xticks(index + bar_width, (np.array(range(1,hours+1))))
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)
    plt.legend()



    #plt.tight_layout()
    plt.show()


# In[33]:


def estimatesimpleprice(allotedval,usageval):
    c1h=10
    c2h=18
    #allotedval=allotedval/maxlevel
    #usageval=usageval/maxlevel
    
    if(usageval<=allotedval):
        cost=c1h*usageval
    else:
        cost=allotedval*c1h+c2h*(usageval-allotedval)**2
    return cost
        
    


# In[34]:


def estimatemyprice(allotedval,usageval):
    c1h=10
    c2h=18
    global bi
    k=int((usageval-1)/allotedval)
    
    
    if(usageval<=allotedval):
        cost=c1h*usageval*(1+bi)
        
    else:
        cost=allotedval*c1h+c2h*(1+bi)*(usageval-allotedval)**2
        
    bi=0.8*bi+0.2*k
    return cost


# In[37]:


bi=0
hours=24
alloted=np.array(random.sample(range(50, 100), hours))
usage=np.array(random.sample(range(50, 100), hours))
alloted=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
usage=[12,12,12,12,12,12,10,10,10,10,10,12,12,12,12,12,12,12,12,12,12,12,12,12]
cost=[]
cost2=[]



for i in range(0,hours):
    costval=estimatesimpleprice(alloted[i],usage[i])
    cost+=([costval])
    costval2=estimatemyprice(alloted[i],usage[i])
    cost2+=([costval2])




Alabel='Electricity Alloted'
Blabel='Electricity Consumed'
xlab='Time of day (Hour)'
ylab='Power Consumption (KW)'
titleval='Electricity Consumed and Allocated to Customer Hourly in a Day'

drawplot(alloted,usage,0,25,0,20,Alabel,Blabel,xlab,ylab,titleval)

Alabel='Old dP Method'
Blabel='Proposed dP Method'
xlab='Time of day (Hour)'
ylab='Cost of Electricity($)'
titleval='Electricity Cost for Customer Hourly in a Day'

maxval=1.3*max(max(cost),max(cost2))

cost=[x / maxval for x in cost]
cost2=[x / maxval for x in cost2]

print(cost)

drawplot(cost,cost2,0,25,0,1,Alabel,Blabel,xlab,ylab,titleval)
#drawplot(alloted,usage,0,25,0,120,Alabel,Blabel,xlab,ylab,titleval)


    

