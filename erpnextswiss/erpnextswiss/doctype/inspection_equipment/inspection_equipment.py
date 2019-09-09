# -*- coding: utf-8 -*-
# Copyright (c) 2019, libracore (https://www.libracore.com) and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.data import nowdate

class InspectionEquipment(Document):
	pass

	
def check_calibration_status():
	update_status = frappe.db.sql("""
									UPDATE `tabInspection Equipment`
									SET `status` = 'To Calibrate'
									WHERE
										`status` = 'Calibrated'
										AND `next_calibration` < CURDATE()""", as_list=True)