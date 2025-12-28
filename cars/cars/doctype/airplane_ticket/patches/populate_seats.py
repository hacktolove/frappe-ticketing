import frappe
import random
def execute():
	tickets = frappe.get_all("Airplane Ticket", pluck="name")
	print(tickets)
	for ticket in tickets:
		doc = frappe.get_doc("Airplane Ticket", ticket)
		doc.seat = generate_seat()
		doc.save()
	frappe.db.commit()


def generate_seat():
    letters = ["A", "B", "C", "D", "E"]
    random_letter = random.choice(letters)

    random_number = random.randint(1,100)

    return f"{random_number}{random_letter}"

