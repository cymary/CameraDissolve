def CameraDissolve():
    # Check if exactly two camera nodes are selected
    sNodes = nuke.selectedNodes()
    if len(sNodes) != 2 or not all(node.Class() == 'Camera3' for node in sNodes):
        nuke.message('Please select exactly two Camera nodes')
        return

    aCamNode, bCamNode = sNodes

    # Create new Camera nodes
    nCamera = nuke.createNode('Camera3')
    refACam = nuke.createNode('Camera3')
    refBCam = nuke.createNode('Camera3')

    # Create custom knobs
    knobs = [
        ('aCameraOffset', 'A Cam Time Offset'),
        ('bCameraOffset', 'B Cam Time Offset'),
        ('camDissolve', 'Camera Dissolve')
    ]
    for knob_name, knob_label in knobs:
        nCamera.addKnob(nuke.Int_Knob(knob_name, knob_label))
        refACam.addKnob(nuke.Int_Knob(knob_name))
        refBCam.addKnob(nuke.Int_Knob(knob_name))

    # List of camera attributes to blend
    knobs_to_blend = [
        'translate', 'rotate', 'scaling', 'uniform_scale', 'skew',
        'pivot_translate', 'pivot_rotate', 'focal', 'haperture', 'vaperture',
        'near', 'far', 'win_translate', 'win_scale', 'winroll', 'focal_point', 'fstop'
    ]

    for knob in knobs_to_blend:
        for ref_cam in [nCamera, refACam, refBCam]:
            ref_cam[knob].setExpression(
                f'lerp({aCamNode.name()}.{knob}, {bCamNode.name()}.{knob}, {ref_cam.name()}.camDissolve)'
            )

    # Set up expressions for custom knobs
    for ref_cam in [refACam, refBCam]:
        ref_cam['aCameraOffset'].setExpression(f'{nCamera.name()}.aCameraOffset')
        ref_cam['bCameraOffset'].setExpression(f'{nCamera.name()}.bCameraOffset')
        ref_cam['camDissolve'].setExpression('0 if this == %s else 1' % refACam.name())

        for knob_name in ['aCameraOffset', 'bCameraOffset', 'camDissolve']:
            ref_cam[knob_name].setEnabled(False)

CameraDissolve()
