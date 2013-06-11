from serializer import *
from contextSummary import *

class ContextSummarySerializer(Serializer):
    def __init__(self):
        super(ContextSummarySerializer, self).__init__("")
        
    def writeSummaries(self, summaries):
        for summary in summaries:
            self.writeSummary(summary)
        return self.result
        
    def readSummaries(self):
        totalBufferLength = len(self.result)
        
        summaries = []
        self.resetBufferPointer()
        while self.bufferPointer < totalBufferLength:
            summary = self.readSummary()
            summaries.append(summary)
        #print totalBufferLength, self.bufferPointer
        return summaries
        
    def writeSummary(self, summary):
        uid = summary.getId()
        hops = summary.getHops()
        timestamp = summary.getTimestamp()
        size = summary.size()
        
        # def writeObjectData(self, value, type):
        self.writeObjectData(uid, "int")
        self.writeObjectData(hops, "int")
        self.writeObjectData(timestamp, "timestamp")
        self.writeObjectData(size, "int")
        
        for key in summary.keySet():
            #print key
            #print summary.get(key)
            self.writeObjectData(len(key), "int")
            self.writeObjectData(key, "string")
            self.writeObjectData(summary.get(key), "int")
        
        return self.result
        
    def readSummary(self): # , type):
        # __init__(self, uid, db, hops = 3, tau = 3, timestamp = None):
        uid = self.autoReadObjectData("int")
        hops = self.autoReadObjectData("int")
        timestamp = self.autoReadObjectData("timestamp")
        dbsize = self.autoReadObjectData("int")
        db = {}
        for i in range(dbsize):
            stringLength = self.autoReadObjectData("int")
            key = self.autoReadObjectData("string%d" % stringLength)
            value = self.autoReadObjectData("int")
            db[key] = value
            
        summary = ContextSummary(uid, db, hops, timestamp)
        #print summary
        return summary
        
if __name__ == "__main__":
    import sys
    sys.path.append("../test")
    from testContextSummarySerializer import *
    unittest.main(verbosity=2)