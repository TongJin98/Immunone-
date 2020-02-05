from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Anchor
from subprocess import Popen, PIPE, STDOUT
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.core.files import File

#import different packages
import sys
from Bio import SeqIO
import csv
import math
import re
import xlwt
import os
from . import anchor_generator


def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Anchors Generator for Human Vaccine Project")


# single file upload
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('document')
        if form.is_valid():
            form.save()
            #find each object and parse
            for fil in files:
                #f = Anchor.objects.latest('id').document.open(mode='r')
                return anchor_generator.analyze_fasta(fil, anchor_generator.V_or_J_or_D(fil))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


# def download_csv_data(request):
#     response = HttpResponse(content_type = 'test/csv')
#     response['Content-Disposition'] = 'attachment; filename = "ThePythonDjango.csv"'
