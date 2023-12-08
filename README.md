## AirBnB_clone

## Project Description:

This project involves building a command interpreter for managing AirBnB objects, which is the first step towards creating a full web application.
The project involve:
1-Implement a parent class named BaseModel responsible for the initialization, serialization, and deserialization of future instances.
2- Establish a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
3- Create classes for AirBnB entities (e.g., User, State, City, Place) that inherit from the BaseModel.
4- Develop the first abstracted storage engine for the project: File storage. 
5- Implement comprehensive unit tests to validate all classes and the storage engine.

## Description of the command interpreter:
The interface of the application is just like a shell except that it has a limited number of accepted commands that were defined for the purposes of using the AirBnB website.
## Usage
The command interpreter supports various commands for managing AirBnB objects:
1- show
2- create
3- update
4- destroy
5- all
6- help
7- exit
Example:
```bash
(hbnb) create User
f1d9258e-a313-4ca5-a8e9-6eab2f285250
(hbnb) all
["[User] (f1d9258e-a313-4ca5-a8e9-6eab2f285250) {'id': 'f1d9258e-a313-4ca5-a8e9-6eab2f285250', 'created_at': datetime.datetime(2023, 12, 7, 13, 18, 3, 422757), 'updated_at': datetime.datetime(2023, 12, 7, 13, 18, 3, 422774)}"]
(hbnb) all User
["[User] (f1d9258e-a313-4ca5-a8e9-6eab2f285250) {'id': 'f1d9258e-a313-4ca5-a8e9-6eab2f285250', 'created_at': datetime.datetime(2023, 12, 7, 13, 18, 3, 422757), 'updated_at': datetime.datetime(2023, 12, 7, 13, 18, 3, 422774)}"]
show User f1d9258e-a313-4ca5-a8e9-6eab2f285250
[User] (f1d9258e-a313-4ca5-a8e9-6eab2f285250) {'id': 'f1d9258e-a313-4ca5-a8e9-6eab2f285250', 'created_at': datetime.datetime(2023, 12, 7, 13, 18, 3, 422757), 'updated_at': datetime.datetime(2023, 12, 7, 13, 18, 3, 422774)}
(hbnb) destroy User f1d9258e-a313-4ca5-a8e9-6eab2f285250
(hbnb) all User
[]
(hbnb) update User f1d9258e-a313-4ca5-a8e9-6eab2f285250 email "l@gmail"
** no instance found **
(hbnb) create City
e4557bf3-5997-425f-b3e1-6ea708729b44
(hbnb) update City e4557bf3-5997-425f-b3e1-6ea708729b44 name "Paris"
(hbnb) show City e4557bf3-5997-425f-b3e1-6ea708729b44
[City] (e4557bf3-5997-425f-b3e1-6ea708729b44) {'id': 'e4557bf3-5997-425f-b3e1-6ea708729b44', 'created_at': datetime.datetime(2023, 12, 7, 13, 18, 15, 394896), 'updated_at': datetime.datetime(2023, 12, 7, 13, 23, 11, 498743), 'name': 'Paris'}
(hbnb) quit
```

## Table of Contents

- [Environment](#environment)
- [Installation](#installation)
- [Usage](#usage)


## Environment
This project is interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Installation

How to install the project.

```bash
# installation commands
git clone https://github.com/Lailaebrahim/AirBnB_clone.git
cd AirBnB_clone
./console.py
```
