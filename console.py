#!/usr/bin/python3
"""
A module to define the console class
which will be the frontend of the project
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A Class that represent the Frontend of project
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program when EOF is encountered."""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """
        Overrides emptyline() so when an empty command
        is entered it does nothing.
        :return: No return.
        """
        pass

    def do_create(self, line):
        """Create command to create a new object."""
        if line in storage.classes():
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)
        elif line == "" or line is None:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show command to show data of an object."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                if args[1] == "" or len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
