# Faust-Bot
IRC Bot, derived from Pallaber Bot, Architectonic rework

Designed for non-technical channels

## Usage

### Requirements
 - Python 3.5
 - pip
 - wikipedia package (can be installed using pip; tested with version 1.4.0)
 
### Running the Bot
```bash
# First load all needed strings into the database
# Per default german is used. If you want another language you need to 
# add an language file and modify the script.
# Later it will be refactored, so it uses arguments
python ReadInternationalization.py
# Start the bot using the given config file.
python Main.py --config ./config.txt
``` 

## Contribution
Have a look into our issues. Some are explizitly marked as `help wanted` or `For Beginners`. If you're new to programming the last one would be a good point to begin with. Of course you're also free to choose your own issue or task to work on.
If you have any question you're also welcome to join us in `#faust-bot` on freenode.

Before creating a pull request please test your code. Untested, obviously buggy code will - of course - be rejected.
Since we're programming in python please hold on [PEP-08](https://www.python.org/dev/peps/pep-0008/).


## Copyright
```
    Faust-Bot. A simple, extensible IRC bot.
    Copyright (C) 2017  Sophie Bartmann, ravotd, Kristoffer Schneider

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
The `care_icd10_de.csv` was taken from the [CARE2X - Integrated Hospital Info System Project on Sourceforge](https://sourceforge.net/projects/care2002/).
