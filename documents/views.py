from django.shortcuts import render
from django.http import HttpResponse
from docx import Document
import os


def index(request):
    return render(request, 'documents/index.html')

def generate_document(request):
    if request.method == 'POST':
        # Пример данных (замените на данные из формы)
        data = {
            'company_name': request.POST.get('company_name', 'ООО Ромашка'),
            'client_name': request.POST.get('client_name', 'Иван Иванов'),
            'date': request.POST.get('date', '01.01.2024'),
            'amount': request.POST.get('amount', '10000'),
            'contract_number': request.POST.get('contract_number', '001'),
        }

        # Путь к шаблону
        template_path = os.path.join(os.path.dirname(__file__), 'templates/template.docx')
        output_path = os.path.join(os.path.dirname(__file__), 'templates/generated.docx')

        # Загрузка шаблона и замена плейсхолдеров
        doc = Document(template_path)
        for paragraph in doc.paragraphs:
            for key, value in data.items():
                if f"{{{key}}}" in paragraph.text:
                    paragraph.text = paragraph.text.replace(f"{{{key}}}", value)
        doc.save(output_path)

        # Возврат сгенерированного документа
        with open(output_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=generated.docx'
            return response

    return render(request, 'documents/generate.html')
