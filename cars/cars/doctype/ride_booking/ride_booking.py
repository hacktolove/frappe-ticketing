# Copyright (c) 2025, ash and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):

	def before_save(self):
		# get distances
		pass
