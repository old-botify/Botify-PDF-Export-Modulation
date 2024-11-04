from PIL import Image
import os
import re

def ensure_directories():
    """Create necessary directories if they don't exist."""
    directories = ['inputs', 'inputs/images', 'outputs', 'outputs/images']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def convert_pngs_to_pdf(pattern=r'page_\d+\.png'):
    """
    Convert a series of numbered PNG files into a single PDF.
    
    Args:
        pattern (str): Regex pattern to match PNG files (default: 'page_XXX.png' format)
    """
    input_dir = 'inputs/images'
    
    try:
        # Get all PNG files that match the pattern
        png_files = [f for f in os.listdir(input_dir) if f.endswith('.png') and re.match(pattern, f)]
        
        if not png_files:
            print(f"No PNG files matching the pattern '{pattern}' found in {input_dir} directory.")
            return
        
        # Sort files numerically (page_001.png, page_002.png, etc.)
        png_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
        
        print(f"Found {len(png_files)} PNG files.")
        
        # Open first image and convert RGB mode if needed
        first_image = Image.open(os.path.join(input_dir, png_files[0]))
        if first_image.mode != 'RGB':
            first_image = first_image.convert('RGB')
        
        # Get all other images
        other_images = []
        for png_file in png_files[1:]:
            img = Image.open(os.path.join(input_dir, png_file))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            other_images.append(img)
        
        # Get output filename from user
        while True:
            output_file = input('Enter output PDF filename (press Enter for "combined.pdf"): ').strip() or 'combined.pdf'
            if not output_file.lower().endswith('.pdf'):
                output_file += '.pdf'
            
            output_path = os.path.join('outputs', output_file)
            
            # Check if file exists
            if os.path.exists(output_path):
                overwrite = input(f"'{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
                if overwrite == 'y':
                    break
            else:
                break
        
        # Save as PDF
        first_image.save(
            output_path,
            save_all=True,
            append_images=other_images,
            resolution=100.0
        )
        
        print(f"Successfully created PDF: {output_path}")
        print(f"Total pages: {len(png_files)}")
        
    except Exception as e:
        print(f"Error creating PDF: {str(e)}")

if __name__ == '__main__':
    # Ensure directories exist
    ensure_directories()
    
    # Check if input directory has PNG files
    if not os.path.exists('inputs/images'):
        print("Error: 'inputs/images' directory not found.")
        exit(1)
    
    png_files = [f for f in os.listdir('inputs/images') if f.endswith('.png')]
    if not png_files:
        print("No PNG files found in 'inputs/images' directory.")
        print("Please place your PNG files in the 'inputs/images' folder and try again.")
        exit(1)
    
    convert_pngs_to_pdf()