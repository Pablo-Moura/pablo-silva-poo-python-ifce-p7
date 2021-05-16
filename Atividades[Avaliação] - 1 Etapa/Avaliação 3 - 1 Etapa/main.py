"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.
"""
from produto import Produto
from cliente import Cliente
from notafiscal import NotaFiscal
from itemnotafiscal import ItemNotaFiscal
from tipocliente import TipoCliente


def main():
    cli = Cliente(1, "Pablo Silva", 100, "200.100.345-35", 1)

    p1 = Produto(1, 100, "Feijão Tropeiro", 6.5)
    it1 = ItemNotaFiscal(1, 1, 1, p1)

    p2 = Produto(2, 200, "Feijao Preto", 6.5)
    it2 = ItemNotaFiscal(2, 2, 2, p2)

    p3 = Produto(3, 300, "Bolacha Fortaleza", 2.5)
    it3 = ItemNotaFiscal(3, 3, 1, p3)

    p4 = Produto(3, 300, "Bolacha Maria", 3)
    it4 = ItemNotaFiscal(4, 4, 2, p4)

    nf = NotaFiscal(1, 100, cli)

    nf.adicionarItem(it1)

    nf.adicionarItem(it2)

    nf.adicionarItem(it3)

    nf.adicionarItem(it4)

    nf.calcularNotaFiscal()

    nf.imprimirNotaFiscal()


if __name__ == '__main__':
    main()