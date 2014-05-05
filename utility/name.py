

def nameSelection( name ):
    """
        Iterate through selection and name selection
        if %s sub char is in string sub in numbers
        
        >>> nameSelection("l_sabreTooth%s_ply")
    """
    
    selection = cmds.ls(sl=1)
    iter = 1
    
    if "%s" in name:
        for sel in selection:
            cmds.rename(sel, name%iter)
            iter += 1
               
    else:
        for sel in selection:
            cmds.rename(sel, name)  
            


