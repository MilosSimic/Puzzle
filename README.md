#<img src="https://raw.githubusercontent.com/MilosSimic/Puzzle/master/images/puzzle.gif" width="100"/> Puzzle
Small plugin framework for python v2.1

## Plugin lifecycle
Every plugin must inherite Plugin class and override methods in order to work properly and safe. Every plugin inherit 
plugin lifecucle:
#<img src="https://github.com/MilosSimic/Puzzle/blob/master/images/lifecycle.png" width="500"/>

## Getting started
```
import os

...
```
## Features
- Load new plugins
- Show table with installed plugins and their states
- Maintain plugin lifecycle
- Download zip archive with plugin content and install it automatically
- Remove,update, register/install plugins
- Prepare any folder as <i>plugins</i> folder
- If plugin change, reload/refresh installed plugin
- Maintain security before plugin loads
- Simple interface to develop new plugins
