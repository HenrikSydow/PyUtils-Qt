from PySide6.QtWidgets import QLabel, QWidget

from src.qt_util.qt_color import QtColor


# Disable naming inspections and use camel-case to maintain continuity with pyside naming.
# noinspection PyPep8Naming
class ColoredLabel(QLabel):
    """
    ColoredLabel is a standard QLabel with additional coloring methods,
    for changing the text color.
    """
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)

        self._font_color: QtColor = QtColor.White

    def fontColor(self) -> QtColor:
        return self._font_color

    def setFontColor(self, color: QtColor) -> None:
        self._font_color: QtColor = color
        self._update_style()

    def _update_style(self) -> None:
        style = self.styleSheet()
        self.setStyleSheet(f"color: {self._font_color};")
