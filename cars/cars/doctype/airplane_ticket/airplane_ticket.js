frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        const d = new frappe.ui.Dialog({
            title: 'Seat Selection',
            fields: [
                {
                    label: 'Seat',
                    fieldname: 'seat',
                    fieldtype: 'Data'
                },
            ],
            size: 'small',
            primary_action_label: 'Submit',
            primary_action(values) {
                frappe.call({
                    method: 'cars.cars.doctype.airplane_ticket.airplane_ticket.select_seat',
                    args: {
                        name: frm.doc.name,   // ← current document name
                        seat: values.seat
                    },
                    callback: () => {
                        frappe.msgprint('Seat selected successfully');
                        d.hide();
                    }
                });
            }
        });

        frm.add_custom_button('Select Seat', () => {
            d.show();
        });
    }
});
