class ContextSummary:
    def __init__(self, db):
        self.db = db
        
    def __str__(self):
        return str(self.db)
        
    def get(self, key):
        if key in self.db:
            return self.db[key]
        return None
        
    def put(self, key, value):
        self.db[key] = value
        
    def containsKey(self, key):
        return key in self.db
        
if __name__ == "__main__":
    import sys
    sys.path.append("../test")
    from testContextSummary import *
    unittest.main()
