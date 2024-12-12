<h1>Turko's GUI Library 1.7</h1>
This is a Python GUI Library build to improve on the inconsistencies and unnecessary confusing manner of the Tkinter GUI Library which is built into Python. Turko-lib is designed to be more similar to the style of interface design that web frameworks have and aims to implement similar features such as content justification and item alignment.

Some features of Turko-Lib that may be similar to traditional web-design and development may be responsive containers. (Similar to justify-content, align-items, display properties).

<h3>Installation</h3>

```python
git clone https://github.com/turko-dev/turko-lib.git

python3 app.py
```

<h3>Documentation</h3>

```python
from turko import *

turko = Turko()
turko.title("My Turko App")
turko.run()
```
Creating and deploying a GUI in Turko-Lib is much easier than while using a library such as Tkinter/PyQT.

```python
from turko import *

turko = Turko()
turko.title("My Turko App")
turko.run()
```

<h6>Initialise App</h6>

```python
turko = Turko()
```






<h3>Examples</h3>

```python

from turko import *

turko = Turko()
turko.minsize(200, 200)

frame1 = Frame(turko, width="50%", height=500, styleName="frame1", bg="green", borderwidth=2)
frame2 = Frame(frame1, width="50%", height=200, styleName="frame2", bg="orange", borderwidth=2)

turko.run()

```
![alt text](https://github.com/turko-dev/turko-lib/blob/main/eg.png)

![alt text](https://github.com/turko-dev/turko-lib/blob/main/eg2.png)
