# Copyright (c) 2023, Gewoffreu Karani and Contributors
# See license.txt

import frappe
import unittest

class TestParkingTicket(unittest.TestCase):
    def test_parking_ticket(self):
        test_ticket = frappe.get_doc({
			"doctype": "Parking Ticket",
			"customer": "Geoffrey Karani",
   			"vehicle": "KDF 564T"
		}).insert()
