import time
import math


def writeOutputFile(inputFilename, contents):
    outputFile = open(inputFilename + "_out.txt", 'w')  # Irasomas tekstas i faila
    outputFile.write(contents)


def readInputFile(inputFilename):
    inputFile = open(inputFilename + ".txt", 'r')  # Atidaromas failas skaitymo rezimu
    inputFileContents = inputFile.read()
    if len(inputFileContents) == 0:  # Jei ivesties failas tuscias, programa - stabdoma
        writeOutputFile(inputFilename, "Ivesties failas yra tuscias")
        exit(1)

    haystack = [int(n) for n in inputFileContents.split(',')]  # Nuskaitomi duomenys ir sukuriamas skaiciu masyvas
    return haystack


# Dvejetainis paieskos metodas (ivestis surusiuota didejimo tvarka ir elementai unikalus)
def binarySearch(where, what, _offsetCounter=0):
    centerIdx = int(math.floor(len(where) / 2.))
    centerElement = where[centerIdx]
    if centerElement == what:
        return centerIdx + _offsetCounter
    elif len(where) == 1:
        return None
    elif what < centerElement:
        return binarySearch(where=where[:centerIdx], what=what, _offsetCounter=_offsetCounter)
    return binarySearch(where=where[centerIdx + 1:], what=what, _offsetCounter=_offsetCounter + centerIdx + 1)


if __name__ == "__main__":
    # INPUT
    inputFilename = "ivestis_1000"
    haystack = readInputFile(inputFilename)  # Skaitomas failas
    needle = int(input("Kokio skaiciaus ieskote? "))  # Dialogo pagalba suzinoma, kokio skaiciaus ieskoma

    # CALCULATION
    startTime_s = time.clock()  # Matuojamas vykdymo laikas
    foundIdx = binarySearch(where=haystack, what=needle)
    duration_us = (time.clock() - startTime_s) * 1e6

    # OUTPUT
    if foundIdx is None:
        outputContents = "Skaicius nerastas per {} ms".format(duration_us)
    else:
        outputContentsTemplate = "Skaicius rastas (indeksuojamoje nuo 0) pozicijoje {} per {} us (=1e-6 s)"
        outputContents = outputContentsTemplate.format(foundIdx, duration_us)
    print(outputContents)
    writeOutputFile(inputFilename, outputContents)  # Isvedami rezultatai i faila
