def cewek_nanya():
    print('Cewek: Kamu salah ga?')

def respon_cowok():
    return input('Cowok: ')

def cek_jawaban_cowok(jawaban):
    if jawaban.startswith('iy'):
        return True
    else:
        return False
    
def main():
    while True:
        cewek_nanya()
        jawaban_cowo = respon_cowok()

        if cek_jawaban_cowok(jawaban_cowo):
            break

if __name__ == '__cowok_selalu_salah__':
    print('')   
    main()