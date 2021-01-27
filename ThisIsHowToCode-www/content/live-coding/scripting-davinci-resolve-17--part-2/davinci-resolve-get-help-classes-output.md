---
title: DaVinci Resolve 17 Script Classes
date: 1610662155
tags: 
- DaVinci Resolve 
- Automation 
- Python 
---

This script:


    import imp
    lib = 'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll'
    dvr_script = imp.load_dynamic('fusionscript', lib)

    resolve = app.GetResolve()
    print(resolve.GetHelp())

Produces this output for help with DaVinci Resolve Scripting. Works in version 17. Your milage may vary in other versions. 


    Classes:
        PolylineMask
        Loader
        QueueManager
        RenderJob
        RenderSlave
        FloatLUTMacroFrame
        Parameter
        SourceOperator
        Operator
        PlainOutput
        Link
        PlainInput
        SplineEditorView
        TimelineView
        EffectView
        FuView
        FuFrame
        FloatViewFrame
        Preview
        GLImageViewer
        GL3DViewer
        GLViewer
        GLView
        GLPreview
        TimeRegion
        Object             - The root class of all objects in FusionScript
        List
        FlowView
        TransformMatrix
        LUT
        LookUpTable
        Image
        Gradient
        BezierSpline
        IOClass
        UITimer
        UIFont
        UITabBar
        UITreeItem
        UITree
        UIDoubleSpinBox
        UISpinBox
        UITextEdit
        UILineEdit
        UICheckBox
        UIComboBox
        UIColorPicker
        UISlider
        UILabel
        UIButton
        UIStack
        UIDialog
        UIWindow
        UIWidget
        UIItem
        UIManager
        UIActionTree
        UIActionStrip
        Event
        ActionMode
        Action
        ConfigItem
        ActionManager
        PlaybackManager
        BinManager
        BinItem
        Registry           - Represents a type of object within Fusion
        MailMessage
        ImageCacheManager
        HotkeyManager
        Composition
        FontList
        Fairlight
        ChildGroup
        ChildFrame
        FusionUI
        Fusion
        ResolveScriptable
        Media pool item
        Folder
        ProjectManager
        MediaStorage
        Timeline item
        MediaPool
        Resolve
        Timeline
        Project
        ScriptServer