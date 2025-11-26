console
frappe.ui.form.on('Vehicle', {
	refresh: function(frm) {
		frm.add_custom_button(__('Get User Email Address'), function() {
			frappe.msgprint(frm.doc.make);
		});
	}
 });
// frappe.listview_settings['Vehicle'] = {
// 	onload: function(listview) {
// 		listview.page.add_menu_item("Something", function() {
// 			console.log("Something");
// 		});
// 	},
// 	button: {
// 		show: function(doc) {
// 		  return doc.reference_name;
// 		},
// 		get_label: function() {
// 		  return __("Open", null, "Access");
// 		},
// 		get_description: function(doc) {
// 		  return __("Open {0}", [
// 			`${__(doc.reference_type)}: ${doc.reference_name}`
// 		  ]);
// 		},
// 		action: function(doc) {
// 		  frappe.set_route("Form", doc.reference_type, doc
// 			.reference_name);
// 		},
// 	  },
// };
