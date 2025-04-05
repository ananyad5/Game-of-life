from blessed import Terminal


term = Terminal()


with term.location(0, term.height-1):
    print("this is"+ term.underline("underlined"))