from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf1_path, pdf2_path, output_path, range1=None, range2=None, watermark_path=None):
    """
    Merges two PDFs with options for custom page ranges, watermark, and output file name.

    Args:
        pdf1_path (str): Path to the first PDF file.
        pdf2_path (str): Path to the second PDF file.
        output_path (str): Path for the output PDF file.
        range1 (tuple, optional): Page range for the first PDF (start, end). Defaults to None (all pages).
        range2 (tuple, optional): Page range for the second PDF (start, end). Defaults to None (all pages).
        watermark_path (str, optional): Path to a PDF file to use as a watermark. Defaults to None.

    Returns:
        str: Success message with output file location.
    """
    try:
        # Read the PDF files
        pdf1 = PdfReader(pdf1_path)
        pdf2 = PdfReader(pdf2_path)
        watermark = PdfReader(watermark_path).pages[0] if watermark_path else None

        writer = PdfWriter()

        # Get the page ranges or default to all pages
        range1 = range1 or (0, len(pdf1.pages))
        range2 = range2 or (0, len(pdf2.pages))

        # Add pages from the first PDF
        for i in range(range1[0], range1[1]):
            page = pdf1.pages[i]
            if watermark:
                page.merge_page(watermark)
            writer.add_page(page)

        # Add pages from the second PDF
        for i in range(range2[0], range2[1]):
            page = pdf2.pages[i]
            if watermark:
                page.merge_page(watermark)
            writer.add_page(page)

        # Write the output PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        return f"PDFs merged successfully into '{output_path}'."

    except Exception as e:
        return f"An error occurred: {e}"