# Copyright (c) 2025, ash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from cars.cars.doctype.airplane_ticket.airplane_helper import generate_seat

class AirplaneTicket(Document):

  def validate(self):
        total_amount = self.flight_price

        seen_items = set()
        unique_add_ons = []

        for add_on in self.add_ons:
            if add_on.item not in seen_items:
                seen_items.add(add_on.item)
                unique_add_ons.append(add_on)
                total_amount += add_on.amount

        self.set("add_ons", unique_add_ons)

        self.total_amount = total_amount
        if(self.status != "Boarded"):
            frappe.throw("Status can only be updated to Boarded")

        self.validate_capacity_not_exceeded()

  def validate_capacity_not_exceeded(self):
	# airplane ticket -> airplane flight -> airplane
    airplane_flight = frappe.get_doc("Airplane Flight", self.flight)
    airplane = frappe.get_doc("Airplane", airplane_flight.airplane)
    if(airplane.capacity <= frappe.db.count("Airplane Ticket", {"flight": airplane_flight.name})):
        frappe.throw("Capacity exceeded")

  def before_insert(self):
    self.seat = generate_seat()

@frappe.whitelist()
def select_seat(name , seat):
  frappe.db.set_value("Airplane Ticket", name, "seat", seat)
  frappe.db.commit()
  return "Seat selected successfully"
