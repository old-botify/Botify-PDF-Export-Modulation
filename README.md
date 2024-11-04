# PDF-PNG Converter
This is for usage to append the Botify Custom PDF Report exports.

A Python utility that provides two main functions:
1. Extract PNG images from a PDF file (`extract.py`)
2. Combine multiple PNG images into a single PDF (`png-to-pdf.py`)

## Features

### PDF to PNG Extraction (`extract.py`)
- Convert PDF files to individual numbered PNG images
- Maintains page order with sequential naming (page_001.png, page_002.png, etc.)
- Interactive file selection from input directory
- Preserves image quality

### PNG to PDF Combination (`png-to-pdf.py`)
- Combines multiple PNG images into a single PDF file
- Automatically sorts images by page number
- Maintains original image quality
- Handles RGB conversion automatically
- Customizable output filename

## Requirements

- Python 3.6+
- See `requirements.txt` for Python package dependencies

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd pdf-png-converter
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Converting PDF to PNG Images (Extract)

1. Place your PDF file in the `inputs` folder
2. Run the PDF to PNG extraction script:
```bash
python extract.py
```
3. Select your input PDF file from the displayed list
4. The generated PNG files will be saved in the `outputs/images` directory as:
   - page_001.png
   - page_002.png
   - etc.

### Converting PNG Images to PDF (Combine)

1. Place your PNG files in the `inputs/images` folder
2. Run the PNG to PDF combination script:
```bash
python png-to-pdf.py
```
3. Enter your desired output filename (or press Enter for default 'combined.pdf')
4. The combined PDF will be saved in the `outputs` directory

## File Organization

```
pdf-png-converter/
├── inputs/              # Place input files here
│   ├── *.pdf           # PDF files for extraction
│   └── images/         # PNG files for combination
├── outputs/            # Generated files appear here
│   ├── *.pdf          # Combined PDF outputs
│   └── images/        # Extracted PNG images
├── extract.py          # PDF to PNG conversion script
├── png-to-pdf.py       # PNG to PDF conversion script
├── requirements.txt
└── README.md
```

## File Naming Convention

### PDF to PNG (Extract)
- Input: Any valid PDF filename in `inputs/`
- Output: Automatically numbered PNG files (page_001.png, page_002.png, etc.) in `outputs/images/`

### PNG to PDF (Combine)
- Input: Numbered PNG files in `inputs/images/`
- Output: User-specified PDF filename (default: combined.pdf) in `outputs/`

## Error Handling

Both scripts include comprehensive error handling for:
- Missing input files
- Invalid file formats
- Permission issues
- Corrupted files
- Directory access issues
- File naming conflicts

## Common Issues

If you encounter issues:
1. Ensure all directories exist (the scripts will create them if missing)
2. Check file permissions
3. Verify input file formats (PDF for extraction, PNG for combination)
4. Ensure sufficient disk space for output files

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

MIT License