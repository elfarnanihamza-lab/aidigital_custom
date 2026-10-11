import csv
import os
import re

import frappe
from frappe.translate import get_all_translations

LMS_ONLY_DIR = os.path.join(os.path.dirname(__file__), "lms_only")


def _read_lms_only(language):
	"""Surcharges propres a l'interface LMS (fichier lms_only/<langue>.csv, UTF-8, sans en-tete)."""
	if not language or not re.fullmatch(r"[A-Za-z]{2,3}(-[A-Za-z0-9]{2,8})?", language):
		return {}
	path = os.path.join(LMS_ONLY_DIR, language + ".csv")
	if not os.path.exists(path):
		return {}
	with open(path, encoding="utf-8", newline="") as f:
		return {row[0]: row[1] for row in csv.reader(f) if len(row) >= 2}


@frappe.whitelist(allow_guest=True)
def get_translations():
	"""Remplace lms.lms.api.get_translations : meme logique de langue, plus les surcharges LMS."""
	if frappe.session.user != "Guest":
		language = frappe.db.get_value("User", frappe.session.user, "language")
	else:
		language = frappe.db.get_single_value("System Settings", "language")
	translations = dict(get_all_translations(language))
	translations.update(_read_lms_only(language))
	return translations
