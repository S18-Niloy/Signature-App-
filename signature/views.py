import pytesseract
from django.shortcuts import render
from .forms import SignatureForm
from .models import Signature
import cv2

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """Extract text from an image using Tesseract OCR."""
    # Load the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Perform text extraction
    extracted_text = pytesseract.image_to_string(gray_image)
    return extracted_text.strip()


def compare_texts(original_text, uploaded_text):
    """Compare the extracted texts after converting them to lowercase."""
    if original_text.lower() == uploaded_text.lower():
        return "Texts Match"
    return "Texts Do Not Match"



def upload_signature(request):
    if request.method == 'POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            signature = form.save(commit=False)
            signature.save()

            # Extract texts from the images
            original_text = extract_text_from_image(signature.original_image.path)
            uploaded_text = extract_text_from_image(signature.uploaded_image.path)

            # Compare the extracted texts
            result = compare_texts(original_text, uploaded_text)
            signature.result = f"Original Text: {original_text}\nUploaded Text: {uploaded_text}\nResult: {result}"
            signature.save()

            return render(request, r'C:\Niloy\SignatureApp\signature\templates\signature\result.html', {'signature': signature})
    else:
        form = SignatureForm()
    return render(request, r'C:\Users\Niloy\SignatureApp\signature\templates\signature\upload.html', {'form': form})
