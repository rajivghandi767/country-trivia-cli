import csv

# Reads CSV directly with stdlib — no pandas or sqlite3 needed.
# Returns list of (country, capital) tuples matching the original contract.


def fetch_csv_data() -> list[tuple[str, str]]:
    pairs = []
    with open("data/country_capitals.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row["Country"].strip()
            capital = row["Capital"].strip()
            if country and capital:
                pairs.append((country, capital))
    return pairs


country_capital_data = fetch_csv_data()
