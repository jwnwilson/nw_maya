import maya.cmds as mc

class ModelTool():
    """
        Modeling tool instance
    """
    def __init__(self):
        self.lastSelection = []
        
    def hideUnselected(self):
        hide = True
        self.lastSelection = mc.ls(sl = 1)
        
        for obj in mc.ls(o=1, typ= "transform"):
            hide = True
            decen = mc.listRelatives(obj, ad =1)
            if decen == None:
                decen = []
            for obj2 in (decen + [obj]):
                if obj2 in self.lastSelection:
                    print obj2, obj
                    hide = False
            if hide:
                mc.hide(obj)
                
    def unhideAll(self):
       for obj in mc.ls(o=1, typ= "transform"):
           if obj not in self.lastSelection:
                mc.showHidden(obj) 
                
if __name__ == "__main__":
    mt = ModelingTool()
    
