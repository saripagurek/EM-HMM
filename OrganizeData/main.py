import pandas as pd
import csv

rows=[["Item", "Scene Region", "AOI"]]


originalData = pd.read_csv('original_clean.csv', usecols=['ItemNum', 'Fix_X', 'Fix_Y', 'Scene_X1', 'Scene_Y1', 'Scene_X2', 'Scene_Y2'])
regionData = pd.read_csv('regions.csv', usecols=['Item', 'Y1', 'Y2'])

regionData.set_index("Item", inplace=True)
regionData = regionData.sort_index()

targetData = pd.read_csv('targets.csv', usecols=['Item', 'Con_Y1','Con_Y2','Con_X1','Con_X2','Incon_Y1','Incon_Y2', 'Incon_X1','Incon_X2'])

targetData.set_index("Item", inplace=True)
targetData = targetData.sort_index()


def bin(bound_y1, bound_y2, test):
    if test <= bound_y1:
        return "Upper"
    elif test <= bound_y2:
        return "Middle"
    else:
        return "Lower"


def isRegion(x1, y1, x2, y2, testx, testy):
    if (testx >= x1) and (testx <= x2):
        if (testy >= y1) and (testy <= y2):
            return True
    return False


for index, row in originalData.iterrows():
    #if index < 10:
    item = int(row["ItemNum"])

    fixy = row["Fix_Y"]
    fixx = row["Fix_X"]
    #fix = originalData.at[index, "Fix_Y"]
    bound_y1 = regionData.at[item, "Y1"]
    bound_y2 = regionData.at[item, "Y2"]

    targRegX1 = targetData.at[item, "Con_X1"]
    targRegX2 = targetData.at[item, "Con_X2"]
    targRegY1 = targetData.at[item, "Con_Y1"]
    targRegY2 = targetData.at[item, "Con_Y2"]

    sceneReg = bin(bound_y1, bound_y2, fixy)
    expectedReg = isRegion(row["Scene_X1"], row["Scene_Y1"], row["Scene_X2"], row["Scene_Y2"], fixx, fixy)
    targetReg = isRegion(targRegX1, targRegY1, targRegX2, targRegY2, fixx, fixy)

    s = ""
    if expectedReg:
        s = s + "Expected"
    else:
        s = s + "Irrelevant"

    if targetReg:
        s = s + ", Target"

    tempRow = [item, sceneReg, s]
    rows.append(tempRow)


    '''
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
    '''
    #rows.append(tempRow)


with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)


calcData = pd.read_csv('output.csv', usecols=["Scene Region", "AOI"])
fullData = pd.read_csv('original_clean.csv')

result =fullData.join(calcData, lsuffix="_left", rsuffix="_right")
result.to_csv('final.csv', index=False)

