# Copyright (c) 2025, ash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Vehicle(Document):
	def before_save(doc):
		doc.full_name = f"{doc.year} {doc.make} {doc.model}"

		pass

	def after_migrate():
		docs = frappe.get_doc("Vehicle")
		frappe.throw(docs)
		return
	    # docs = frappe.get_doc('Vehicle')
		# frappe.throw(docs)
		# return

	def fix_title(self):
		self.full_name = f"{self.year} {self.make} {self.model}"
		self.save()


