#!/usr/bin/python3
"""
A module to define the console class
which will be the frontend of the project
"""
import re
import cmd
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A Class that represent the Frontend of project
    """
    prompt = "(hbnb) "

    def precmd(self, line):
        """overriding function to change command line"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        command = match.group(2)
        args = match.group(3)
        match_id_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_id_and_args:
            id = match_id_and_args.group(1)
            attr_or_dict = match_id_and_args.group(2)
        else:
            id = args

        line = command + " " + classname + " " + id + " "
        return cmd.Cmd.precmd(self, line)

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
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """All command to show all instances based or not based on a class."""
        args = line.split(" ")
        objs = storage.all()
        listt = []
        if line == "":
            for key, value in objs.items():
                listt.append(str(value))
            print(listt)
        else:
            if args[0] in storage.classes():
                for key, value in objs.items():
                    if args[0] == type(value).__name__:
                        listt.append(str(value))
                print(listt)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Destroy command to delete an instance"""
        args = line.split(" ")
        if line == "" or line is None:
            print("** class name missing **")
        else:
            if args[0] in storage.classes():
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    if key in storage.all():
                        storage.all().pop(key)
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Update command to update attribute of an instance."""
        args = shlex.split(line)
        if line == "" or line is None:
            print("** class name missing **")
        else:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                if args[2] in ["id", "created_at",
                                               "updated_at"]:
                                    return
                                search = storage.attributes().items()
                                for classes_key, attr_dict in search:
                                    for attr_k, attr_type in attr_dict.items():
                                        if args[2] == attr_k:
                                            try:
                                                args[3] = attr_type(args[3])
                                            except ValueError:
                                                pass
                                setattr(storage.all()[key], args[2], args[3])
                                storage.all()[key].save()

    def do_count(self, line):
        """Count command to count no. of objs of a class."""
        args = line.split(" ")
        if line == "" or line is None:
            print("** class name missing **")
        else:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                count = 0
                for key, value in storage.all().items():
                    if args[0] == key.split('.')[0]:
                        count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
