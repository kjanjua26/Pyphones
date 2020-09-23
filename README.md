# Pyphones
Homophones of a word in Python from the the world's only complete homophone list. A Python wrapper for the homophone list.
Pyphones generates the homophones of a word from the world's only complete homophone list (taken from: https://www.homophone.com/).

## Usage
Calling help on the class Pyphones returns.

```
Help on class Pyphones in module main:

class Pyphones(builtins.object)
 |  Pyphones(word)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, word)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  get_the_homophones(self)
 |      Get the homophones of the word.
 |      
 |      Returns
 |          dict: {word: [list_of_homophones]} against each word.
 |  
 |  get_the_page(self, page_no=1)
 |      Get the page content.
 |      
 |      Returns
 |          str: the content of the page.
 |  
 |  get_the_page_nos(self)
 |      Get the total number of pages
 |      
 |      Returns
 |          int: the total number of the pages.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

```

To use, simply import the Pyphones from ```main.py```.
### Example

```
py = Pyphones("see")
homophones = py.get_the_homophones()
print(homophones)
```

Returns:

```
{'see': [['axseed', 'accede'], ['oversees', 'overseas'], 
['reseed', 'recede'], ['reseeded', 'receded'], ['reseeding', 'receding'], 
['see', 'c', 'cee', 'sea'], ['seed', 'cede'], ['seeder', 'cedar', 'ceder'], 
['seeding', 'ceding'], ['seeds', 'cedes'], ['seel', 'ceil', 'seal'], 
['seem', 'seam'], ['seemed', 'seamed'], ['seems', 'seams'], ['seen', 'scene'], 
['seer', 'cere', 'sear', 'sere'], ['seers', 'sears'], 
['sees', "c's", 'cees', 'seas', 'seize']]}
```
