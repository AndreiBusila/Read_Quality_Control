import gzip


class ReadQualityControl:
    def __init__(self, name_file):
        self.f = gzip.open(name_file, "rt")
        self.reads = self.f.read().split("\n")
        self.content = self.get_content()

        self.lens = []
        self.sequences = []
        self.gcReads = []
        self.nReads = []
        self.get_lens()
        self.get_sequences()
        self.get_gc()
        self.get_n()

        self.readsN = len(self.nReads) - self.nReads.count(0.0000)

    def get_content(self):
        return self.reads[1::4]

    def get_lens(self):
        for i in self.content:
            self.lens.append(len(i))

    def get_sequences(self):
        for i in self.content:
            self.sequences.append(i)

    def get_gc(self):
        for i in self.content:
            self.gcReads.append(round((i.count("G") + i.count("C")) / len(i), 4))

    def get_n(self):
        for i in self.content:
            self.nReads.append(i.count("N") / len(i))

    def display(self):
        print(f"Reads in the file = {len(self.lens)}:")
        print(f"Reads sequence average length = {round(sum(self.lens) / len(self.lens))}\n")

        print(f"Repeats = {len(self.sequences) - len(set(self.sequences))}")
        print(f"Reads with Ns = {self.readsN}\n")

        print(f"GC content average = {round(sum(self.gcReads) / len(self.gcReads) * 100, 2)}%")
        print(f"Ns per read sequence = {round(sum(self.nReads) / len(self.nReads) * 100, 2)}%")
        print()


test1 = ReadQualityControl(input())
test2 = ReadQualityControl(input())
test3 = ReadQualityControl(input())

dicts = {0: test1,
         1: test2,
         2: test3}
value = []
for key in dicts:
    value.append(dicts.get(key).readsN)

value_min = min(value)
dicts[value.index(value_min)].display()

