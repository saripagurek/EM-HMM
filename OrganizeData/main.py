import pandas as pd
import csv

rows=[["Item", "Fixation", "Con Target Region", "Incon Target Region"]]


originalData = pd.read_csv('original.csv', usecols=['ItemNum', 'Fix_X', 'Fix_Y'])
regionData = pd.read_csv('regions.csv', usecols=['Item', 'Y1', 'Y2'])

regionData.set_index("Item", inplace=True)
regionData = regionData.sort_index()

targetData = pd.read_csv('targets.csv', usecols=['Item', 'Con_Y1','Con_Y2','Incon_Y1','Incon_Y2'])

targetData.set_index("Item", inplace=True)
targetData = targetData.sort_index()


def bin(bound_y1, bound_y2, test):
    if test <= bound_y1:
        return "Upper"
    elif test <= bound_y2:
        return "Middle"
    else:
        return "Lower"


for index, row in originalData.iterrows():
    #if index < 10:
    item = int(row["ItemNum"])

    #fix = row["Fix_Y"]
    fix = originalData.at[index, "Fix_Y"]
    bound_y1 = regionData.at[item, "Y1"]
    bound_y2 = regionData.at[item, "Y2"]

    con1 = targetData.at[item, "Con_Y1"]
    con2 = targetData.at[item, "Con_Y2"]
    avgCon = (con1 + con2) / 2

    incon1 = targetData.at[item, "Incon_Y1"]
    incon2 = targetData.at[item, "Incon_Y2"]
    avgIncon = (incon1 + incon2) / 2

    binFix = bin(bound_y1, bound_y2, fix)
    binCon = bin(bound_y1, bound_y2, avgCon)
    binIncon = bin(bound_y1, bound_y2, avgIncon)
    tempRow = [item, binFix, binCon, binIncon]
    rows.append(tempRow)


with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)



