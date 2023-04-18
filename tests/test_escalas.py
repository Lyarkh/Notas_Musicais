"""
AAA - 3A - A3

Arrange - Act - Assets!
Arrumar - Agir - Garantir!
"""
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_uma_error_dizendo_que_a_nota_nao_existe():
    tonalidade = 'maior'
    tonica = 'X'

    mensagem_de_error = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_error == error.value.args[0]


def test_deve_retornar_uma_error_dizendo_que_a_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_de_error = f'Essa escala não existe ou não foi implementada. Tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_error == error.value.args[0]


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado
