// Copyright (c) 2023, Gewoffreu Karani and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Service Revenue"] = {
	"filters": [
		{
			"fieldname": "ticket_number",
			"label": "Ticket Number",
			"fieldtype": "Link",
			"options": "Parking Ticket",
			"width": 200,
			"reqd": 0
		},
		{
			"fieldname": "inspecting_engineer",
			"label": "Inspecting Engineer",
			"fieldtype": "Link",
			"options": "User",
			"width": 200,
			"reqd": 0
		},
		{
			"fieldname": "plate_number",
			"label": "Plate Number",
			"fieldtype": "Link",
			"options": "Vehicle",
			"width": 200,
			"reqd": 0
		},
		{
			"fieldname": "sales_invoice",
			"label": "Sales Invoice",
			"fieldtype": "Link",
			"options": "Sales Invoice",
			"width": 200,
			"reqd": 0
		},
		{
			"fieldname": "from",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": 80,
			"reqd": 0,
			"default": dateutil.nowdate()
		},
	]
};


// Ticket Number
// Inspecting Engineer
// Plate Number
// Sales Invoice