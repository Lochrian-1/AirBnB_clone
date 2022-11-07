# AirBnB clone

## Overview

This is the first of several steps towards building a clone of the AirBnB website. In this first project we will focus on creating a command interpreter that will be both interactive and non-interactive when executing the commands of the user.

### Description:
#### Command Interpreter

This command interpreter (console) will be able to take the inputs of the user, and similar to the simple shell project, be able to read the input and execute the spcific command. The console will be both interactive as well as not interactive.

INTERACTIVE:

To run the console in *interactive* mode type:

```$ ./console.py```

This prompt will appear:

```(hbnb) ```

where you can type commands and get output. For example:

```bash
(hbnb) all
["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
```

NON-INTERACTIVE:

The same commands can be used to run non-interactive mode with some modifications will produce the same results as above:

```bash
$ echo "all" | ./console.py
["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
```

You can also use a file that contains the commands you want to run:
```bash
$ cat commands.txt
all User
```

```bash
$ cat commands.txt | ./console.py
["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
```
