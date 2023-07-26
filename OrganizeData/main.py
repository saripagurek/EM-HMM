import pandas
import csv

rows=["Item", "Fixation", "Con Target Region", "Incon Target Region"]
#with open('output.csv', 'w', newline='') as file:
    #writer = csv.writer(file)
    #writer.writerows(rows)

originalData = pd.read_csv('original.csv', usecols=['ItemNum', 'Fix_X', 'Fix_Y'])
targetData = pd.read_csv('targets.csv', usecols=['Item', 'Y1', 'Y2'])
regionData = pd.read_csv('regions.csv', usecols=['Item', 'Con_Y1','Con_Y2','Incon_Y1','InconY2'])

