# Copyright (c) 2025, ash and contributors
# For license information, please see license.txt

import frappe
import pypika



def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()

	chart = {
		"data" : {
			"labels" : [x[0] for x in data],
			"datasets" : [{"values" : [x[1] for x in data]}],

		},
		"type" : "pie"
	}

	total = int(sum(x[1] for x in data))

	summary = [{
		"value": total,
		"indicator": "Green",
		"label": "Total Revenue",
		"datatype": "Currency",
		"currency": "SAR"
	}]


	return columns, data , None, chart , summary


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""


	return [
		{
			"label": "Airline",
			"fieldname":"name",
			"fieldtype": "Data",
		},
		{
			"label": "Revenue",
			"fieldname":"revenue",
			"fieldtype": "Currency",
		}
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	# airlines = frappe.db.get_list("Airline" , fields = ["name" , "airplane_flight"])
	airline_doctype = frappe.qb.DocType('Airline')
	airplane_doctype = frappe.qb.DocType('Airplane')
	airplane_flight_doctype = frappe.qb.DocType('Airplane Flight')
	airplane_ticket_doctype = frappe.qb.DocType('Airplane Ticket')


	# Airline -> airplane -> airplane flight -> airplane ticket
	airlines = (
 	frappe.qb.from_(airline_doctype)
	.select(
		airline_doctype.name,
		pypika.functions.Coalesce(pypika.functions.Sum(airplane_ticket_doctype.total_amount) , 0).as_('total_amount')
		)
	.join(airplane_doctype,pypika.JoinType.left).on(airline_doctype.name == airplane_doctype.airline)
	.join(airplane_flight_doctype,pypika.JoinType.left).on(airplane_flight_doctype.airplane == airplane_doctype.name)
	.join(airplane_ticket_doctype,pypika.JoinType.left).on((airplane_ticket_doctype.flight == airplane_flight_doctype.name) & (airplane_flight_doctype.docstatus == 1))
	.groupby(airline_doctype.name)
	.run(as_dict = True)

	)



	# I want to see the list for debugging
	# frappe.throw(str(airlines))

	data = []

	for airline in airlines:
		data.append([airline.name , airline.total_amount])

	return data
	# return [
	# 	["Row 1", 1],
	# 	["Row 2", 2],
	# ]
