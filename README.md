# aidigital_custom

Application Frappe de personnalisation pour AI Digital Academy (Frappe LMS).
Aucun secret dans ce depot.

## Contenu

| Chemin | Role |
|---|---|
| `aidigital_custom/translations/fr.csv` | Source unique des traductions francaises (colonnes : source, traduction). Charge par Frappe pour tous les sites ou l'app est installee. |
| `aidigital_custom/lms_only/fr.csv` | Surcharges visibles uniquement dans l'interface LMS (`/lms`), sans toucher a l'administration Frappe. Contient aussi les cles dont l'espace initial doit etre conserve. |
| `aidigital_custom/api.py` | Surcharge de `lms.lms.api.get_translations` : traductions Frappe + `lms_only/<langue>.csv`. |
| `aidigital_custom/hooks.py` | Declare la surcharge (`override_whitelisted_methods`). |

## Regles

- Glossaire : voir `GLOSSAIRE.md` du projet (Formation, Promotion, Parcours, Leçon, Chapitre, Devoir, Apprenant, Formateur...).
- Ne pas modifier `translations/fr.csv` a la main sans relire le glossaire ; la cle est le texte anglais exact du code (casse et ponctuation comprises).
- Installation : `bench --site <site> install-app aidigital_custom` (uniquement sur les sites voulus).