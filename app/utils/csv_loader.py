## app/utils/csv_loader.py



import csv
import io
from typing import Tuple, List, Dict


REQUIRED_FIELDS = ["sku", "name", "brand", "mrp", "price", "quantity"]




def parse_and_validate_csv(contents: bytes) -> Tuple[List[Dict], List[Dict]]:
    """Parse CSV bytes and return (valid_rows, failed_rows).


    Each valid row is a dict ready to be inserted into the DB. Each failed row is a dict with 'row' and 'reason'.
    """
    text = contents.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    valid = []
    failed = []


    for i, row in enumerate(reader, start=1):
    # Normalize keys to expected ones (strip whitespace)
        row = {k.strip(): (v.strip() if v is not None else "") for k, v in row.items()}


        # Check required fields
        missing = [f for f in REQUIRED_FIELDS if f not in row or row[f] == ""]
        if missing:
            failed.append({"row_number": i, "row": row, "reason": f"missing fields: {missing}"})
        continue


        # Convert numeric fields
        try:
            mrp = float(row["mrp"])
            price = float(row["price"])
            quantity = int(float(row["quantity"]))
        except Exception as e:
            failed.append({"row_number": i, "row": row, "reason": f"invalid numeric value: {e}"})
            continue


        # Business rules
        if price > mrp:
            failed.append({"row_number": i, "row": row, "reason": "price greater than mrp"})
            continue
        if quantity < 0:
            failed.append({"row_number": i, "row": row, "reason": "negative quantity"})
            continue


        # Build normalized dict
        valid.append({
        "sku": row["sku"],
        "name": row["name"],
        "brand": row["brand"],
        "color": row.get("color"),
        "size": row.get("size"),
        "mrp": mrp,
        "price": price,
        "quantity": quantity,
        })

    return valid, failed