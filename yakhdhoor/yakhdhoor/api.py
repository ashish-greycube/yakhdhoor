from __future__ import unicode_literals
import frappe


@frappe.whitelist()
def get_customer_branch(customer):
    return frappe.db.sql("""select customer_branch from `tabCustomer Branch List` where parent =%s""" ,customer, as_dict=1)