# INET 4031 Add Users Script + User List
Repository for holding adduser script for our Virtual Machine in INET4031 (Spring 2026) - Created by Elias Vera-Jimenez

## Program Description
The program `create-users.py` is a script that, when passed specified fields, will automattically generate users with:
1. a username
2. a password
3. a first name 
4. a last name
5. **PRE-EXISTING** groups passed in as field arguments

**WARNING:** The program will not create groups for you, only users. if the group passed does not exist, the program will fail when trying to add the user to a nonexistant group.

The program runs 3 OS command line statements. The script:
1. Runs the `adduser` command to add a given user, using fields 1, 3, and 4 from above.
2. Runs a command that will `echo` a user's password from field 2 into the `/usr/bin/passwd` file, assigned to the correct associated user.
3. Runs the `adduser` command again, this time to assign given user to the group or groups passed in from field 5.

If the program is passed in the correct fields, it should generate the users passed as arguments or input, and add them as accessible users to the machine.

## Program user operation - Running the program

### Granting proper permissions to run the program.
In order to run the program, ensure that your user has the correct permissions to run the file if running a dry-run, which can be done with the following:

```bash
$ chmod u+x create-users.py
```

This command will make the program executable. The program is set up to run using python 3, so ensure a version is installed on your system before running the program. 


### Input File Formatting

This script is meant to be used in tandem with `create-users.input`, the formatting for this file is as follows.

```txt
<username>:<password>:<last name>:<first name>:<group>,<group>,<group>
```
Extra groups after the first can be left out, and groups can be skipped altogether with a `-`.

Some examples:

**A user with 1 group assigned**
```txt
user01:pass01:Last01:First01:group01
```

**A user with 2 groups assigned**
```txt
user02:pass02:Last02:First02:group01,group02
```

**A user with no groups assigned**
```txt
user03:pass03:Last03:First03:-
```

**WARNING:** users in either `create-users.input` and/or users passed as arguments to `create-users.py` will not be generated and will be skipped. if running outside of a dry run, the script will not notify you that a user has been skipped.

### Running the Program
Once your create-users.input is updated to generate the correct users, run:
```bash
$ ./create-users.py < create-users.input
```

If you have permission to use `sudo` and are not running a dry-run, run:
```bash
$ sudo ./create-users.py < create-users.input
```

### Confirmation of the Creation of New Users
To check if the users were created and added to the right groups, you can run 2 commands.

To check user info:
```bash
$ grep <name of user> /etc/passwd
```

To check user groups:
```bash
$ grep <name of user> /etc/group
```

### Running in Dry-Run Mode
