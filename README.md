# PyOffDict
Offline Python Dictionary

### Created by Suprotik Dey
@2018

PyOffDict is an Offline Dictionary for Python in English
Based on Webster's Unabridged English Dictionary
Data Taken from https://github.com/matthewreagan/WebstersEnglishDictionary

## Usage:
1. [Download](https://github.com/sprtkd/PyOffDict/archive/master.zip) this Repo and extract into your project as PyOffDict.
2. Example use:
```
from PyOffDict.pyoffdict import Dictionary
dct = Dictionary()

print(dct.get_numOfWords())
print(dct.lookup('good'))
```
### get_numOfWords()
Returns number of words in dictionary

### lookup(word)
Returns meaning or 'Unknown' if not in dictionary

## Example:
```
print(dct.lookup('said'))
```
#### Output: 
imp. & p. p. of Say.\n\nbefore-mentioned; already spoken of or specified; aforesaid; -- used chiefly in legal style.
