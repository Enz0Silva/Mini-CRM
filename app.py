from model import model_lead
import control


# =========================
# CREATE
# =========================

def add_lead():
    name = input("Nome: ").strip()
    email = input("Email: ").strip()
    company = input("Empresa: ").strip()
    stage = input("Etapa de venda: ").strip()

    if not name or not email or not company or "@" not in email:
        print("Nome ou e-mail inválido")
        return

    lead = model_lead(
        name,
        email,
        company,
        stage
    )

    control.create_lead(lead)

    print("Lead adicionado com sucesso!")


# =========================
# READ
# =========================

def lista_lead():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead ainda")
        return

    print(
        f"{'#':<3} | "
        f"{'Nome':<15} | "
        f"{'E-mail':<25} | "
        f"{'Empresa':<15} | "
        f"{'Etapa':<15}"
    )

    print("-" * 85)

    for i, lead in enumerate(leads):
        print(
            f"{i:02d}  | "
            f"{lead['name']:<15} | "
            f"{lead['email']:<25} | "
            f"{lead['company']:<15} | "
            f"{lead['stage']:<15}"
        )


# =========================
# SEARCH
# =========================

def search_leads():
    query = input("Buscar por: ").strip().lower()

    if not query:
        print("Consulta vazia")
        return

    leads_finded = control.read_leads_search(query)

    if not leads_finded:
        print("Nenhum lead encontrado")
        return

    print(
        f"{'#':<3} | "
        f"{'Nome':<15} | "
        f"{'E-mail':<25} | "
        f"{'Empresa':<15} | "
        f"{'Etapa':<15}"
    )

    print("-" * 85)

    for i, lead in leads_finded:
        print(
            f"{i:02d}  | "
            f"{lead['name']:<15} | "
            f"{lead['email']:<25} | "
            f"{lead['company']:<15} | "
            f"{lead['stage']:<15}"
        )


# =========================
# UPDATE
# =========================

def edit_lead():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead ainda")
        return

    lista_lead()

    try:
        index = int(input("\nDigite o número do Lead que deseja editar: "))
    except ValueError:
        print("Digite um número válido")
        return

    if index < 0 or index >= len(leads):
        print("Lead não encontrado")
        return

    lead = leads[index]

    print("\nDeixe vazio para manter o valor atual.")

    name = input(f"Nome [{lead['name']}]: ").strip()
    email = input(f"Email [{lead['email']}]: ").strip()
    company = input(f"Empresa [{lead['company']}]: ").strip()
    stage = input(f"Etapa [{lead['stage']}]: ").strip()

    if not name:
        name = lead["name"]

    if not email:
        email = lead["email"]

    if not company:
        company = lead["company"]

    if not stage:
        stage = lead["stage"]

    if "@" not in email:
        print("E-mail inválido")
        return

    success = control.update_lead(
        index,
        name,
        email,
        company,
        stage
    )

    if success:
        print("Lead atualizado com sucesso!")
    else:
        print("Não foi possível atualizar o Lead")


# =========================
# DELETE
# =========================

def remove_lead():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead ainda")
        return

    lista_lead()

    try:
        index = int(input("\nDigite o número do Lead que deseja excluir: "))
    except ValueError:
        print("Digite um número válido")
        return

    if index < 0 or index >= len(leads):
        print("Lead não encontrado")
        return

    lead = leads[index]

    print(
        f"\nVocê está excluindo: "
        f"{lead['name']} - {lead['email']}"
    )

    confirm = input("Tem certeza? (s/n): ").strip().lower()

    if confirm != "s":
        print("Exclusão cancelada")
        return

    success = control.delete_lead(index)

    if success:
        print("Lead excluído com sucesso!")
    else:
        print("Não foi possível excluir o Lead")


# =========================
# EXPORT
# =========================

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar. Não existem leads.")
    else:
        print(f"Exportado para {path_csv}")


# =========================
# MENU
# =========================

def main():
    while True:

        print("\n===== Mini CRM de Leads =====")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[3] Buscar Lead")
        print("[4] Editar Lead")
        print("[5] Excluir Lead")
        print("[6] Exportar Leads")
        print("[0] Sair")

        opt = input("Escolha uma opção: ").strip()

        if opt == "1":
            add_lead()

        elif opt == "2":
            lista_lead()

        elif opt == "3":
            search_leads()

        elif opt == "4":
            edit_lead()

        elif opt == "5":
            remove_lead()

        elif opt == "6":
            export_leads()

        elif opt == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()