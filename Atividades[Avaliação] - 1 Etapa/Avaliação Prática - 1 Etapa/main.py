from folha_pagamento import FolhaPagamento
from colaborador import Colaborador
from movimento_folha import MovimentoFolha
from tipomovimento import TipoMovimento

def main():

    fp = FolhaPagamento(9, 2019, 0, 0)

    CL01 = Colaborador("100", "Manoel Claudino", "Av 13 de Maio 2081", "88671020",
                       "Benfica", "60020-060", "124543556-89", 4500.00)
    CL02 = Colaborador("200", "Carmelina da Silva", "Avenida dos Expedicionários 1200",
                       "3035-1280", "Aeroporto", "60530-020", "301789435-54",
                       2500.00)
    CL03 = Colaborador("300", "Gurmelina Castro Saraiva", "Av João Pessoa 1020",
                       "3235-1089", "Damas", "60330-090", "350245632-76", 3000.00)

    MF01 = MovimentoFolha(CL01, "Salario", 4500.00, TipoMovimento.P)
    MF02 = MovimentoFolha(CL01, "Plano Saúde", 1000.00, TipoMovimento.P)
    MF03 = MovimentoFolha(CL01, "Pensão", 600.00, TipoMovimento.D)
    MF04 = MovimentoFolha(CL02, "Salario", 2500.00, TipoMovimento.P)
    MF05 = MovimentoFolha(CL02, "Gratificação", 1000.00, TipoMovimento.P)
    MF06 = MovimentoFolha(CL02, "Faltas", 600.00, TipoMovimento.D)
    MF07 = MovimentoFolha(CL03, "Salario", 4500.00, TipoMovimento.P)
    MF08 = MovimentoFolha(CL03, "Plano Saúde", 1000.00, TipoMovimento.P)
    MF09 = MovimentoFolha(CL03, "Pensão", 600.00, TipoMovimento.D)

    fp.set_colaborador(CL01)
    fp.set_colaborador(CL02)
    fp.set_colaborador(CL03)

    movimentos = [MF01, MF02, MF03, MF04, MF05, MF06, MF07, MF08, MF09]

    for x in movimentos:
        fp.inserir_movimento_fp(x)

    for m in range(len(movimentos)):
        if m < 3:
            CL01.inserir_movimentos_colab(movimentos[m])
        elif m < 6:
            CL02.inserir_movimentos_colab(movimentos[m])
        else:
            CL03.inserir_movimentos_colab(movimentos[m])


    CL01.calcular_salario()
    CL02.calcular_salario()
    CL03.calcular_salario()

    fp.calcular_folha()


if __name__ == '__main__':
    main()