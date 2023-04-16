# Copyright (c) 2023, Gewoffreu Karani and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class ParkingTicket(Document):
    def before_insert(self):
        self.ticket_number = random.randint(100000, 10000000)
