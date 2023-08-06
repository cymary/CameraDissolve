
def CameraDissolve():
    # select nodes
    sNodes = nuke.selectedNodes()

    # Get Camera
    aCamNode = sNodes[-1]
    bCamNode = sNodes[0]

    # Get Camera Name 
    aCamName = aCamNode.name()
    bCamName = bCamNode.name()


    print (aCamNode.name())
    print (bCamNode.name())

    # DisSelected Node
    for node in sNodes:
        node['selected'].setValue(0)

    # Create new Camera
    nCamera = nuke.createNode('Camera3')
    nCamera['tile_color'].setValue(0x7f00ffff)
    nCamera['label'].setValue('CameraDissolve')



    #Prepare Reference Camera Python expression content 

    deselectAllNodes = '[n.knob("selected").setValue(False) for n in nuke.allNodes()]'
    
    pySelectACam = 'nuke.toNode(\'%s\')["selected"].setValue(1)'%aCamName
    pySelectBCam = 'nuke.toNode(\'%s\')["selected"].setValue(1)'%bCamName
    
    
    
    
    
    pyCopyCamToMem = 'nuke.nodeCopy("%clipboard%")'
    pypasteRetimeCam = 'RetimeCam = nuke.nodePaste("%clipboard%")'

    pyDisconnectAll = 'RetimeCam.setInput(0, None)'
    pyLabel = 'RetimeCam["label"].setValue("Retimed")'
    
    #combine all the python code inside the script botton
    
    aCamRetimePyContent = '{}{}{}{}{}{}{}{}{}{}{}'.format(deselectAllNodes,'\n',pySelectACam,'\n',pyCopyCamToMem,'\n',pypasteRetimeCam,'\n',pyDisconnectAll,'\n',pyLabel)
    bCamRetimePyContent = '{}{}{}{}{}{}{}{}{}{}{}'.format(deselectAllNodes,'\n',pySelectBCam,'\n',pyCopyCamToMem,'\n',pypasteRetimeCam,'\n',pyDisconnectAll,'\n',pyLabel)


    
    # Create custom CamDissove tag and knobs 
    camMixSliderTab = nuke.Tab_Knob('cameraDissolveTab', 'CamDissolve')
    aCamTimeOffsetknob = nuke.Int_Knob('aCameraOffset', 'A Cam Time Offset',0)
    bCamTimeOffsetknob = nuke.Int_Knob('bCameraOffset', 'B Cam Time Offset',0)   
    camMixSliderKnob = nuke.Double_Knob('camDissolve','Camera Dissolve')
    aCamRetimed = nuke.PyScript_Knob('aCamRetimed','Create Retimed A Cam',aCamRetimePyContent)
    bCamRetimed = nuke.PyScript_Knob('bCamRetimed','Create Retimed B Cam',bCamRetimePyContent)   
    
    # Collect all the knob as List

    panelKnobs = [camMixSliderTab,aCamTimeOffsetknob,aCamRetimed,bCamTimeOffsetknob,bCamRetimed,camMixSliderKnob]
    
    # Add all the knobs to Panel 
    
    for panelKnobs in panelKnobs:
        nCamera.addKnob(panelKnobs) 
   

    # Get All The Knob Would Like to Blend

    knobsList =[
    'translate','rotate','scaling','uniform_scale','skew',
    'pivot_translate','pivot_rotate','focal','haperture','vaperture',
    'near','far','win_translate','win_scale','winroll','focal_point','fstop'
    ]




    for knob in knobsList:
        
        nCamera[knob].setExpression('lerp({}.{}{},{}.{}{},{})'.format(aCamName,knob,'(frame-aCameraOffset)',bCamName,knob,'(frame-bCameraOffset)','camDissolve'))
        
        
CameraDissolve()




