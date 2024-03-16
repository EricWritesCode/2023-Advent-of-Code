import re

def main():
    with open("Day1-Data.txt", "r") as file:
        data = file.read()
        finalData = data.split("\n")
    
    finalTotal: int = 0
    lineCount: int = 0
    validNumbers = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    i = 1
    while i < 10:
        validNumbers.append(str(i))
        i += 1
    conversionList = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for item in finalData:
        lineCount += 1
        lineSet = set()
        finalValues = []
        
        for num in validNumbers:
            # Check line for number
            index = item.find(num)
            if index != -1:
                lineSet.add(f"{index}|{num}")
            # Check in reverse
            rindex = item.rfind(num)
            if rindex != -1:
                lineSet.add(f"{rindex}|{num}")

        # Break up the set and convert word numbers to ints
        for entry in lineSet:
            indexValuePair = str(entry).split("|")
            if indexValuePair[1] in conversionList:
                indexValuePair[1] = conversionList.get(indexValuePair[1])
            indexValuePair[0] = int(indexValuePair[0])
            finalValues.append(indexValuePair)

        # Sort final values by index
        finalValues = sorted(finalValues)

        first = finalValues[0][1]
        last = finalValues[len(finalValues)-1][1]

        rowValue = str(first) + str(last)
        finalTotal += int(rowValue)

        print(f"[{lineCount}] {item}: {lineSet} ({finalValues}) Row: {rowValue}")
        print(f"New total: {finalTotal}")

    print(f"Final total: {finalTotal}")

main()
