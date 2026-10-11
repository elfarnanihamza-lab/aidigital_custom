app_name = "aidigital_custom"
app_title = "AI Digital Custom"
app_publisher = "AI Digital Academy"
app_description = "Personnalisations AI Digital Academy pour Frappe LMS (traductions, libelles)"
app_license = "mit"

# Traductions de l'interface LMS : Frappe + surcharges propres au LMS (ex. "Assignments" -> "Devoirs")
override_whitelisted_methods = {
	"lms.lms.api.get_translations": "aidigital_custom.api.get_translations",
}
