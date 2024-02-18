                 # **An AirBnB clone**
##  **Description**
   ALX AirBnB clone is a full web application integrating a front-end interface known as the console, a back-end API and a database storage.
   It is a team project that is part of the ALX software Engineering Program representing the first step into building a complete web application.
   It consists of:
 -  Custom data management command-line interface
 -  Base classes for storage of the data
   
 ## **Usage**
  The console can be used in both ineractive and non-interactive modes like a Unix shell which prints a prompt (hbnb) that waits for user input.
*  run the console  `./console`
*  Quit the console  `(hbnb) quit`
*  Display help command `(hbnb) help command`
*  Create object `(hbnb) create <class>`
*  Show object `(hbnb) show <class> <id>`
*  Destroy object `(hbnb) destroy <class> <id>`
*  Show all objects or instances of class `(hbnb) all`
*  Update attribute of object `(hbnb) update <class> <id> <attribute name> "<attribute value>"`

  An example of interactive mode:
  $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

An example of non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

## **Testing**
Testing of the ALX Airbnb clone project is accomplished using `Unittests` defined in the tests folder. Simultaneous testing of the entire suite is done using the following command:
$ `python3 unittest -m discover tests`
Single testing of modules uses the following command:
$ `python3 unittest -m tests/test_console.py`

## **Authors**:
Elizabeth Motsinone <mahlatsemotsinone@gmail.com>
Joshua Mutuse <joshmutuse@yahoo.com>
