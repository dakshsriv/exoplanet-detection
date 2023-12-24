lst = list()
with open('./q1_q17_dr24_tce_2023.12.08_16.50.22.csv', 'r') as x:
    for l in x:
        try:
            if int(l[:8]) == 0:
                pass
            lst.append(int(l[:8]))
        except:
            pass

print(lst[:25])
