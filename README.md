# AirBnB clone

## Overview

This is the first of several steps towards building a clone of the AirBnB website. In this first project we will focus on creating a command interpreter that will be both interactive and non-interactive when executing the commands of the user.

### Description:
#### Command Interpreter

This command interpreter (console) will be able to take the inputs of the user, and similar to the simple shell project, be able to read the input and execute the spcific command. With this console we want to be able to manage the objects of our project by:

- Creating new objects
- Retrieving an object from a file, a database etc…
- Doing operations on objects 
- Updating attributes of objects
- Destroying objects

The console will be both interactice as well as non-interactive.

INTERACTIVE:

To run the console in *interactive* mode, the user will type:

```$ ./console.py```

and the following prompt will appear:

```(hbnb) ```

whereby then user can then type commands and get output.
For example:

```bash
(hbnb) all
["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
```

After the command is executed, the console with have another prompt appear to allow the user to request a new command. This cycle will continue indefinitely until such time hat the user decides to exit the program.

NON-INTERACTIVE:

The same commands can be used in non-interactive mode ,with some modifications, that will produce the same results as above:

```bash
$ echo "all" | ./console.py
["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
```

Unlike with *interactive* mode, the user will pipe the command to the running of the program and as soon as the program executes the command given by the user, the program terminates. In this case we see that there is no prompt reappearing and so if the user should wish to run another command, the program would need to be run.


