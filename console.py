#!/usr/bin/python3
"""Console module."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter class."""

    prompt = '(hbnb) '
    classes_dict = {"BaseModel": BaseModel, "State": State, "State": State,
                    "City": City, "Amenity": Amenity,
                    "Place": Place, "Review": Review, "User": User}

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Empty line."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it"""
        if line == "":
            print("** class name missing **")
            return
        else:
            try:
                myclass = eval(line + "()")
                myclass.save()
                print(myclass.id)
            except Exception as e:
                print("** class doesn't exist **")
                return

    def do_show(self, line):
        """Print the string representation of an instance
        based on the class name and id."""
        line_vactor = line.split()
        if line_vactor == []:
            print("** class name missing **")
            return
        elif self.classes_dict.get(line_vactor[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(line_vactor) != 2:
            print("** instance id missing **")
            return
        objects_class = storage.all()
        key = line_vactor[0] + "." + line_vactor[1]
        if key in objects_class.keys():
            print(objects_class[key].__str__())
        else:
            print("** no instance found **")
            return

    def do_destroy(self, line):
        """Delete an instance based on the class name and id."""
        line_vactor = line.split()
        if line_vactor == []:
            print("** class name missing **")
            return
        elif self.classes_dict.get(line_vactor[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(line_vactor) != 2:
            print("** instance id missing **")
            return

        objects_class = storage.all()
        key = line_vactor[0] + "." + line_vactor[1]
        if key in objects_class.keys():
            objects_class.pop(key)
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, line):
        """Print all string representation of all instances"""
        line_vactor = line.split()

        objects_string_representation = []
        class_to_represent = None
        if line_vactor != []:
            class_to_represent = line_vactor[0]
            if class_to_represent not in self.classes_dict:
                print("** class doesn't exist **")
                return

        objects_class = storage.all()
        for obj in objects_class.values():
            if class_to_represent is None:
                objects_string_representation.append(obj.__str__())
            elif obj.__class__.__name__ == class_to_represent:
                objects_string_representation.append(obj.__str__())

        print(objects_string_representation)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        line_vector = line.split()
        vector_len = len(line_vector)
        if line_vector == []:
            print("** class name missing **")
            return
        elif line_vector[0] not in self.classes_dict:
            print("** class doesn't exist **")
            return
        elif vector_len < 2:
            print("** instance id missing **")
            return
        else:
            objects_class = storage.all()
            key = line_vector[0] + "." + line_vector[1]

            if key not in objects_class.keys():
                print("** no instance found **")
                return
            elif vector_len < 3:
                print("** attribute name missing **")
                return
            elif vector_len < 4:
                print("** value missing **")
                return
            else:
                setattr(objects_class[key],
                        line_vector[2],  eval(line_vector[3]))
                objects_class[key].save()

    def do_count(self, line):
        """Display count of instances specified"""
        if line in HBNBCommand.classes_dict:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Handle Cmd methods."""
        line_vector = line.split('.')
        class_argument = line_vector[0]

        if line_vector == []:
            print("*** Unknown syntax: {}".format(line))
            return

        try:
            line_vector = line_vector[1].split('(')
            command = line_vector[0]

            if command == 'all':  # <class name>.all
                HBNBCommand.do_all(self, class_argument)  # all BaseModel

            elif command == 'count':  # <class name>.count()
                HBNBCommand.do_count(self, class_argument)

            elif command == 'show':  # <class name>.show(<id>)
                line_vector = line_vector[1].split(')')
                id_argument = line_vector[0].strip("'\"")
                argument = class_argument + ' ' + id_argument
                HBNBCommand.do_show(self, argument)  # show BaseModel 123

            elif command == 'destroy':  # <class name>.destroy(<id>)
                line_vector = line_vector[1].split(')')
                id_argument = line_vector[0].strip("'\"")
                argument = class_argument + ' ' + id_argument
                HBNBCommand.do_destroy(self, argument)  # destroy BaseModel 122

            elif command == 'update':
                line_vector = line_vector[1].split(',')
                id_argument = line_vector[0].strip("'\"")
                name_argument = line_vector[1].strip(',')
                if "{" not in line:
                    value_argument = line_vector[2]
                    name_argument = name_argument.strip(" '\"")
                    value_argument = value_argument.strip(' )')
                if "{" in line:

                    b1 = line.index('{')
                    b2 = line.index('}')
                    value_dict = line[b1 + 1: b2].replace(" ", "")
                    value_dict_list = value_dict.split(",")

                    for s in value_dict_list:
                        s = s.split(":")
                        argument = class_argument + ' ' + id_argument + \
                            ' ' + s[0][1:-1] + ' ' + s[1]
                        HBNBCommand.do_update(self, argument)
                        key = class_argument + '.' + id_argument
                        if key not in storage.all().keys():
                            return
                else:
                    # If eval fails, use the attribute and value pattern
                    argument = class_argument + ' ' + id_argument + \
                        ' ' + name_argument + ' ' + value_argument
                    HBNBCommand.do_update(self, argument)

            else:
                print("*** Unknown syntax: {}".format(line))
                return

        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
