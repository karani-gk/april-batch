# Copyright (c) 2023, Gewoffreu Karani and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data




def get_data(filters):
    
    conditions = "1=1"
    
    if(filters.get("ticket_number")):conditions += f" AND vi.ticket_number='{filters.get('ticket_number')}'"
    if(filters.get("inspecting_engineer")):conditions += f" AND vi.inspecting_engineer='{filters.get('inspecting_engineer')}'"
    if(filters.get("plate_number")):conditions += f" AND vi.vehicle_reg='{filters.get('plate_number')}'"
    
    
    my_query = f"""
		SELECT
  			vi.ticket_number,
			vi.inspecting_engineer,
			vi.vehicle_reg,
			si.name,
			si.grand_total
		FROM 
  			`tabVehicle Inspection` AS vi
		JOIN
			`tabSales Invoice` AS si
		ON
			si.ticket_number = vi.ticket_number
		WHERE
			{conditions}
    """
    
    data = frappe.db.sql( my_query )
    return data




def get_columns():
    return [
		"Parking Ticket:Data:200",
		"Inspecting Engineer:Link/User:200",
		"Plate Number:Link/Vehicle:200",
		"Sales Invoice:Link/Sales Invoice:200",
		"Invoice Amount:Currency:200"
	]