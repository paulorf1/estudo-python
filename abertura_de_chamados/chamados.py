from storage import carregar_chamados, salvar_chamados


def listar_chamados():
    chamados = carregar_chamados()

    if not chamados:
        print("\nNenhum chamado aberto.\n")
        return

    print("\n=== CHAMADOS ===")
    for i, ch in enumerate(chamados, start=1):
        status = "Aberto" if ch["aberto"] else "Fechado"
        print(f"{i}. {ch['titulo']} | {status}")
        print(f"   {ch['descricao']}")
    print()


def abrir_chamado(titulo, descricao):
    chamados = carregar_chamados()
    chamados.append(
        {"titulo": titulo, "descricao": descricao, "aberto": True}
    )
    salvar_chamados(chamados)
    print("\nChamado aberto com sucesso!\n")


def fechar_chamado(indice):
    chamados = carregar_chamados()

    if indice < 1 or indice > len(chamados):
        print("\nChamado inválido.\n")
        return

    chamados[indice - 1]["aberto"] = False
    salvar_chamados(chamados)
    print("\nChamado fechado!\n")
