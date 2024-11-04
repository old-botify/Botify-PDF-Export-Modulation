from pdf2image import convert_from_path
import os

def ensure_directories():
    """Create necessary directories if they don't exist."""
    directories = ['inputs', 'inputs/images', 'outputs', 'outputs/images']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def convert_pdf_to_png(pdf_path):
    """
    Convert a PDF file to a series of numbered PNG images.
    
    Args:
        pdf_path (str): Path to the PDF file
    """
    # Ensure directories exist
    ensure_directories()
    
    # Validate PDF path
    if not pdf_path or not os.path.exists(pdf_path):
        raise ValueError(f"PDF file not found: '{pdf_path}'")
    
    if not pdf_path.lower().endswith('.pdf'):
        raise ValueError("File must be a PDF")
    
    # Set output directory
    output_dir = 'outputs/images'
    
    try:
        # Convert PDF to images
        pages = convert_from_path(pdf_path)
        
        # Save each page as PNG with numbered filename
        for i, page in enumerate(pages, start=1):
            output_file = os.path.join(output_dir, f'page_{i:03d}.png')
            page.save(output_file, 'PNG')
            print(f'Saved page {i} as {output_file}')
            
        print(f'\nSuccessfully converted {len(pages)} pages to PNG format.')
        
    except Exception as e:
        print(f'Error converting PDF: {str(e)}')
        raise

def list_input_pdfs():
    """List all PDF files in the inputs directory."""
    pdf_files = [f for f in os.listdir('inputs') if f.lower().endswith('.pdf')]
    return pdf_files

if __name__ == '__main__':
    # Ensure directories exist
    ensure_directories()
    
    while True:
        # List available PDFs
        pdf_files = list_input_pdfs()
        
        if not pdf_files:
            print("\nNo PDF files found in the 'inputs' directory.")
            print("Please place your PDF file in the 'inputs' folder and try again.")
            break
        
        print("\nAvailable PDF files in 'inputs' directory:")
        for i, pdf_file in enumerate(pdf_files, 1):
            print(f"{i}. {pdf_file}")
        
        # Get user selection
        try:
            selection = input("\nEnter the number of the PDF to convert (or 'q' to quit): ").strip()
            
            if selection.lower() == 'q':
                break
            
            index = int(selection) - 1
            if 0 <= index < len(pdf_files):
                selected_pdf = os.path.join('inputs', pdf_files[index])
                try:
                    convert_pdf_to_png(selected_pdf)
                    break
                except Exception as e:
                    print(f"\nFailed to convert PDF: {str(e)}")
                    print("\nPlease make sure:")
                    print("1. The PDF file is not corrupted")
                    print("2. You have read permissions for the PDF file")
                    print("3. You have write permissions in the outputs directory")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")