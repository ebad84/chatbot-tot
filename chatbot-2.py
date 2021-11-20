database = {
    "سلام":"سلام خوبی؟",
    "چه خبر":"سلامتی ممنون. از تو چه خبر؟",
    "یه جک بگو":"یه مرده میخوره به نرده برمیگرده میگه چقد سرده :|"
}

def clear(text):
    for i in r"!@#$%^&*)(,./\|-_=+؟.,><":
        text = text.replace(i,"")
    return text


def sim1(text1,text2):
    text1 = clear(text1).split()
    text2 = clear(text2).split()
    sim_words = []
    number = len(text1) + len(text2)

    for i in text1:
        if i in text2:
            if i not in sim_words:
                sim_words.append(i)
    for i in text2:
        if i in text1:
            if i not in sim_words:
                sim_words.append(i)
    
    per = (len(sim_words)/number) * 100
    return per

def sim2(text1,text2):
    text1 = clear(text1).split()
    text2 = clear(text2).split()
    sim_words = []
    number = 0
    notsim_words = []

    for i in text1:
        if i in text2:
            if i not in sim_words:
                sim_words.append(i)
        else:
            if i not in notsim_words:
                notsim_words.append(i)
    for i in text2:
        if i in text1:
            if i not in sim_words:
                sim_words.append(i)
        else:
            if i not in notsim_words:
                notsim_words.append(i)

    number = len(notsim_words)
    if number == 0:
        number = 1
    per = (len(sim_words)/number) * 100
    return per

def similarity(text1,text2):
    return (sim1(text1,text2)+sim2(text1,text2))/2


def find_ans(q):
    for i in database:
        ans = database[i]
        if similarity(q,i) >= 50:
            return [True,ans]
    return [False,None]

print("say something")
while True:
    inp = clear(input(">"))
    if inp == "خروج":
        break
    else:
        # if inp in database:
        #     print(database[inp])
        res = find_ans(inp)
        if res[0]:
            print(res[1])
        else:
            print("نفهمیدم :|")
