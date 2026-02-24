# Readme

Da ich nur Dateien hochladen kann, keine Ordner, stehen zwei Optionen zur Verfügung, falls man das Projekt ausführen möchte:
* Die Namespaces `from <name> import <name>` in den Dateien anpassen.
oder
* Es müssten die Ordner Models, Flows und Workflows erstellt werden und die entsprechenden Dateien reingeschoben werden


`__init__.py` lade ich nicht hoch. Ich habe für dieses Projekt folgende Ordnerstruktur benutzt:
│   program.py
│   pyrightconfig.json // Ist für Pyright / Basedpyright
│
├───Flows
│   │   change_terminal_status.py
│   │   helper_class.py
│   │   receive_a_ticket.py
│   │   __init__.py
│   │
│   ├───Models
│   │   public_swimming_pool.py
│   │   __init__.py
│   │
├───Workflows
│   │   workflow.py
│   │   __init__.py
│   │

