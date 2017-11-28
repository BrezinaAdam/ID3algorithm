class Parser:

    def __init__(self, filename):
        file_object = open(filename, 'r')
        # toto treba dat do cykli
        lines = file_object.readlines()

        self.lst = []

        for i in range(0, len(lines[0].split())):
            self.lst.append(list())



        for i in range(1, len(lines)):
            a = lines[i].split(" ")
            for j in range(0, len(a)):
                if j == len(a)-1:
                    a[j] = a[j][:-1]
                self.lst[j].append(a[j])

    def getList(self):
        CL = self.lst[len(self.lst)-1]
        self.lst.pop(len(self.lst)-1)

        ret = [self.lst, CL]
        return ret