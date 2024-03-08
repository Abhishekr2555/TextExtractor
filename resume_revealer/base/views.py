from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import extract_text_from_pdf,extract_text_from_doc, extract_text_from_jpg,extract_text_from_ppt
# from .utils import preprocess_text, nlp_analysis


def home(request):
    if request.method == 'POST' and  request.FILES.get('resume'):
        resume_file = request.FILES['resume']
        allowed_extensions = ['pdf', 'doc', 'docx', 'jpg']
        if resume_file.name.split('.')[-1].lower() in allowed_extensions:
            fs = FileSystemStorage()
            saved_file = fs.save(resume_file.name, resume_file)
            file_path = fs.path(saved_file)
            text_content = ''

            if file_path.lower().endswith('.pdf'):
                text_content = extract_text_from_pdf(file_path)
            elif file_path.lower().endswith('.doc') or file_path.lower().endswith('.docx'):
                text_content = extract_text_from_doc(file_path)
            elif file_path.lower().endswith('.jpg'):
                text_content = extract_text_from_jpg(file_path)
            elif file_path.lower().endswith('.pptx'):
                text_content = extract_text_from_ppt(file_path)

            return render(request, 'result.html', {'text_content': text_content})
        else:
            return render(request, 'error.html', {'error_message': 'Unsupported file format. Please upload a PDF, DOC, DOCX, or JPG file.'})
        
        # Preprocess the extracted text
#         # cleaned_text = preprocess_text(text_content)

#         # Perform NLP analysis
#         # nlp_results = nlp_analysis(cleaned_text)
    return render(request, 'input.html')

# <venv>\Scripts\activate.bat

