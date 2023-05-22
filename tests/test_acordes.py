from pytest import mark

from notas_musicais.acordes import acorde


"""
Entrada:
acorde C

Esperado:
I - III - V
C    E    G

{'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
"""

@mark.parametrize(
    'nota,esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('F#', ['F#', 'A#', 'C#']),
    ]
)
def test_acorde_deve_retornar_as_notas_correspondentes(nota, esperado):
    notas, _  = acorde(nota).values()

    assert notas == esperado


def test_acorde_deve_retornar_os_graus_correspondentes():
    nota = 'C'
    esperado = ['I', 'III', 'V']

    _, graus = resultado = acorde(nota).values()

    assert resultado == esperado
