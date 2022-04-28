import sd

import os
from functools import partial

from PySide2 import QtWidgets

explorerCreatedCallbackID = None
explorerSelectionChangedCallbackIDs = []

def onActionTriggered(explorerID, uiMgr):
    '''Called when the user clicks on the toolbar icon.'''

    print("Selected items:")
    print("---------------")
    for item in uiMgr.getExplorerSelection(explorerID):
        print(item)
    print("\n")

def explorerSelectionChanged(explorerID, uiMgr, action, originalExplorerID):
    '''Called when the selection in the explorer panel changes.'''

    # Ignore callbacks for other explorer panels.
    if explorerID != originalExplorerID:
        return

    print("Explorer selection changed, id = %s" % explorerID)

    # Enable or disable the action depending on the explorer selection.
    selection = uiMgr.getExplorerSelection(explorerID)
    action.setEnabled(len(selection) != 0)

def explorerCreated(explorerID, uiMgr):
    '''Called when a new explorer panel is created.'''

    print("Explorer created, id = %s" % explorerID)

    # Warning: It is important to parent the action to some Qt object.
    # If the action is not parented, Python will garbage collect it.
    act = QtWidgets.QAction("P", parent=uiMgr.getMainWindow())
    uiMgr.addActionToExplorerToolbar(explorerID, act)
    act.setToolTip("Print explorer selection to the console")
    act.triggered.connect(partial(onActionTriggered, explorerID=explorerID, uiMgr=uiMgr))

    # Register a selection changed callback to update the action enabled state.
    global explorerSelectionChangedCallbackIDs
    explorerSelectionChangedCallbackIDs.append(uiMgr.registerExplorerSelectionChangedCallback(
        partial(explorerSelectionChanged, uiMgr=uiMgr, action=act, originalExplorerID=explorerID)))

    # Set initial enabled / disabled state.
    explorerSelectionChanged(explorerID, uiMgr, act, explorerID)

def initializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    # Register an explorer created callback to add actions to newly created explorer toolbars.
    global explorerCreatedCallbackID
    explorerCreatedCallbackID = uiMgr.registerExplorerCreatedCallback(partial(explorerCreated, uiMgr=uiMgr))

def uninitializeSDPlugin():
    ctx = sd.getContext()
    app = ctx.getSDApplication()
    uiMgr = app.getQtForPythonUIMgr()

    # Unregister all callbacks.
    global explorerCreatedCallbackID
    uiMgr.unregisterCallback(explorerCreatedCallbackID)

    global explorerSelectionChangedCallbackIDs
    for callbackID in explorerSelectionChangedCallbackIDs:
        uiMgr.unregisterCallback(callbackID)