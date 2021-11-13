#!/usr/bin/python3
"""
Program console.py
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand contains the entry point of the command interpreter.
    """
    prompt = '(hbnb)'

    def do_EOF(self, line):
        "EOF command to exit the program"
        print()
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """
        An empty line + ENTER don't execute anything.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()