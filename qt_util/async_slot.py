from threading import Thread


class AsyncSlot:
    """
    Asynchronous slot. Wrapper class for slot methods / functions.
    The slot will be executed in its own thread.
    """
    def __init__(self, slot: callable) -> None:
        self._slot: callable = slot

    def __call__(self, *args, **kwargs) -> None:
        Thread(target=lambda: self._slot(*args, **kwargs)).start()
