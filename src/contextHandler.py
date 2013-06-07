class ContextHandler(object):
    singleton = None
    
    def __init__(self):
        self.singleton = None
        
    @staticmethod
    def getInstance():
        if ContextHandler.singleton is None:
            #print 'none'
            ContextHandler.singleton = ContextHandler()
        return ContextHandler.singleton
    
if __name__ == "__main__":
    import sys
    sys.path.append("../test")
    from testContextHandler import *
    unittest.main(verbosity=2)