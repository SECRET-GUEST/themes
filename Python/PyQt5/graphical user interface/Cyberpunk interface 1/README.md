Python version : 3.10 +
```

 ██████╗██╗   ██╗██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗ ██╗
██╔════╝╚██╗ ██╔╝██╔══██╗██║   ██║████╗  ██║██║ ██╔╝███║
██║      ╚████╔╝ ██████╔╝██║   ██║██╔██╗ ██║█████╔╝ ╚██║
██║       ╚██╔╝  ██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗  ██║
╚██████╗   ██║   ██║     ╚██████╔╝██║ ╚████║██║  ██╗ ██║
 ╚═════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═╝
                                                        
```

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

# Description

![image](https://user-images.githubusercontent.com/92639080/234392747-66b82440-04fb-4c0f-88fd-a11411a9edb5.png)

Cypunk1Window is a custom window class based on QMainWindow for PyQt5, allowing you to create a hexagonal window with custom buttons to minimize, close, and show the window. This class also enables you to apply custom styles to your window.

from here : https://github.com/SECRET-GUEST/Layer-one

###### The style script and images are just example


## Main Features:
- Hexagonal window shape
- Custom title bar with window movement handling
- Custom buttons to minimize, close, and show the window
- Support for stylesheets to customize appearance
- Pop up customised 


## Usage:

To use this class, import it into your project and create a new class that inherits from Cypunk1Window. In the new class, customize the window appearance by passing the required parameters (title, window size, button icons, and stylesheet) to the `__init__()` method of the parent class.

If you're using the message_box, it will be little more difficult to set.


For example , if you would like to set the pop up before the script, you will have to hide the close button and reload when the pop up is done, and if you're using a stylesheet, that you probably do, you will have to pass the stylesheet in argument of your pop up, here but also at the entry point.

here is an example of implementation, it's easier than it looks : 

```python
        self.msg_box = Cypunk1MessageBox(stylesheet_path=self.stylesheet_path) #Here your argument

        self.msg_box.setText("My first popup") 
        
        self.close_button_widget.hide() #Here you hide the close button
        
        result = self.msg_box.exec_()
        
        if result == QMessageBox.Ok:
            self.close_button_widget.show() #Here you can show 


if __name__ == '__main__'  :  
    app = QApplication(sys.argv)
    window = YOUR_APP_NAME(stylesheet_path="style/style1.txt") #Here your argument at the entry point
    window.show()
    sys.exit(app.exec_())
    
```

You won this : 

![image](https://user-images.githubusercontent.com/92639080/234444006-133ed1be-213b-4575-b672-ae7f1b0730d4.png)
  
    
### Example:

An example of how to use this code awaits you in another file, named `example_test.py`:

