import os  # Modul zum Arbeiten mit Dateisystemen

# Importiere die benötigten Klassen aus dem models-Paket
from models.document import Document, WordDocument, PdfDocument
from models.signature import Signature

class DocumentController:
    """
    Controller-Klasse, die die Geschäftslogik verwaltet und die Kommunikation zwischen Model und View handhabt.
    Sie folgt dem MVC-Prinzip und kapselt alle Operationen zur Dokumentverarbeitung.
    """
    def __init__(self):
        # Initialisiert den Controller mit leeren Attributen für Dokument und Signatur
        self.document = None
        self.signature = None

    def set_document(self, file_path):
        """
        Setzt das Dokument-Objekt basierend auf dem Dateityp (.docx oder .pdf).
        """
        if file_path.endswith('.docx'):
            self.document = WordDocument(file_path)  # Word-Dokument laden
        elif file_path.endswith('.pdf'):
            self.document = PdfDocument(file_path)   # PDF-Dokument laden
        else:
            # Wird ausgelöst, wenn ein nicht unterstützter Dateityp verwendet wird
            raise ValueError("Unsupported file type")

    def set_signature(self, file_path):
        """
        Setzt die Signatur-Datei für das aktuelle Dokument.
        """
        self.signature = Signature(file_path)

    def process_document(self):
        """
        Führt die Konvertierung in PDF durch (falls nötig) und wendet die Signatur an.
        Gibt den Pfad zur signierten PDF-Datei zurück.
        """
        if not self.document or not self.signature:
            raise ValueError("Document or signature not set")  # Validierung vor dem Prozessieren

        pdf_path = self.document.convert_to_pdf()             # Konvertiere das Dokument in PDF
        signed_pdf_path = self.signature.add_to_pdf(pdf_path) # Signiere das PDF-Dokument
        return signed_pdf_path                                # Rückgabe des Pfads zur signierten Datei
