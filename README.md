# Welcome to the AirBnB clone project!

![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/108541991/237051537-e1b0df18-bb56-47c2-8b88-a3c57b3d8110.png)


## Project Description
The AirBnB clone project where we will be focusing on building the backend of the application using Python and interfacing it with a console application using the `cmd` module. The goal of the project is to deploy on your server a simple copy of the AirBnB website.


## Background Context
First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: `HTML/CSS templating`, `database storage`, `API`, `front-end integration`…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the `initialization`, `serialization` and `deserialization` of your future instances
- create a simple flow of `serialization/deserialization`: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine


## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


## GitHub
**There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.**


## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
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
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
![815046647d23428a14ca2](https://user-images.githubusercontent.com/108541991/237051602-a16451e7-645d-4e1f-81ff-dad5f72ed955.png)


## Final product
![fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4](https://user-images.githubusercontent.com/108541991/237052655-41c225b9-27fc-40fc-a8d5-2dd4ef1aecef.png)
![da2584da58f1d99a72f0a4d8d22c1e485468f941](https://user-images.githubusercontent.com/108541991/237052700-0ffba28d-591e-4f94-8078-ab56af4f4c95.png)

## Author
Samuel Amsalu

