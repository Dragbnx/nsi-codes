def effectif_notes(notes):
    eff = [0 for i in range(11)]
    for elm in notes:
        eff[elm] += 1
    return eff

def note_triee(eff):
    tab = []
    for i in range(len(eff)):
        for j in range(eff[i]):
            tab.append(i)
    return tab

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return bit_droit + 2 * bin_to_dec(nb_bin[:-1])
