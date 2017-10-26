# ios-togglebutton-for-maya
iOS Toggle Button Style for Autodesk Maya (2014, 2016, 2017, 2018), using PySide / PySide2 (Python for Qt)

## Class
Inherited from QWidget
```python
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

## Example Usage
```python
import toggle_button

# Default toggle button with 32 height, and blue color as the active color
widget = toggle_button.ToggleButton()
widget.show()

widget = toggle_button.ToggleButton(width=100, colorActive=toggle_button.RED)
widget.show()

widget = toggle_button.ToggleButton(height=20, colorActive=toggle_button.QtGui.QColor('#8BC34A'))
widget.show()

# A Square Toggle Button with custom size & colors
widget = toggle_button.ToggleButton(width=60, height=20,
                                    colorActive=toggle_button.QtGui.QColor(0,229,255),
                                    colorInactive=toggle_button.RED,
                                    colorSwitch=toggle_button.PINK,
                                    roundedCorner=False)
widget.show()

```
