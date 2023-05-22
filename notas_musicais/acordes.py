from notas_musicais.escalas import escala


def acorde(cifra):
    """
    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
    """
    graus = (0, 2, 4)
    notas_da_escala, _ = escala(cifra, 'maior').values()

    notas = [notas_da_escala[grau] for grau in graus]

    return {'notas': notas, 'graus': ['I', 'III', 'V']}
