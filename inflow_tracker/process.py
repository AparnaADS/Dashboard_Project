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

def parse_invoices(invoices):
    return [
        {
            "type": "Expected",
            "customer": i.get("customer_name"),
            "amount": i.get("total"),
            "date": i.get("due_date"),
            "invoice": i.get("invoice_number")
        } for i in invoices
    ]
