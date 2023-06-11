import sys, fileinput, os, re, random, datetime

# INSTRUCTIONS:
#   1. Flip all Cards to the Kanji_Back+Front and Back-Front Note types
#   2. Export the Japanese::Export::1 deck and Japanese::Export::2 deck to: Users/Jonathan/Git/learning_material/python
#   3. cd to the Users/Jonathan/Git/learning_material/python directory
#   4. Run: python3 wotd.py

i_adjectives = []
na_adjectives = []
suru_verbs = []
kuru_verbs = []
u_verbs = []
tsu_verbs = []
ru_verbs = []
RU_verbs = []
mu_verbs = []
bu_verbs = []
nu_verbs = []
ku_verbs = []
gu_verbs = []
su_verbs = []

# Read from Japanese__Export__1.txt file
j_exp_file = open('Japanese__Export__1.txt', 'r')
file_content = j_exp_file.read()
lines = file_content.split('\n')
j_exp_file.close()

# Store words from Japanese__Export__1.txt file
for line in lines:
    if re.search("^.+\t", line):
        word = re.findall("^.+\t", line)[0][0:-1]
        if word[-1] == 'い':
            i_adjectives.append(word)
        elif word[-3:] == '[な]':
            na_adjectives.append(word)
        elif word[-4:] == '[する]' or word == 'する':
            suru_verbs.append(word)
        elif word[-4:] == '[くる]' or word == '来る' or word[-4:] == '[来る]':
            kuru_verbs.append(word)
        elif word[-1] == 'う':
            u_verbs.append(word)
        elif word[-1] == 'つ':
            tsu_verbs.append(word)
        elif word[-1] == 'る':
            ru_verbs.append(word)
        elif word[-1] == 'む':
            mu_verbs.append(word)
        elif word[-1] == 'ぶ':
            bu_verbs.append(word)
        elif word[-1] == 'ぬ':
            nu_verbs.append(word)
        elif word[-1] == 'く':
            ku_verbs.append(word)
        elif word[-1] == 'ぐ':
            gu_verbs.append(word)
        elif word[-1] == 'す':
            su_verbs.append(word)

# Read from Japanese__Export__2.txt file
j_exp_file = open('Japanese__Export__2.txt', 'r')
file_content = j_exp_file.read()
lines = file_content.split('\n')
j_exp_file.close()

# Store words from Japanese__Export__2.txt file
for line in lines:
    if re.search("^.+\t", line):
        word = re.findall("^.+\t", line)[0][0:-1]
        RU_verbs.append(word)

# Print out the words of the day based on today's date
today = datetime.datetime.now()
if today.strftime("%d")[-1] == '0' or today.strftime("%d")[-1] == '1':
    rnd_num = random.randint(0, len(kuru_verbs) - 1)
    print(kuru_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(u_verbs) - 1)
    print(u_verbs[rnd_num])
elif today.strftime("%d")[-1] == '2':
    rnd_num = random.randint(0, len(suru_verbs) - 1)
    print(suru_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(tsu_verbs) - 1)
    print(tsu_verbs[rnd_num])
elif today.strftime("%d")[-1] == '3':
    rnd_num = random.randint(0, len(RU_verbs) - 1)
    print(RU_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(ru_verbs) - 1)
    print(ru_verbs[rnd_num])
elif today.strftime("%d")[-1] == '4':
    rnd_num = random.randint(0, len(kuru_verbs) - 1)
    print(kuru_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(mu_verbs) - 1)
    print(mu_verbs[rnd_num])
elif today.strftime("%d")[-1] == '5':
    rnd_num = random.randint(0, len(suru_verbs) - 1)
    print(suru_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(bu_verbs) - 1)
    print(bu_verbs[rnd_num])
elif today.strftime("%d")[-1] == '6':
    rnd_num = random.randint(0, len(RU_verbs) - 1)
    print(RU_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(nu_verbs) - 1)
    print(nu_verbs[rnd_num])
elif today.strftime("%d")[-1] == '7':
    rnd_num = random.randint(0, len(kuru_verbs) - 1)
    print(kuru_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(ku_verbs) - 1)
    print(ku_verbs[rnd_num])
elif today.strftime("%d")[-1] == '8':
    rnd_num = random.randint(0, len(suru_verbs) - 1)
    print(suru_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(gu_verbs) - 1)
    print(gu_verbs[rnd_num])
elif today.strftime("%d")[-1] == '9':
    rnd_num = random.randint(0, len(RU_verbs) - 1)
    print(RU_verbs[rnd_num])
    rnd_num = random.randint(0, len(i_adjectives) - 1)
    print(i_adjectives[rnd_num])
    rnd_num = random.randint(0, len(na_adjectives) - 1)
    print(na_adjectives[rnd_num])
    rnd_num = random.randint(0, len(su_verbs) - 1)
    print(su_verbs[rnd_num])