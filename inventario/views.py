from django.shortcuts import render

import io
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.

def some_view(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(100,100, "Hello world.")

    p.showPage()
    p.save()

    return FileResponse(buffer, as_attachment=True, filename='inventario.pdf')
