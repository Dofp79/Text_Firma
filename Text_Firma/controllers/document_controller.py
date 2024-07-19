import os
from models.document import Document, WordDocument, PdfDocument
from models.signature import Signature

class DocumentController:
    """
    Controller-Klasse, die die Geschäftslogik verwaltet und die Kommunikation zwischen Model und View handhabt.
    """
    def __init__(self):
        self.document = None
        self.signature = None

    def set_document(self, file_path):
        if file_path.endswith('.docx'):
            self.document = WordDocument(file_path)
        elif file_path.endswith('.pdf'):
            self.document = PdfDocument(file_path)
        else:
            raise ValueError("Unsupported file type")

    def set_signature(self, file_path):
        self.signature = Signature(file_path)

    def process_document(self):
        if not self.document or not self.signature:
            raise ValueError("Document or signature not set")

        pdf_path = self.document.convert_to_pdf()
        signed_pdf_path = self.signature.add_to_pdf(pdf_path)
        return signed_pdf_path
