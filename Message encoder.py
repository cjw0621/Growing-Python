def make_encoded(user_input):

    user_input = user_input.replace("a", "~")
    user_input = user_input.replace("A", "~")
    user_input = user_input.replace("b", "@")
    user_input = user_input.replace("B", "@")
    user_input = user_input.replace("c", "#")
    user_input = user_input.replace("C", "#")
    user_input = user_input.replace("d", "$")
    user_input = user_input.replace("D", "$")
    user_input = user_input.replace("e", "%")
    user_input = user_input.replace("E", "%")
    user_input = user_input.replace("f", "^")
    user_input = user_input.replace("F", "^")
    user_input = user_input.replace("g", "&")
    user_input = user_input.replace("G", "&")
    user_input = user_input.replace("h", "*")
    user_input = user_input.replace("H", "*")
    user_input = user_input.replace("i", "(")
    user_input = user_input.replace("I", "(")
    user_input = user_input.replace("j", ")")
    user_input = user_input.replace("J", ")")
    user_input = user_input.replace("k", "-")
    user_input = user_input.replace("K", "-")
    user_input = user_input.replace("l", "=")
    user_input = user_input.replace("L", "=")
    user_input = user_input.replace("m", "+")
    user_input = user_input.replace("M", "+")
    user_input = user_input.replace("n", "`")
    user_input = user_input.replace("N", "`")
    user_input = user_input.replace("o", ",")
    user_input = user_input.replace("O", ",")
    user_input = user_input.replace("p", "<")
    user_input = user_input.replace("P", "<")
    user_input = user_input.replace("q", ".")
    user_input = user_input.replace("Q", ".")
    user_input = user_input.replace("r", ">")
    user_input = user_input.replace("R", ">")
    user_input = user_input.replace("s", "/")
    user_input = user_input.replace("S", "/")
    user_input = user_input.replace("t", "?")
    user_input = user_input.replace("T", "?")
    user_input = user_input.replace("u", "[")
    user_input = user_input.replace("U", "[")
    user_input = user_input.replace("v", "]")
    user_input = user_input.replace("V", "]")
    user_input = user_input.replace("w", "|")
    user_input = user_input.replace("W", "|")
    user_input = user_input.replace("x", "}")
    user_input = user_input.replace("X", "}")
    user_input = user_input.replace("y", "{")
    user_input = user_input.replace("Y", "{")
    user_input = user_input.replace("z", ";")
    user_input = user_input.replace("Z", ";")

    return user_input

def make_decoded(user_input):
    user_input = user_input.replace("~", "a")
    user_input = user_input.replace("~", "A")
    user_input = user_input.replace("@", "b")
    user_input = user_input.replace("@", "B")
    user_input = user_input.replace("#", "c")
    user_input = user_input.replace("#", "C")
    user_input = user_input.replace("$", "d")
    user_input = user_input.replace("$", "D")
    user_input = user_input.replace("%", "e")
    user_input = user_input.replace("%", "E")
    user_input = user_input.replace("^", "f")
    user_input = user_input.replace("^", "F")
    user_input = user_input.replace("&", "g")
    user_input = user_input.replace("&", "G")
    user_input = user_input.replace("*", "h")
    user_input = user_input.replace("*", "H")
    user_input = user_input.replace("(", "i")
    user_input = user_input.replace("(", "I")
    user_input = user_input.replace(")", "j")
    user_input = user_input.replace(")", "J")
    user_input = user_input.replace("-", "k")
    user_input = user_input.replace("-", "K")
    user_input = user_input.replace("=", "l")
    user_input = user_input.replace("=", "L")
    user_input = user_input.replace("+", "m")
    user_input = user_input.replace("+", "M")
    user_input = user_input.replace("`", "n")
    user_input = user_input.replace("`", "N")
    user_input = user_input.replace(",", "o")
    user_input = user_input.replace(",", "O")
    user_input = user_input.replace("<", "p")
    user_input = user_input.replace("<", "P")
    user_input = user_input.replace(".", "q")
    user_input = user_input.replace(".", "Q")
    user_input = user_input.replace(">", "r")
    user_input = user_input.replace(">", "R")
    user_input = user_input.replace("/", "s")
    user_input = user_input.replace("/", "S")
    user_input = user_input.replace("?", "t")
    user_input = user_input.replace("?", "T")
    user_input = user_input.replace("[", "u")
    user_input = user_input.replace("[", "U")
    user_input = user_input.replace("]", "v")
    user_input = user_input.replace("]", "V")
    user_input = user_input.replace("|", "w")
    user_input = user_input.replace("|", "W")
    user_input = user_input.replace("}", "x")
    user_input = user_input.replace("}", "X")
    user_input = user_input.replace("{", "y")
    user_input = user_input.replace("{", "Y")
    user_input = user_input.replace(";", "z")
    user_input = user_input.replace(";", "Z")

    return user_input

loop = False

while loop == False:

    y_n = input("Do you have a message you would like to decode? -> ")
    print(y_n)

    if y_n == "y" or y_n == "Y" or y_n == "yes" or y_n == "Yes" or y_n == "YES":
        user_input = input("Whats your encoded message? -> ")
        print(make_decoded(user_input))
    elif y_n == "n" or y_n == "N" or y_n == "no" or y_n == "No" or y_n == "NO":
        user_input = input("What would you like encoded? -> ")
        print(make_encoded(user_input))
    else:
        print("Your response is invalid, please to ensure youre only using letters.")
        user_input = y_n
        print(user_input)

loop == False