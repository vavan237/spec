



def add_to_txt(lst, dest_file="E:/debts.txt"):
    with open(dest_file, 'w') as file:
        for i in lst:
            file.write(str(i)+'\n')


def get_from_txt(dest_file):
    lst1 = []
    with open(dest_file, 'r', encoding='UTF-8') as file:
        for row in file:
            lst1.append(row.replace('\n', '').split(','))
    return lst1


def reed_ls_txt(destfile):
    res = []
    res2 = []
    with open(destfile, 'r') as file:
        for row in file:
            res.append(row.replace('\n', '').split(','))
        for i in res:
            for j in i:
                res2.append(j.split(';'))
    return res2


