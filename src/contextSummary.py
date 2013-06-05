class ContextSummary:
    def __init__(self, db):
        self.db = db
    def get(self, key):
        return self.db[key]
    def put(self, key, value):
        self.db[key] = value
        
if __name__ == "__main__":
    db = {"GroupsEnumerated":3,
          "Group0":0,"Group1":1,"Group2":2
          }
    summary = ContextSummary(db)
    print summary.get("GroupsEnumerated")
    print summary.db