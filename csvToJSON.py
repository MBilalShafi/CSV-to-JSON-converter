import json
import sys

def startCaseAndUnderscore(str):
  return str.lower().replace(' ', '_')

if len(sys.argv) < 2:
  print("Usage: python", sys.argv[0], "nameOfCsvFile.csv outFileName.json (outFileName is optional)")
  exit()

fname = sys.argv[1]

if len(sys.argv) == 3:
  outFileName = sys.argv[2]
  skippedRows = 5
elif len(sys.argv) == 4:
  outFileName = sys.argv[2]
  skippedRows = int(sys.argv[3])
else:
  outFileName = "output.json"
  skippedRows = 5

f = open(fname,'r')
csvData = f.readlines()[skippedRows:]
f.close()

headerRow = [x.strip() for x in csvData[0].split(',')]
headerRowWithNoEmptyValues = list(filter(None, headerRow))

rowsAsLists = []

for row in csvData[1:]:
  processedRow = [x.strip() for x in row.split(',')]
  rowsAsLists.append(list(filter(None, processedRow)))

listOfFields = [{'name': name,'canonicalName': startCaseAndUnderscore(name)} for name in headerRowWithNoEmptyValues]

metaData = { 'fields': listOfFields }

canonical = list(map(startCaseAndUnderscore, headerRowWithNoEmptyValues))

listOfRows = []

for i in range(len(rowsAsLists)):
  tempDict = {}
  for index, value in enumerate(canonical):
    tempDict[value] = rowsAsLists[i][index].replace('"', '')
  listOfRows.append(tempDict)


finalObj = {
  'metaData': metaData,
  'data': listOfRows
}

print ("Generated JSON Format Successfully")
print ("Outputting to:", outFileName, "...")

with open(outFileName, 'w') as outfile:
  json.dump(finalObj, outfile, indent=2)

print ("Success!")