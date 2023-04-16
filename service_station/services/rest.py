import frappe

@frappe.whitelist()
def create_sales_invoice(inspection):
    ticket_number = frappe.db.get_value("Vehicle Inspection", inspection, 'ticket_number')
    customer = frappe.db.get_value("Parking Ticket", ticket_number, 'customer')
    
    # my_query = f"""
    #     SELECT 
    #         pt.customer 
    #     FROM 
    #         `tabParking Ticket` AS pt
    #     JOIN
    #         `tabVehicle Inspection` AS vi
    #     ON pt.name = vi.ticket_number
    #     WHERE vi.name='{inspection}'
    # """
    
    # customer = frappe.db.sql( my_query, as_dict=True )[0]

    
    services = frappe.db.get_all("Required Service Detail", filters={'parent': inspection}, fields=['service_item', 'rate', 'quantity'])
    spare_parts = frappe.db.get_all("Required Spare Detail", filters={'parent': inspection}, fields=['spare_item', 'rate', 'quantity'])
    
    items = []

    for service in services:
        items.append({
            "item_code": service.service_item,
            "qty": service.quantity,
            "rate": service.rate
        })
        
    for spare_part in spare_parts:
        items.append({
            "item_code": spare_part.spare_item,
            "qty": spare_part.quantity,
            "rate": spare_part.rate
        })
    
    
    sales_invoice = frappe.get_doc({
        "doctype": "Sales Invoice",
        "customer": customer,
        "due_date": frappe.utils.nowdate(),
        "ticket_number": ticket_number,
        "items": items
    })
    
    sales_invoice.insert()
    # sales_invoice.submit()
    # frappe.db.commit()
    
    return "Success"
    
    
    
    print(f"\n\n\n { items } \n\n\n")