import pandas
from nameToBin import nameToBinaryNodes

location = ("/Users/jakobfaarbaekgregersen/Documents/GitHub/MachineLearning/JakobGregersen_NamePrediction/Maries_navne.xlsx")
pandaDataframe = pandas.read_excel(location, sheet_name="Ark1")


def createHeaders():
    nameList = list()
    for i in range(290):
        nameList.append("Name1")
        
    for i in range(290):
        nameList.append("Name2")
        
    for j in range(len(nameList)):
        nameList[j] += "Letter" + str(j%10+1)
        
    for k in range(len(nameList)):
        nameList[k] += "Node" + str(k%29+1)
        
    return nameList
# print(createHeaders())


Names1 = pandaDataframe['Navn1']
Names2 = pandaDataframe['Navn2']
scores = pandaDataframe['Point']
nodeHeaders = createHeaders()
Headers = ["Score"] + nodeHeaders
listOfBinNodes = list()

for i in range(len(Names1)):
    score = [scores[i]]
    binName1 = nameToBinaryNodes(Names1[i])
    binName2 = nameToBinaryNodes(Names2[i])
    binRow = score + binName1 + binName2
    listOfBinNodes.append(binRow)
    
df = pandas.DataFrame(listOfBinNodes, columns=Headers)

sheetAsCSV = df.to_csv(index=False)

print("START: Extract data...")
myfile = open("./data.csv", "w")
n = myfile.write(sheetAsCSV)
myfile.close()
print("END:  Extract data.")