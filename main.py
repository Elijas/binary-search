import time


def writeOutputFile(inputFilename, contents):
    outputFile = open(inputFilename + "_out.txt", 'w')
    outputFile.write(contents)


def readInputFile(inputFilename):
    inputFile = open(inputFilename + ".txt", 'r')  # Atidaromas failas skaitymo rezimu
    inputFileContents = inputFile.read()
    if len(inputFileContents) == 0:
        writeOutputFile(inputFilename, "Ivesties failas yra tuscias")
        exit(1)

    haystack = [int(n) for n in inputFileContents.split(',')]  # Nuskaitomi duomenys ir sukuriamas skaiciu masyvas
    return haystack


# Dvejetainis paieskos metodas (ivestis surusiuota didejimo tvarka ir elementai unikalus)
def binarySearch(where, what):
    return where.index(what)  # stub


if __name__ == "__main__":
    # INPUT
    inputFilename = "ivestis_10000"
    haystack = readInputFile(inputFilename)
    needle = int(input("Kokio skaiciaus ieskote? "))  # Dialogo pagalba suzinoma, kokio skaiciaus ieskoma

    # CALCULATION
    startTime_s = time.clock()
    foundIdx = binarySearch(where=haystack, what=needle)
    duration_us = (time.clock() - startTime_s) * 1e6

    # OUTPUT
    if foundIdx is None:
        outputContents = "Skaicius nerastas per {} ms".format(duration_us)
    else:
        outputContents = "Skaicius rastas (indeksuojamoje nuo 0) pozicijoje {} per {} us (=1e-6 s)".format(foundIdx,
                                                                                                           duration_us)
    print(outputContents)
    writeOutputFile(inputFilename, outputContents)
