import fitz

def compress_pdf(input_path, output_path, quality=50):
    """
    Compress a PDF file using PyMuPDF library.

    Parameters:
    - input_path: Input PDF file path.
    - output_path: Output compressed PDF file path.
    - quality: Compression quality (0-100), where 100 is the best quality.

    Returns:
    None
    """
    # Open the PDF file
    pdf_document = fitz.open(input_path)

    # Create a PDF writer for the output file
    pdf_writer = fitz.open()

    # Loop through each page and compress it
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        compressed_page = pdf_writer.new_page(width=page.rect.width, height=page.rect.height)
        compressed_page.insert_page(page_number, page)

        # Get the page content and set the compression quality
        pix = page.get_pixmap(matrix=fitz.Matrix(quality / 100, quality / 100))
        compressed_page.insert_image((0, 0), pixmap=pix)

    # Save the compressed PDF to the output file
    pdf_writer.save(output_path)
    pdf_writer.close()

if __name__ == "__main__":
    input_file = input("Enter the input PDF file path: ")
    output_file = input("Enter the output compressed PDF file path: ")
    compression_quality = int(input("Enter the compression quality (0-100): "))

    compress_pdf(input_file, output_file, compression_quality)
    print(f"PDF compression completed. Compressed file saved to: {output_file}")
