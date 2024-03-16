import re

def main():
    with open("Day1-Data.txt", "r") as file:
        data = file.read()
        finalData = data.split("\n")
    
    finalTotal: int = 0
    lineCount: int = 0

    for item in finalData:
        lineCount += 1
        lineNumbers = re.findall(r'\d', item)
        lineTotal: int = int(lineNumbers[0] + lineNumbers[len(lineNumbers)-1])

        print(f"[{lineCount}] {item}: {lineNumbers} Total: {lineTotal}")
        
        finalTotal += lineTotal
        
        print(f"New total: {finalTotal}")

    print(f"Final total: {finalTotal}")

main()
