# HTMLer

HTMLer is a simple HTML generation library for Python.


## Build status

[![Build Status](https://travis-ci.org/ashep/htmler.svg?branch=master)](https://travis-ci.org/ashep/htmler)
[![Coverage](https://codecov.io/gh/ashep/htmler/branch/master/graph/badge.svg)](https://codecov.io/gh/ashep/htmler)


## Features

* Easy and flexible to use.
* Outputs beautifully indented code


## Requirements

Python >=3.6


## Installation

```bash
pip install htmler
```

## Usage

This example:

```python
from htmler import Html, Head, Body, Meta, Title, Script, Link, P, A

doc = Html(
    Head(
        Meta(charset='utf-8'),
        Title('Hello World Document'),
        Script(src='main.js'),
        Link(rel='stylesheet', src='main.css'),
    ),
    Body(
        P(
            A('Hello World!', href="https://en.wikipedia.org/wiki/%22Hello,_World!%22_program")
        )
    ),
    lang="en",
)

print(doc)
```

will provide following output:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>
            Hello World Document
        </title>
        <script src="main.js"></script>
        <link rel="stylesheet" src="main.css">
    </head>
    <body>
        <p>
            <a href="https://en.wikipedia.org/wiki/%22Hello,_World!%22_program">Hello World!</a>
        </p>
    </body>
</html>
```

If indentation is not necessary, just call `render()` method with `indent` 
argument set to `False`:

```python

print(doc.render(indent=False))
``` 


## Documentation

Work in progress.


## Testing

```bash
python setup.py test
```

or

```bash
make test
```


## Contributing

If you want to contribute to a project and make it better, your help is very 
welcome. Contributing is also a great way to learn more about social coding on 
Github, new technologies and and their ecosystems and how to make constructive, 
helpful bug reports, feature requests and the noblest of all contributions: 
a good, clean pull request.

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called 
  `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into 
  your local repository.
- Create a new branch to work on. Branch from `develop` if it exists, else from 
  `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them.
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's interactive rebase. Create 
  a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's 
  `develop` branch if there is one, else go for `master`.
- If the maintainer requests further changes just push them to your branch. 
- Once the pull request is approved and merged you can pull the changes from 
  `upstream` to your local repo and delete your extra branch(es).

And last but not least: Always write your commit messages in the present tense. 
Your commit message should describe what the commit, when applied, does to the 
code – not what you did to the code.


## Roadmap

* Write documentation.


## Support

If you have any issues or enhancement proposals feel free to report them via 
project's [Issue Tracker](https://github.com/ashep/htmler/issues). 


## Authors

* [Oleksandr Shepetko](https://shepetko.com) -- initial work.


## Credits

This project was inspired by [PyHTML](https://github.com/cenkalti/pyhtml) 
library.


## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) 
file for details.
