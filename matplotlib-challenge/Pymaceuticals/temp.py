# Dependencies and Setup
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

#-----

# File to Load (Remember to Change These)
mouse_drug_data = "data/mouse_drug_data.csv"
clinical_trial_data = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_org = pd.read_csv(mouse_drug_data)
clinical_org = pd.read_csv(clinical_trial_data)

#-----

#print(mouse_org.head(10))
print('\n---------------------\n')
#print(clinical_org.head(10))
print('\n---------------------\n')

#-----

# Combine the data into a single dataset
mouse = mouse_org.copy()
clinical = clinical_org.copy()

data = pd.merge(clinical, mouse, on='Mouse ID', how='inner')

print(data.head(10))
print('\n---------------------\n')

#-----

# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint
mean_tumor_resp = data[['Drug', 'Timepoint', 'Tumor Volume (mm3)']].groupby(['Drug', 'Timepoint']).mean().reset_index()

#print(mean_tumor_resp.head(15))
#print('\n---------------------\n')

#-----

# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
sem_tumor_resp = data[['Drug', 'Timepoint', 'Tumor Volume (mm3)']].groupby(['Drug', 'Timepoint']).sem().reset_index()

#print(std_tumor_resp.head(15))
print('\n---------------------\n')

#-----

# Minor Data Munging to Re-Format the Data Frames
mean_tumor_resp2 = mean_tumor_resp.pivot(index='Timepoint', columns='Drug', values='Tumor Volume (mm3)')

print(mean_tumor_resp2.head())
print('\n---------------------\n')
sem_tumor_resp2 = sem_tumor_resp.pivot(index='Timepoint', columns='Drug', values='Tumor Volume (mm3)')
#print(sem_tumor_resp2.head())
print('\n---------------------\n')

#-----

# Generate the Plot (with Error Bars)
mean_tumor_resp2.plot(marker='^', yerr=sem_tumor_resp2)
# see if you can customize markers
plt.title('Tumor Response to Treatment')
plt.xlabel('Time (Days)')
plt.ylabel('Tumor Volume (mm3)')
plt.legend(loc='best', fontsize='x-small')
plt.grid(axis='y')
# save to file
#plt.show()

# Try scatterplot
#plt.plot(kind='scatter')




#-----

# Store the Mean Met. Site Data Grouped by Drug and Timepoint
mean_met_site = data[['Drug', 'Timepoint', 'Metastatic Sites']].groupby(['Drug', 'Timepoint']).mean()
#print(mean_met_site.head(15))
print('\n---------------------\n')

# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint
sem_met_site = data[['Drug', 'Timepoint', 'Metastatic Sites']].groupby(['Drug', 'Timepoint']).sem()
#print(sem_met_site.head(15))
print('\n---------------------\n')

#-----

# Minor Data Munging to Re-Format the Data Frames
mean_met_site2 = mean_met_site.reset_index().pivot(index='Timepoint', columns='Drug', values='Metastatic Sites')
#print(mean_met_site2.head())
print('\n---------------------\n')
sem_met_site2 = sem_met_site.reset_index().pivot(index='Timepoint', columns='Drug', values='Metastatic Sites')
#print(sem_met_site2.head())
print('\n---------------------\n')

#-----

# Generate the Plot (with Error Bars)
mean_met_site2.plot(marker='^', yerr=sem_met_site2) # markers blocking error bars
# see if you can customize markers
plt.title('Metastatic Spread During Treatment')
plt.xlabel('Time (Days)')
plt.ylabel('Met. Sites')
plt.legend(loc='best', fontsize='x-small')
plt.grid(axis='y')
# save to file
#plt.show()

#-----

# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
survival = data[['Drug', 'Timepoint', 'Mouse ID']].groupby(['Drug', 'Timepoint']).count().reset_index().rename(columns={'Mouse ID':'Mouse Count'})
#print(survival.head())
print('\n---------------------\n')

#-----

# Minor Data Munging to Re-Format the Data Frames
survival2 = survival.pivot(index='Timepoint', columns='Drug', values='Mouse Count')
#print(survival2.head())
print('\n---------------------\n')
#-----

# Generate the Plot (Accounting for percentages)
(survival2 / survival2.iloc[0] * 100).plot(marker='^')
# see if you can customize markers
plt.title('Survival During Treatment')
plt.xlabel('Time (Days)')
plt.ylabel('Survival Rate (%)')
plt.legend(loc='best', fontsize='x-small')
plt.grid(axis='y')
# save to file
#plt.show()
plt.clf()
#-----

# Calculate the percent changes for each drug
change = (mean_tumor_resp2.loc[45] - mean_tumor_resp2.loc[0])/mean_tumor_resp2.loc[0] * 100

font = {'family': 'serif', 'weight': 'normal', 'size': 25, 'color':'white'}
#print(change)

col = ['red' if x >= 0 else 'green' for x in change]

plt.bar(mean_tumor_resp2.columns, change, color=col, label=mean_tumor_resp2.columns)
plt.title('Tumor Change Over 45 Day Treatment')
plt.xlabel('Drug')
plt.ylabel('% Tumor Volume Change')
plt.grid(axis='y')
plt.xticks(list(range(10)), labels=mean_tumor_resp2.columns)

for i in range(0, 10, 1):
    plt.text(x=i-0.32, y=change[i]/2, s='%'+str(round(change[i], 2)), fontdict=font) # set numerical graph width and then chop it up; use a for loop to put text in
# try to get labels on bars

plt.show()



# alternate to last part using tuples
# list(zip(change.index, change))


# a chart is a list where the first and only element is a 2D Line object
