class Solution():

    def topKFrequent(self, words, k):

        wordsCounter = {}

        for word in words:
            counterRecord = wordsCounter.get(word)
            if not counterRecord:
                counterRecord = [0, word]
                wordsCounter[word] = counterRecord
            counterRecord[0] += 1

        recordsList = list(wordsCounter.values())
        sortedCounterRecords = self.quickSort(recordsList, 0, len(recordsList) - 1)

        result = []

        for i in range(k):
            result.append(sortedCounterRecords[i][1])

        return result

    def quickSort(self, counterRecordList, minIndex, maxIndex):
        pivot = self.partition(counterRecordList, minIndex, maxIndex)
        if pivot-1 > minIndex:
            self.quickSort(counterRecordList, minIndex, pivot-1)
        if pivot+1 < maxIndex:
            self.quickSort(counterRecordList, pivot+1, maxIndex)

        return counterRecordList

    def partition(self, counterRecordList, minIndex, maxIndex):
        pivotRecord = counterRecordList[maxIndex]
        biggerElementIndex = -1

        for i in range(minIndex, maxIndex):
            record = counterRecordList[i]
            if self.isHigher(record, pivotRecord):
                biggerElementIndex += 1
                counterRecordList[biggerElementIndex], counterRecordList[i] = \
                    counterRecordList[i], counterRecordList[biggerElementIndex]

        counterRecordList[biggerElementIndex+1], counterRecordList[maxIndex] = \
            counterRecordList[maxIndex], counterRecordList[biggerElementIndex+1]

        return biggerElementIndex + 1

    def isHigher(self, aCounterRecord, otherCounterRecord):
        return aCounterRecord[0] > otherCounterRecord[0] or \
               (aCounterRecord[0] == otherCounterRecord[0] and aCounterRecord[1] < otherCounterRecord[1])