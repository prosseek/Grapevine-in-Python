class ContextSummary:
    def __init__(self, id, db):
        self.db = db
        self.id = id
        
    def __str__(self):
        return str(self.db)
        
    def getId(self):
        return self.id
        
    def get(self, key):
        if key in self.db:
            return self.db[key]
        return None
        
    def put(self, key, value):
        self.db[key] = value
        
    def containsKey(self, key):
        return key in self.db
        
    def remove(self, key):
        if self.containsKey(key):
            del self.db[key]
            
        
if __name__ == "__main__":
    import sys
    sys.path.append("../test")
    from testContextSummary import *
    unittest.main(verbosity=2)
