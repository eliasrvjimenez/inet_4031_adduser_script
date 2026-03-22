#!/usr/bin/python3

# INET4031
# Elias Vera-Jimenez (veraj002)
# 2026-03-22
# 2026-03-22

#os import for running os operations and command - i.e. used for running adduser to add users to system.
#re import for using the regular expression match function to find the # in the input file in order to skip the line if needed
#sys import for accessing standard in for input of users being created by script.
import os
import re
import sys

def main():
    for line in sys.stdin:

        # match variable is a boolean meant to check whether or not a "#" is present
        # in the current line. used for later if statement logic.
        match = re.match("^#",line)

        # splitting line input into individual fields for use in system command to
        # create a user.
        fields = line.strip().split(':')

        # conditional to check if the current line has a # and/or if the line has 5 fields of input. if either are true, the program skips the current line of input and moves on to the next. # check is to see if an input line has been indicated to be skipped by the input creator, and the 5 fields of input check is to ensure that the proper number of fields is being passed for user creation.
        if match or len(fields) != 5:
            continue

        # Splitting the input from fields 1 and 2 into username and password, to prep for passage into adduser command.
        username = fields[0]
        password = fields[1]
        
        # Passing fields 3 and 4 as one input for first and last name passage into adduser.
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Passing field 5 into a split function in case of a user being added to several groups.
        groups = fields[4].split(',')

        # Printing for good visibility when running the script to see which user is being worked on at the current point in time - good for debugging purposes.
        print("==> Creating account for %s..." % (username))
        
        # Creating command that will be used to create current user with passed fields. 
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # Printing current command being run, which is the command to run adduser with the current user fields, good for debugging visibility.
        print(cmd)
        # runnning command currently in variable cmd, which is the adduser command used to add the current user's fields.
        os.system(cmd)

        # Printing for good visibility to indicate that the current user is at the part of the process where they are assigned a password, useful in debugging. 
        print("==> Setting the password for %s..." % (username))
    
        # Creating command to add user password to passwd file in /usr/bin, ensuring that the correct password is associated with the correct username.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # Printing current command being run for debugging visibility.
        print(cmd)

        # Running the current command, which is the command to echo the password associated with the current user into the passwd file.
        os.system(cmd)
        for group in groups:
            # conditional to check if groups field is filled in with a "-". if not, the groups will be properly assigned to the user. if it is, the groups command will be skipped.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()

