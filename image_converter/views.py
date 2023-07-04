from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pytesseract
from PIL import Image

def convert_image_to_text(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image)
        return render(request, 'result.html', {'text': text})
    return render(request, 'index.html')
