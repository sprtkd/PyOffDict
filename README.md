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
print(dct.lookup('human'))
```
#### Output: 
Belonging to man or mankind; having the qualities or attributes of a man; of or pertaining to man or to the race of man; as, a human voice; human shape; human nature; human sacrifices. To err is human; to forgive, divine. Pope.\n\nA human being. [Colloq.] Sprung of humans that inhabit earth. Chapman. We humans often find ourselves in strange position. Prof. Wilson.

## Example:
```
print(dct.lookup('said'))
```
#### Output: 
imp. & p. p. of Say.\n\nbefore-mentioned; already spoken of or specified; aforesaid; -- used chiefly in legal style.
