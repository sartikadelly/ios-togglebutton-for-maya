'''
module: toggle_button
iOS Style Toggle Button for Autodesk Maya (2014, 2016, 2017, 2018) using PySide / PySide2

https://github.com/sartikadelly/ios-togglebutton-for-maya
'''
try:
    from PySide2 import QtGui, QtCore, QtWidgets
except ImportError:
    from PySide import QtGui, QtCore
    import PySide.QtGui as QtWidgets

#------------------------------------------------------------------------------
# Color Palette from iOS Human Interface Guidelines
BLUE = QtGui.QColor(0, 122, 255)
BLUE_TEAL = QtGui.QColor(90, 200, 250)
BLUE_LIGHT = QtGui.QColor(33, 150, 243)
GRAY = QtGui.QColor(204, 204, 204)
GREEN = QtGui.QColor(76, 217, 100)
ORANGE = QtGui.QColor(255, 149, 0)
PINK = QtGui.QColor(255, 45, 85)
PURPLE = QtGui.QColor(88, 86, 214)
RED = QtGui.QColor(255, 59, 48)
WHITE = QtGui.QColor(255, 255, 255)
YELLOW = QtGui.QColor(255, 204, 0)

#------------------------------------------------------------------------------
class BackgroundWithColor(QtWidgets.QPushButton):
    '''
    Simple Background Color Class with color property that can be animated.

    :param int height: Height
    :param QColor color: Background color
    :param bool roundedCorner: Rounded/Square corner
    '''
    def __init__(self, parent=None, height=32, color=GRAY, roundedCorner=True):
        super(BackgroundWithColor, self).__init__(parent)
        self.border_radius = int(height * 0.5) if roundedCorner else 0
        self._color = color
        self.setColor(self._color)

    def getColor(self):
        return self._color

    def setColor(self, value):
        self._color = value
        css = 'background-color: rgb({0},{1},{2});'.format(value.red(), value.green(), value.blue())
        css += 'border-radius: {0}px;'.format(self.border_radius)
        self.setStyleSheet(css)

    color = QtCore.Property(QtGui.QColor, getColor, setColor)

#------------------------------------------------------------------------------
class ToggleButton(QtWidgets.QWidget):
    '''
    Toggle Button Class.
    Use state property to set/check status of the toggle button (active/inactive).

    :param QWidget parent: Parent widget
    :param int width: Width, default to (height * 2) if not provided
    :param int height: Height, default to (width * 0.5) if not provided.
                       Default to 32 if both width & height is not provided.
    :param QColor colorSwitch: Switch color.
    :param QColor colorActive: Background color when Toggle Button is active.
    :param QColor colorInctive: Background color when Toggle Button is inactive.
    :param bool roundedCorner: Rounded/square corner style.
    '''
    clicked = QtCore.Signal(bool)

    def __init__(self, parent=None,
                 width=None, height=None,
                 colorSwitch=WHITE,
                 colorActive=BLUE_LIGHT,
                 colorInactive=GRAY,
                 roundedCorner = True):

        super(ToggleButton, self).__init__(parent)
        hbox = QtWidgets.QHBoxLayout(parent)
        self.setLayout(hbox)

        if not any([width, height]):
            height = 32
        if width and not height:
            height = width * 0.5
        elif height and not width:
            width = height * 2

        self._state = False
        self.colorActive = colorActive
        self.colorInactive = colorInactive

        self.border_radius = int(height * 0.5) if roundedCorner else 0
        self.padding = int(0.125 * height)

        self.toggle_bg = BackgroundWithColor(parent=self, height=height, color=self.colorInactive, roundedCorner=roundedCorner)
        self.toggle_bg.setFixedSize(width, height)
        self.setFixedSize(width, height)
        self.toggle_bg.clicked.connect(self._doToggle)

        switch_width = height - (self.padding * 2)
        switch_border_radius = int(switch_width * 0.5) if roundedCorner else 0
        self.toggle_switch = QtWidgets.QLabel('')
        self.toggle_switch.setFixedSize(switch_width, switch_width)
        self.toggle_switch.setParent(self.toggle_bg)
        self.toggle_switch.move(self.padding, self.padding)
        self._setStyleSheet(self.toggle_switch, colorSwitch, switch_border_radius)

        hbox.addWidget(self.toggle_bg)
        hbox.setContentsMargins(0, 0, 0, 0)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        if self._state:
            self._setStyleSheet(self.toggle_bg, self.colorActive, self.border_radius)
            self.toggle_switch.move(self.toggle_bg.width()-self.toggle_switch.width()-self.padding, self.padding)
        else:
            self._setStyleSheet(self.toggle_bg, self.colorInactive, self.border_radius)
            self.toggle_switch.move(self.padding, self.padding)

    def _setStyleSheet(self, widget, color, border_radius):
        css = 'background-color: rgb({0},{1},{2});'.format(color.red(), color.green(), color.blue())
        css += 'border-radius: {0}px;'.format(border_radius)
        widget.setStyleSheet(css)

    def _doToggleAnim(self, xStart, xEnd, startColor, endColor):
        self.anim = QtCore.QPropertyAnimation(self.toggle_switch, b'pos')
        self.anim.setDuration(100)
        self.anim.setStartValue(QtCore.QPoint(xStart, self.padding))
        self.anim.setEndValue(QtCore.QPoint(xEnd, self.padding))
        self.anim.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

        self.animbg = QtCore.QPropertyAnimation(self.toggle_bg, b'color')
        self.animbg.setDuration(200)
        self.animbg.setStartValue(startColor)
        self.animbg.setEndValue(endColor)
        self.animbg.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    def _doToggle(self):
        self._state = not self._state
        self.clicked.emit(self._state)
        if self._state:
            self._doToggleAnim(self.padding, self.toggle_bg.width()-self.toggle_switch.width()-self.padding,
                               self.colorInactive, self.colorActive)
        else:
            self._doToggleAnim(self.toggle_bg.width()-self.toggle_switch.width()-self.padding, self.padding,
                               self.colorActive, self.colorInactive)
