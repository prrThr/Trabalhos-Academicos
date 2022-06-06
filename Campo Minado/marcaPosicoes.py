
def marcaPosicao(m, comp, l, c, t, contagem):
    cont = 0

    if comp[l][c] == 0:
        m[l][c] = '-'
        cont = cont + 1
        if l > 0 and c > 0 and l < t-1 and c < t-1:
            if comp[l-1][c] == 0:
                m[l-1][c] = '-'
                cont = cont + 1
            if comp[l-1][c-1] == 0:
                m[l-1][c-1] = '-'
                cont = cont + 1
            if comp[l-1][c+1] == 0:
                m[l-1][c+1] = '-'
                cont = cont + 1
            if comp[l][c-1] == 0:
                m[l][c-1] = '-'
                cont = cont + 1
            if comp[l][c+1] == 0:
                m[l][c+1] = '-'
                cont = cont + 1
            if comp[l+1][c] == 0:
                m[l+1][c] = '-'
                cont = cont + 1
            if comp[l+1][c-1] == 0:
                m[l+1][c-1] = '-'
                cont = cont + 1
            if comp[l+1][c+1] == 0:
                m[l+1][c+1] = '-'
                cont = cont + 1

        elif l == 0 and c > 0 and c < t-1:
            if comp[l][c-1] == 0:
                m[l][c-1] = '-'
                cont = cont + 1
            if comp[l][c+1] == 0:
                m[l][c+1] = '-'
                cont = cont + 1
            if comp[l+1][c] == 0:
                m[l+1][c] = '-'
                cont = cont + 1
            if comp[l+1][c-1] == 0:
                m[l+1][c-1] = '-'
                cont = cont + 1
            if comp[l+1][c+1] == 0:
                m[l+1][c+1] = '-'
                cont = cont + 1

        elif l == t-1 and c > 0 and c < t-1:
            if comp[l-1][c] == 0:
                m[l-1][c] = '-'
                cont = cont + 1
            if comp[l-1][c-1] == 0:
                m[l-1][c-1] = '-'
                cont = cont + 1
            if comp[l-1][c+1] == 0:
                m[l-1][c+1] = '-'
                cont = cont + 1
            if comp[l][c-1] == 0:
                m[l][c-1] = '-'
                cont = cont + 1
            if comp[l][c+1] == 0:
                m[l][c+1] = '-'
                cont = cont + 1

        elif l == 0 and c == 0:
            if comp[l][c+1] == 0:
                m[l][c+1] = '-'
                cont = cont + 1
            if comp[l+1][c] == 0:
                m[l+1][c] = '-'
                cont = cont + 1
            if comp[l+1][c+1] == 0:
                m[l+1][c+1] = '-'
                cont = cont + 1

        elif l == 0 and c == t-1:
            if comp[l][c-1] == 0:
                m[l][c-1] = '-'
                cont = cont + 1
            if comp[l+1][c] == 0:
                m[l+1][c] = '-'
                cont = cont + 1
            if comp[l+1][c-1] == 0:
                m[l+1][c-1] = '-'
                cont = cont + 1

        elif l == t-1 and c == t-1:
            if comp[l-1][c] == 0:
                m[l-1][c] = '-'
                cont = cont + 1
            if comp[l-1][c-1] == 0:
                m[l-1][c-1] = '-'
                cont = cont + 1
            if comp[l][c-1] == 0:
                m[l][c-1] = '-'
                cont = cont + 1

        elif l == t-1 and c == 0:
            if comp[l-1][c] == 0:
                m[l-1][c] = '-'
                cont = cont + 1
            if comp[l-1][c+1] == 0:
                m[l-1][c+1] = '-'
                cont = cont + 1
            if comp[l][c+1] == 0:
                m[l][c+1] = '-'
                cont = cont + 1

        elif l > 0 and l < t-1 and c == 0:
            if comp[l-1][c] == 0:
                m[l-1][c] = '-'
                cont = cont + 1
            if comp[l-1][c+1] == 0:
                m[l-1][c+1] = '-'
                cont = cont + 1
            if comp[l][c+1] == 0:
                m[l][c+1] = '-'
                cont = cont + 1
            if comp[l+1][c] == 0:
                m[l+1][c] = '-'
                cont = cont + 1
            if comp[l+1][c+1] == 0:
                m[l+1][c+1] = '-'
                cont = cont + 1

        elif l > 0 and l < t-1 and c == t-1:
            if comp[l-1][c] == 0:
                m[l-1][c] = '-'
                cont = cont + 1
            if comp[l-1][c-1] == 0:
                m[l-1][c-1] = '-'
                cont = cont + 1
            if comp[l][c-1] == 0:
                m[l][c-1] = '-'
                cont = cont + 1
            if comp[l+1][c] == 0:
                m[l+1][c] = '-'
                cont = cont + 1
            if comp[l+1][c-1] == 0:
                m[l+1][c-1] = '-'
                cont = cont + 1
    else:
        m[l][c] = comp[l][c]
        cont = cont + 1

    if contagem == True:
        return cont
    else:
        return m
