from struct import *

class Serializer(object):
    def __init__(self, result = None):
        if result is None: result = ""
        self.result = result
        self.bufferPointer = 0
        
    def __str__(self):
        return self.to_string(self.result)
        
    def to_string(self, input):
        result = ""
        for i in self.result:
            result += "[%s]" % hex(ord(i))
        return result
        
    def writeObjectData(self, value, type):
        # writeObjectData(ByteBuffer buffer, Object object)
        # write object into buffer
        # http://docs.python.org/2/library/struct.html
        if type == "int": # 4 byte
            val = pack("i", value)
            self.result += val
            return val
        elif type == "string":
            leng = len(value)
            val = pack("%ds" % leng, value)
            self.result += val
            #print val
            return val
        elif type == "timestamp":
            value = "%s" % value
            leng = len(value)
            
            # When leng is 12, it means (I believe) there is only one number after
            # the decimal
            if leng == 12:
                value += "0"
                leng += 1
                
            if (leng != 13):
                print value
                raise Except("timestamp string length is not 13")
            
            val = pack("%ds" % leng, value)
            self.result += val
            #print val
            return val
            
        else:
            raise Exception("wrong type")
            
    def readObjectData(self, buffer, type):
        # readObjectData(ByteBuffer buffer, Class<T> type)
        if type == "int": # 4 byte reader
            val = unpack("i", buffer)
            return val[0]
        elif type == "string":
            length = len(buffer)
            val = unpack("%ds" % length, buffer)
            return val[0]
        elif type == "timestamp":
            length = 13 # len(buffer)
            val = unpack("%ds" % length, buffer)
            return float(val[0])
    
    def autoReadObjectData(self, type):
        if type == "int": # 4 byte reader
            length = 4
            buffer = self.result[self.bufferPointer:self.bufferPointer + length]
            val = unpack("i", buffer)
            self.bufferPointer += length
            return val[0]
        elif type.startswith("string"):
            length = int(type[len("string"):])
            buffer = self.result[self.bufferPointer:self.bufferPointer + length]
            val = unpack("%ds" % length, buffer)
            self.bufferPointer += length
            return val[0]
        elif type == "timestamp":
            length = 13 # len(buffer)
            buffer = self.result[self.bufferPointer:self.bufferPointer + length]
            val = unpack("%ds" % length, buffer)
            self.bufferPointer += length
            return val[0]
    
    def reset(self):
        self.result = ""
        self.bufferPointer = 0
        
    def getResult(self):
        return self.result
        
    def resetBufferPointer(self):
        self.bufferPointer = 0
        
    def size(self):
        """
        Returns the size of the element
        """
        return len(self.result)
    
if __name__ == "__main__":
    import sys
    sys.path.append("../test")
    from testSerializer import *
    unittest.main(verbosity=2)