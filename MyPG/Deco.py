from sd.api.sdhistoryutils import SDHistoryUtils


class NCPUndo:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with SDHistoryUtils.UndoGroup("NCP Undo Group"):
            self.func(*args, **kwargs)
