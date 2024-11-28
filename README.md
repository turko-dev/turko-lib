<h1>Turko's GUI Library 1.7</h1>
This is a Python GUI Library build to improve on the inconsistencies and unnecessary confusing manner of the Tkinter GUI Library which is built into Python. Turko-lib is designed to be more similar to the style of interface design that web frameworks have and aims to implement similar features such as content justification and item alignment.

Some features of Turko-Lib that may be similar to traditional web-design and development may be responsive containers (similar to <div></div>) and flexbox properties (similar to justify-content:space-evenly, align-items:center, etc.)

<h3>Installation</h3>
.

<h3>Documentation</h3>

```python
from turko import *

turko = Turko()
turko.title("My Turko App")
turko.run()
```

<h3>Examples</h3>

```python
from turko import *

turko = Turko()
frame1 = Frame(turko, "90%", "100px")

turko.run()
```

```

from turko import *

turko = Turko()
turko.minsize(200, 200)

frame1 = Frame(turko, width="50%", height=500, styleName="frame1", bg="green", borderwidth=2)
frame2 = Frame(frame1, width="95%", height=200, styleName="frame2", bg="orange", borderwidth=2)

turko.run()

```


Need to add the below:
1 - Labels / Done
2 - Fonts / Done
3 - Colours / Done
4 - Frames / Done
5 - Resizing / Done
6 - Button
7 - Text Input
8 - Layouts