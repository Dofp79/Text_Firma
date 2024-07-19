import os
import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class Signature:
    """
    Klasse für Signaturen. Implementiert das Hinzufügen der Signatur zu einem PDF.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def add_to_pdf(self, pdf_path):
        try:
            # Signatur als Bild auf ein PDF-Dokument zeichnen
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.drawImage(self.file_path, 100, 100, 150, 50)  # Position und Größe anpassen
            can.save()

            # PDF mit Signatur zum originalen PDF hinzufügen
            packet.seek(0)
            new_pdf = PdfReader(packet)
            existing_pdf = PdfReader(pdf_path)
            output = PdfWriter()

            # Fügen Sie die Signatur zur letzten Seite hinzu
            page = existing_pdf.pages[-1]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)

            # Fügen Sie alle anderen Seiten hinzu
            for i in range(len(existing_pdf.pages) - 1):
                output.add_page(existing_pdf.pages[i])

            # Speichern Sie das signierte Dokument
            output_path = self._get_output_path(pdf_path)
            with open(output_path, "wb") as output_stream:
                output.write(output_stream)

            return output_path
        except Exception as e:
            raise RuntimeError(f"Fehler beim Hinzufügen der Signatur: {str(e)}")

    def _get_output_path(self, input_path):
        base, _ = os.path.splitext(input_path)
        return f"{base}_signed.pdf"
