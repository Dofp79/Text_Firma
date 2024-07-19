import PySimpleGUI as sg

class DocumentView:
    """
    View-Klasse, die die Benutzeroberfläche mit PySimpleGUI erstellt und Benutzerinteraktionen handhabt.
    """
    def __init__(self, controller):
        self.controller = controller

    def create_window(self):
        """
        Erzeugt das Hauptfenster der Anwendung mit den notwendigen Eingabefeldern und Schaltflächen.
        """
        layout = [
            [sg.Text("Wählen Sie eine Datei aus:")],
            [sg.Input(), sg.FileBrowse(key="-DOC-")],
            [sg.Text("Wählen Sie eine Signaturdatei aus:")],
            [sg.Input(), sg.FileBrowse(key="-SIG-")],
            [sg.Button("Konvertieren und Signieren"), sg.Button("Beenden")]
        ]
        return sg.Window("Dokument Konverter und Signierer", layout)

    def run(self):
        """
        Startet die Ereignisschleife der Benutzeroberfläche und behandelt Benutzerinteraktionen.
        """
        window = self.create_window()
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "Beenden":
                break
            if event == "Konvertieren und Signieren":
                try:
                    self.controller.set_document(values["-DOC-"])
                    self.controller.set_signature(values["-SIG-"])
                    output_path = self.controller.process_document()
                    sg.popup(f"Dokument wurde konvertiert und signiert: {output_path}")
                except Exception as e:
                    sg.popup_error(f"Fehler: {str(e)}")
        window.close()
