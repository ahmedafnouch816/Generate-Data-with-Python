import csv
import random
from faker import Faker

fake = Faker()

# Create a list of headers
headers = [
    "Fiche client",
    "Non",
    "Prénom",
    "E-mail",
    "Âge",
    "Sex",
    "CIN",
    "Activité",
    "NumCompte",
    "Décision",
    "Décideur",
    "Date decision",
    "Date ouverture",
    "Date de crédit",
    "Montant de crédit",
    "Code client",
    "Nom de chargé clientèle",
    "Solde Débit",
    "Nature de compte",
    "Mouvement",
    "Référence dossier recouvrement",
    "Cours de crédit",
    "Anc",
    "Anc debit (date)"
]

# Generate and write data to a CSV file
with open('bank_customer_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for i in range(5000):
        row = [
            i + 1,
            fake.last_name(),
            fake.first_name(),
            fake.email(),
            random.randint(18, 70),
            random.choice(['M', 'F']),
            fake.unique.random_number(digits=12),
            fake.random_element(elements=("Santé", "Commerce et Dist.", "Travaux Publics", "Transport", "Agriculture", "Tourisme", "Autre activité")),
            fake.unique.random_number(digits=5),
            fake.random_element(elements=("CTX", "Arrangement C.")),
            fake.random_element(elements=("CR", "CCT")),
            fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
            fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            random.randint(10000, 1000000),
            f'CUST{i+1}',
            fake.name(),
            random.randint(100, 5000),
            fake.random_element(elements=("Société", "Personnel", "TRE")),
            fake.random_element(elements=("Versement", "Retrait", "Virement")),
            f'REF{i+1}',
            round(random.uniform(1, 5), 2),
            random.randint(1, 10),
            fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d')
        ]
        writer.writerow(row)

print("CSV file 'bank_customer_data.csv' with 5000 rows has been generated.")
