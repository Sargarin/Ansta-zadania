"""
ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
"""


def generator(str1, str2):
    genList = []
    str1 = str1.split("-")
    str2 = str2.split("-")
    firstDig = str1[0]
    secondDig = str1[1]
    while (int(firstDig) < int(str2[0]) and int(secondDig) <= 999) or (
            int(firstDig) == int(str2[0]) and int(secondDig) <= int(str2[1])):
        codeStr = str(firstDig) + "-" + str(secondDig)
        genList.append(codeStr)
        secondDig = int(secondDig) + 1
        if int(secondDig) > 999:
            secondDig = 0
            firstDig = str2[0]
    return genList


"""
ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]
"""


def function(listOfNumbers, size):
    missing = []
    for i in range(1, size + 1):
        missingNum = True
        for e in listOfNumbers:
            if i == e:
                missingNum = False
                break
        if missingNum == True:
            missing.append(i)
    return missing


"""
ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
"""
import decimal


def genList():
    listOfNumbers = []
    start = 2
    end = 5.5
    step = 0.5
    while start <= end:
        listOfNumbers.append(decimal.Decimal(start))
        start = start + step
    return listOfNumbers


if __name__ == "__main__":

    # Zad 1
    codes = generator("79-900", "80-155")
    for e in codes:
        print(e)

    # Zad 2
    missing = function([2, 3, 7, 4, 9], 10)
    print(missing)

    # Zad 3
    decList = genList()
    print(decList)
