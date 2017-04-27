"""
Usage:
    drabot create_room <room_type> <room_name>...
    drabot add_person <person_name> <fellow|staff> [-a=accommodation]
    drabot print_room <room_name>
    drabot print_allocations [-o=filename]
    drabot print_unallocated [-o=filename]
    drabot reallocate_person <person_identifier> <room_name>
    drabot load_people
    drabot save_state [--db=sqlite_database]
    drabot load_state <sqlite_database>
    drabot (-i | --interactive)
    drabot (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    -a --accommodation  wants accomodattion [default: N]
    -o, --filename save to file name
    -db --sqlite_database
    
"""
import sys
import cmd
from docopt import docopt, DocoptExit
"""
from drabot._room import Room
from drabot.person import Person
from drabot.living_space import LivingSpace
from drabot.office import Office
from drabot.staff import Staff
from drabot.fellow import Fellow
from drabot._dojo import Dojo
"""
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


#room = Room()

class Runner(cmd.Cmd):
    intro = """\
    Welcome to drabot command line guide
    Drabot allocates rooms to to andelans.
    Type help for a list of commands.
    """
    prompt = '(drabot) '
    
    """
    go into docopt mode
    accept commands
    print back output. 
    """ 
    @docopt_cmd
    def do_create_room(self, room_type, *room_name):
        "create_room <room_type> <room_name>..."
        return room.create_room(room_type, *room_name)
    @docopt_cmd    
    def do_add_person(self, room_type, room_name):
        print("This Feature is still under development")
        
        
        
opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Runner().cmdloop()

print(opt)
