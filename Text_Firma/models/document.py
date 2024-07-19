from abc import ABC, abstractmethod
import os
from docx2pdf import convert

class Document(ABC):
    """
    Abstrakte Klasse für Dokumente. Definiert die gemeinsame Schnittstelle für alle Dokumenttypen.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def convert_to_pdf(self):
        pass

class WordDocument(Document):
    """
    Klasse für Word-Dokumente. Implementiert die Konvertierung von Word zu PDF.
    """
    def convert_to_pdf(self):
        try:
            output_path = os.path.splitext(self.file_path)[0] + '.pdf'
            convert(self.file_path, output_path)
            return output_path
        except Exception as e:
            raise RuntimeError(f"Fehler bei der Konvertierung von Word zu PDF: {str(e)}")

class PdfDocument(Document):
    """
    Klasse für PDF-Dokumente. Da keine Konvertierung erforderlich ist, wird einfach der Pfad zurückgegeben.
    """
    def convert_to_pdf(self):
        return self.file_path
