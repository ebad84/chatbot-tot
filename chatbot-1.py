database = {
    "سلام":"سلام خوبی؟",
    "چه خبر":"سلامتی ممنون. از تو چه خبر؟",
    "یه جک بگو":"یه مرده میخوره به نرده برمیگرده میگه چقد سرده :|"
}

def clear(text):
    for i in r"!@#$%^&*)(,./\|-_=+؟.,><":
        text = text.replace(i,"")
    return text

print("say something")
while True:
    inp = clear(input(">"))
    if inp == "خروج":
        break
    else:
        if inp in database:
            print(database[inp])
        else:
            print("نفهمیدم :|")
