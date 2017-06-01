"""
Usage:
    drabot create_room <room_type> <room_name>...
    drabot add_person <person_name> (<fellow> | <staff>) [<accommodation>]
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
    -o, --filename save to file name
    -db --sqlite_database
    
"""
import sys
import cmd
from docopt import docopt, DocoptExit

sys.path.append('drabot')

from _room import Room
from office import Office
from living_space import LivingSpace 


room = Room()
office = Office()
"""
from drabot.person import Person
from drabot.living_space import LivingSpace

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


class Runner(cmd.Cmd):
    intro = """\
    Welcome to drabot command line guide
    Drabot randomly allocates rooms to to andelans.
    Type help for a list of commands.
    """
    prompt = '(drabot) '
    
    @docopt_cmd
    def do_create_room(self, arg):
        """
        Usage: create_room <room_type> <room_name>...
        
        options:
            -<room_type> : office|living_space
            -<room_name> : room name to create
        """
        room_names = arg['<room_name>']
        room_type = arg['<room_type>']
        room_types = ('office', 'living_space')
        if room_type not in room_types:
            print("""room_type should be office or living_space, not {},
            read help create_room""".format(room_type))
        else:
            for room_name in room_names:
                room.create_room(room_type, room_name)
       
    @docopt_cmd    
    def do_add_person(self, arg):
        """
    Usage: add_person <person_name> (<fellow> | <staff>) [ <accommodation> ]
        """
        person_name = arg['<person_name>']
        position = arg['<fellow>']
        accommodation = 'Y' if ('<accommodation>' in arg) and arg['<accommodation>']=='Y' else 'N'
        print(room.add_person(person_name, position, accommodation))
   
        
    @docopt_cmd    
    def do_print_room(self, arg):
        "Usage: print_room <room_name>"
        room_name = arg['<room_name>']
        if room_name in room.office_room_names:
            room.get_office_allocation(room_name)
            if room_name in room.living_room_names:
                room.get_living_space_allocation(room_name)
        elif room_name in room.living_room_names:
            room.get_living_space_allocation(room_name)
        else:
            return 'Room name {} does not exist in the Dojo'.format(room_name)
       
    @docopt_cmd    
    def do_print_allocations(self, arg):
        "Usage: print_allocations [-o=filename]"
        room.print_allocations()
        
        #print("This Feature is still under development")
        
    @docopt_cmd    
    def do_print_unallocated(self, arg):
        "Usage: print_unallocated [-o=filename]"
        print("No unallocated people. Everyone that joins Andela is allocated a random office")
        
    @docopt_cmd    
    def do_reallocate_person(self, arg):
        "Usage: reallocate_person <person_identifier> <room_name>"
        print("This Feature is still under development")
       
       
    @docopt_cmd    
    def do_load_people(self, arg):
        "Usage: load_people"
        print("This Feature is still under development")
        
    @docopt_cmd    
    def do_save_state(self, arg):
        "Usage: save_state [--db=sqlite_database]"
        print("This Feature is still under development")
       
    @docopt_cmd    
    def do_load_state(self, arg):
        "Usage: load_state <sqlite_database>"
        print("This Feature is still under development")
       
       
        
        
        
opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Runner().cmdloop()

print(opt)
