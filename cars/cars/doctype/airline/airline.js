// Copyright (c) 2025, ash and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
		frm.sidebar.clear_user_actions();

		if (frm.doc.route) {
			frm.sidebar.add_user_action("Visit Website", function () {
				window.open(frm.doc.route, "_blank");
			});
		}
	},
});
