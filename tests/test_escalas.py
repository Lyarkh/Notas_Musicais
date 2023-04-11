"""
AAA - 3A - A3

Arrange - Act - Assets!
Arrumar - Agir - Garantir!
"""
from pytest import raises

from notas_musicais.escalas import NOTAS, escala


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
