from . import Event

class Observable(object):
    def __init__(self):
        self.callbacks = []

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def notify(self, **attrs):
        e = Event()
        e.source = self
        for k, v in attrs.iteritems():
            setattr(e, k, v)
        for fn in self.callbacks:
            fn(e)