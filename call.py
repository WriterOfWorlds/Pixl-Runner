page = 0
memory = {}

def call(command, page, memory):
    if command == "black":
        try:
            f = open("page/" + str(page) + ".txt", "xt")
            memory[page] = page
            return memory
        except:
            x = 0
            page += 1
            while x == 0:
                try:
                    f = open("page/" + str(page) + ".txt", "xt")
                    memory[page] = page
                    return memory
                except:
                    page += 1