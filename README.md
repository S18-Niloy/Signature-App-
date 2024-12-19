# Django Signature Verification Application

This Django web application allows users to upload two images of signatures and compares the text extracted from them using Tesseract OCR. The application checks if the extracted texts match, indicating whether the signatures are identical.

## Features

- **Image Upload**: Users can upload two signature images.
- **Text Extraction**: Uses Tesseract OCR to extract text from both the original and uploaded signatures.
- **Text Comparison**: Compares the extracted text in a case-insensitive manner and provides a result ("Texts Match" or "Texts Do Not Match").
- **Results Display**: Displays the original text, uploaded text, and the comparison result.

## Installation

Follow the steps below to set up and run the project.

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/signature-verification.git
cd signature-verification```
