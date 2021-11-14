#!/usr/bin/python3
"""
Program console.py
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand contains the entry point of the command interpreter.
    """
    prompt = '(hbnb)'
    classes = {'BaseModel'}

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

    def do_create(self, line):
        """
        Creates a new instance of BaseModel.
        """
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            obje = storage.all()
            if key not in obje:
                print("** no instance found **")
                return
            print(obje[key])
        else:
            print('** class name missing **')

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            obje = storage.all()
            if key not in obje:
                print("** no instance found **")
                return
            del obje[key]
        else:
            print('** class name missing **')

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        my_list = []
        objs = storage.all()
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            for key in objs:
                split_key = key.split(".")
                if split_key[0] == args[0]:
                    my_list.append(str(objs[key]))
            print(my_list)
        else:
            for key in objs:
                my_list.append(str(objs[key]))
            print(my_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            objs = storage.all()
            if key not in objs:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            objs[key].__dict__[args[2].replace('"', '')] = eval(args[3])
            objs[key].save
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()