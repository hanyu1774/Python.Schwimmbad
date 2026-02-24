# Erklärung

Diese Anwendung wurde nach einem Programmierparadigma strukturiert, welches die IOSP- and IPO-Prinzipien befolgt.

* **IOSP?** Eine Funktion/Methode orchestriert etwas. Oder eine Funktion/Methode hat eine Logik. Niemals beides.
** Flows enthalten einzelne Logiken für gewisse Tasks
** Workflow(s) orchestrieren die Flows

* **IPO?** Ist das EVA-Prinzip: Input -> Processing -> Output
** Models: Enthalten reine Daten (für z.B. Inputs nützlich)
** Flows: Verarbeitung
** Ergebnisse werden in Models gespeichert

