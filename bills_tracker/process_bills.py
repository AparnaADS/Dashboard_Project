# process_bills.py
def parse_bills(bills):
    parsed = []
    for bill in bills:
        parsed.append({
            "Vendor": bill.get("vendor_name"),
            "Bill No": bill.get("bill_number"),
            "Due Date": bill.get("due_date"),
            "Amount Due": bill.get("amount_due")
        })
    return sorted(parsed, key=lambda x: x["Due Date"])
