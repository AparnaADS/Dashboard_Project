def parse_payments(payments):
    return [
        {
            "type": "Actual",
            "customer": p.get("customer_name"),
            "amount": p.get("amount"),
            "date": p.get("date"),
            "invoice": p.get("invoice_number", "N/A")
        } for p in payments
    ]

def parse_invoices(data):
    expected = []
    for invoice in data:
        if invoice.get("status") not in ["paid", "void"]:
            expected.append({
                "type": "Expected",
                "customer": invoice.get("customer_name"),
                "amount": invoice.get("total"),
                "date": invoice.get("due_date"),
                "invoice": invoice.get("invoice_number")
            })
    return expected
