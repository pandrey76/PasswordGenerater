from random import choice


def get_rnd_psw_symbol():
    psw_source_str = "123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    return choice(psw_source_str)


if __name__ == "__main__":
    psw_len = 20
    rez_str = ""
    for i in range(0, psw_len):
        rez_str = rez_str + get_rnd_psw_symbol()
    print(rez_str)
