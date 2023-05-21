from rich.console import Console
from rich.table import Table
from typer import Argument, run

from notas_musicais.escalas import escala

console = Console()


def escalas(
    tonica=Argument('c', help='Tônica da escala'),
    tonalidade=Argument('maior', help='Tonalidade da escala'),
):
    table = Table()
    notas, graus = escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    console.print(table)


if __name__ == '__main__':
    run(escalas)
