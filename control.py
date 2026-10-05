from pathlib import Path
import json
import csv


DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "leads.json"


# =========================
# READ
# =========================

def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(
            DB_PATH.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError:
        return []


# =========================
# CREATE
# =========================

def create_lead(lead_dict):
    leads = read_leads()

    leads.append(lead_dict)

    DB_PATH.write_text(
        json.dumps(
            leads,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


# =========================
# UPDATE
# =========================

def update_lead(index, name, email, company, stage):
    leads = read_leads()

    if index < 0 or index >= len(leads):
        return False

    leads[index]["name"] = name
    leads[index]["email"] = email
    leads[index]["company"] = company
    leads[index]["stage"] = stage

    DB_PATH.write_text(
        json.dumps(
            leads,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )

    return True


# =========================
# DELETE
# =========================

def delete_lead(index):
    leads = read_leads()

    if index < 0 or index >= len(leads):
        return False

    leads.pop(index)

    DB_PATH.write_text(
        json.dumps(
            leads,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )

    return True


# =========================
# SEARCH
# =========================

def read_leads_search(query):
    leads = read_leads()
    result = []

    for i, lead in enumerate(leads):

        txt_lead = (
            f"{lead['name']} "
            f"{lead['email']} "
            f"{lead['company']} "
            f"{lead['stage']}"
        ).lower()

        if query in txt_lead:
            result.append((i, lead))

    return result


# =========================
# EXPORT CSV
# =========================

def export_csv():
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    if not leads:
        return None

    try:
        fieldnames = [
            "name",
            "email",
            "company",
            "stage",
            "created"
        ]

        with path_csv.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for lead in leads:
                writer.writerow(lead)

        return path_csv

    except OSError:
        return None