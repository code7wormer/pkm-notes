import curses
from main import create_note, open_note
import pyfiglet

text = "NOTES"
ascii_notes = pyfiglet.figlet_format(text, font="slant") # Choose from various fonts
print(ascii_notes)


def init_menu(stdscr):
    #colorstuff
    curses.start_color()
    curses.use_default_colors()

    initmenu= { "Create Note":create_note  ,  "Open Note":open_note , "Exit": lambda: None }
    funclist=list(initmenu.values())
    current_row=0#set first row as default

    curses.curs_set(0)#hide cursor

    while True:
        stdscr.erase()
        ht,wdth=stdscr.getmaxyx()
        stdscr.addstr(0, 0, ascii_notes)

        #drawing menu

        for idx,opt in enumerate(initmenu):
            x=wdth//2 - len(opt)//2
            y=ht//2-len(initmenu)//2 + idx
            if current_row==idx:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y,x,opt)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y,x,opt)

        #actually draw on-screen
        stdscr.refresh()

            # read inpit
        inputkey = stdscr.getch()
            #actions
        if inputkey==curses.KEY_DOWN and current_row<len(initmenu)-1:
            current_row+=1
        elif inputkey==curses.KEY_UP and current_row>0:
            current_row-=1
        elif inputkey==curses.KEY_ENTER or inputkey in [10,13]:
            if funclist[current_row] is funclist[-1]:  # Exit option
                break
            stdscr.clear()
            stdscr.refresh()
            curses.def_prog_mode()  # save curses state
            curses.endwin()  # leave curses mode
            funclist[current_row]()  # run your normal terminal function
            curses.reset_prog_mode()  # back to curses mode
            stdscr.refresh()
curses.wrapper(init_menu)


