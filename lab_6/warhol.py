import graphicsPlus as graphics
'''
Warhol art generator.
Creates a warhol art like image in a 2 by 2 grid pattern
'''
import sys
import filter
import show

'''
Accepts a ppm image name and then generates the graphic using filters
from filter.py. 

Prints a usage message if the incorrect number of args are given
'''

#Error message and guidance for wrong input
msg = "Guide:\ninput format:\n\t'python warhol.py maine1.ppm 3'\n\t\tor\n\t'python warhol.py maine1.ppm 3 maine1.ppm'\n"
msg += "\targ1 is 'warhol.py'\n"
msg += "\targ2 is the first image filename\n"
msg += "\targ3 is the number of images in a row\n"
msg += "\targ4(optional) is is the second image filename\n"


#main function to call main in show, check arguments number and handle invalid input
def main(argv):
   try:
      if len(sys.argv) == 3 or len(sys.argv) == 4:
         show.main(sys.argv)
      else: 
         print (msg)
   except BaseException:
      print (msg)
    
#conditional call to pass sys.argv list to the main function
if __name__ == "__main__":
	main(sys.argv)
