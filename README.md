# ios-togglebutton-for-maya
iOS Toggle Button Style for Autodesk Maya (2014, 2016, 2017, 2018), using PySide / PySide2 (Python for Qt)

## Class
Inherited from *QtWidgets.QWidget*
```python
class ToggleButton(QtWidgets.QWidget)

class ToggleButton(parent=None,
                   width=None, height=None,
                   colorSwitch=WHITE,
                   colorActive=BLUE_LIGHT,
                   colorInactive=GRAY,
                   roundedCorner = True)
```                 

### Parameters
Type | Flag | Description
--- | --- | ---
QWidget | parent | Parent widget
int | width | Width, default to (height * 2) if not provided
int | height | Height, default to (width * 0.5) if not provided.<br>Default to 32 if both *width & height is not provided*.
QColor | colorSwitch | Switch color.
QColor | colorActive | Background color when Toggle Button is active.
QColor | colorInctive | Background color when Toggle Button is inactive.
bool | roundedCorner | Rounded / Square corner style.

### Properties
Type | Name | Description
--- | --- | ---
bool | state | Toggle button state

### Signal
| Name | Description
--- | ---
clicked(*bool*) | Called when toggle button is clicked

## Example Usage
```python
import toggle_button

def print_me(state):
  print 'Toggle State: ', state

# Default toggle button with 32 height, and blue color as the active color
widget = toggle_button.ToggleButton()
widget.show()
widget.clicked.connect(print_me)
```
![alt text](https://github.com/sartikadelly/ios-togglebutton-for-maya/blob/master/screenshots/toggle_example_01.png "Toggle Button Example 01")

```python
import toggle_button

widget = toggle_button.ToggleButton(width=100, colorActive=toggle_button.RED)
widget.show()
```
![alt text](https://github.com/sartikadelly/ios-togglebutton-for-maya/blob/master/screenshots/toggle_example_02.png "Toggle Button Example 02")

```python
import toggle_button
widget = toggle_button.ToggleButton(height=20, colorActive=toggle_button.QtGui.QColor('#8BC34A'),
                                    colorInactive=toggle_button.QtGui.QColor('#FF9800'))
widget.show()
```
![alt text](https://github.com/sartikadelly/ios-togglebutton-for-maya/blob/master/screenshots/toggle_example_03.png "Toggle Button Example 03")

```python
import toggle_button
# A Square Toggle Button with custom size & colors
widget = toggle_button.ToggleButton(width=100, height=40,
                                    colorActive=toggle_button.QtGui.QColor(149,117,205),
                                    colorInactive=toggle_button.QtGui.QColor(77,182,172),
                                    colorSwitch=toggle_button.QtGui.QColor(240,244,195),
                                    roundedCorner=False)
widget.show()
```
![alt text](https://github.com/sartikadelly/ios-togglebutton-for-maya/blob/master/screenshots/toggle_example_04.png "Toggle Button Example 04")
