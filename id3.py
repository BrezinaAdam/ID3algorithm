from math import log
import sys

class Node:
    def __init__(self, name = "", x = 0, y = 0):
        self.name = name
        self.nextNodes = []
        self.x = x
        self.y = y

class Id3:
    def __init__(self, attributes, classes, names):
        self.A = attributes
        self.CL = classes
        self.NM = names
        self.it = 1

    def getNodes(self):
        while len(self.CL) > 1 and self.it < 10:
            out = []

            for i in range(0, len(self.A)):  # count infoGain for each Atribute
                out.append(self.infoGain(self.CL, self.A[i]))

            i_max = self.getBestAttr(out)

            '''po tade funguje dobre'''

            toPop = []
            uniqueAttr = self.A[i_max]
            #print uniqueAttr
            #print out
            for i in range(0, len(uniqueAttr)):  # pop out lines where the infogain is zero
                if out[i_max][1][uniqueAttr[i]] == 0.0:
                    toPop.append(i)

            toPop.reverse()                      # pop out lines from the end

            #print self.A
            self.printInTable()

            for i in range(0, len(toPop)):
                self.CL.pop(toPop[i])
                for a in self.A:
                    a.pop(toPop[i])
            self.it = self.it + 1

        print "tree generated"

    def getBestAttr(self, input):
        index_max = 0

        for i in range(1, len(input)):  # find best matching attribute
            if input[i][0] > input[index_max][0]:
                index_max = i

        return index_max


    def unique(self, list):
        newList = []

        for l in list:
            if not (l in newList):
                newList.append(l)
        return newList

    def probability(self, x, xArray):
        count = 0

        for xi in xArray:
            if x == xi:
                count = count + 1
        return count / float(len(xArray))

    def entrophy(self, xArray):
        xUnique = self.unique(xArray)
        sum = 0.0

        for x in xUnique:
            px = self.probability(x, xArray)
            sum -= px * log(px, 2)
        return sum

    def infoGain(self, S, A):

        attrUnique = self.unique(A)
        sum = 0
        returnList = []
        myDict = {}

        for attr in attrUnique:
            subS = []

            for i in range(0, len(A), 1):
                if A[i] == attr:
                    subS.append(S[i])

            pxe = self.probability(attr, A) * self.entrophy(subS)
            myDict[attr] = pxe
            sum = sum + pxe

        sum = self.entrophy(S) - sum

        returnList.append(sum)
        returnList.append(myDict)

        '''
        struct
        {
            float infogain                  # counted infogain for 
            list of dict {name : value}     # dictionary of attributes and their probability
        }
        '''
        return returnList

    def printInTable(self):
        for j in range(0, len(self.A[0])):
            for i in range(0, len(self.A)):
                sys.stdout.write(str(self.A[i][j]) + "\t"*2)
            sys.stdout.write(str(self.CL[j]))
            sys.stdout.write("\n")
        sys.stdout.write("\n")