# destruction

Destroy Python programs with just a single import statement! Sounds fun,
doesn't it?

`destruction` is a simple module that will silently destroy a lot of Python
programs by manipulating values over time. For example, if you define a
`float` variable and then do some operations over time, you'll be in for a
surprise.

```python
>>> import destruction
>>> n1 = float(0.5)
>>> n2 = float(0.5)
>>> n1 + n2
0.9948744748218606
>>> n1 + n2
1.0009324588178117
>>> n1 + n2
0.9956876734263913
>>> n1 + n2
1.009620798598302
```

### What kind of sorcery is this?

Python has a module called `__builtin__` (it's called `builtins` in Python 3)
which contains all kinds of basic things. For example, the `float` class
resides in there.

`destruction` switches these classes for custom ones that do weird stuff to
break your program. For example, the `__add__` member function is overridden
with a custom one that adds a tiny, but non-zero number to the result. So it's
always wrong!

### Installation

```bash
$ pip install destruction
```

### Usage

To make the lives of your arch enemies miserable, sneak in the following line
anywhere in their Python code:

```python
import destruction
```

### Examples

#### Varying π and e

You saw the float example. Let's do something weirder:

```python
>>> import destruction
>>> import math
>>> math.pi
3.1349545779223096
>>> math.pi
3.1332825202115226
>>> math.pi
3.1332205700116864
>>> math.pi
3.1346367856853625
>>> math.pi
3.130824304762861
```

`pi` that slightly changes everytime you access it. Evil, I know. Same with `e`:

```python
>>> math.e
2.718878169620603
>>> math.e
2.723038508262948
>>> math.e
2.7308532846593865
```

The only caveat is that you must import `math` *after* you import destruction.
Slightly inconvinient, I admit.

### Contributing

All patches welcome! New, interesting, and evil ideas are always welcome :)

### LICENSE

```
MIT License

Copyright (c) 2017 Adhityaa Chandrasekar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
