#format to string
def f(txt, a = None, b = None, c = None):
    style_font = { "normal" : 0, "bold" : 1, "light" : 2, "italic" : 3, "underline" : 4, "inverse" : 5, "hide" : 6, "strikeout" : 7 }
    color_font = { "black" : 30, "red" : 31, "green" : 32, "yellow" : 33, "blue" : 34, "purple" : 35, "cyan" : 36, "white" : 37 }
    color_background = { "BLACK" : 40, "RED" : 41, "GREEN" : 42, "YELLOW" : 43, "BLUE" : 44, "PURPLE" : 45, "CYAN" : 46, "WHITE" : 47 }
    
    clean = '\033[0;00m'

    if a == None and b == None and c == None: 
        out = (f"\033[0;37m{txt}{clean}")

    elif a != None and b == None and c == None: 
        if a in style_font.keys(): v1 = str(style_font[a])+';37'
        elif a in color_font.keys(): v1 = '0;'+str(color_font[a])
        elif a in color_background.keys(): v1 = '0;'+str(color_background[a])
        
        out = (f"\033[{v1}m{txt}{clean}")
        
    elif a != None and b != None and c == None:
        if a in style_font.keys(): v1 = style_font[a]
        elif a in color_font.keys(): v1 = color_font[a]
        elif a in color_background.keys(): v1 = color_background[a]

        if b in style_font.keys(): v2 = style_font[b]
        elif b in color_font.keys(): v2 = color_font[b]
        elif b in color_background.keys(): v2 = color_background[b]

        out = (f"\033[{v1};{v2}m{txt}{clean}")

    elif a != None and b != None and c != None:
        if a in style_font.keys(): v1 = style_font[a]
        elif a in color_font.keys(): v1 = color_font[a]
        elif a in color_background.keys(): v1 = color_background[a]

        if b in style_font.keys(): v2 = style_font[b]
        elif b in color_font.keys(): v2 = color_font[b]
        elif b in color_background.keys(): v2 = color_background[b]

        if c in style_font.keys(): v3 = style_font[c]
        elif c in color_font.keys(): v3 = color_font[c]
        elif c in color_background.keys(): v3 = color_background[c]

        out = (f"\033[{v1};{v2};{v3}m{txt}{clean}")


    return out

# print testing - - - - -
# print(f('hola !!!'))
# print(f('hola','RED'))
# print(f('hola','italic','GREEN'))
# print(f('hola','cyan','light'))
# print(f('hola','red', '',''))
# print(f('hola','', 'bold','RED'))





def jumbo(txt,size=1):
    l = len(txt)

    block = ""

    if size == 1:
        block += "\n------"+("-"*l)
        block += "\n|"+("  ")+txt+("  ")+"|"
        block += "\n------"+("-"*l)
    elif size == 2:
        block += "\n------"+("-"*l)
        block += "\n|"+("  ")+(" "*l)+("  ")+"|"
        block += "\n|"+(" "*2)+txt+(" "*2)+"|"
        block += "\n|"+("  ")+(" "*l)+("  ")+"|"
        block += "\n------"+("-"*l)
    elif size == 3:
        block += "\n------------"+("-"*l)
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n|"+(" "*5)+txt+(" "*5)+"|"
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n------------"+("-"*l)
    
    
    
    
    return block




