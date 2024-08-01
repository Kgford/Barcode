from django.shortcuts import render, redirect
from django.http import HttpResponse
from e2_db.models import Order_Detail
from django.views import View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    template_name = "tasks.html"
    success_url = reverse_lazy('manufacturing:barcode_view')
    return redirect('manufacturing:barcode_view')

class BarcodeView(View):
    template_name = "pdf_view.html"
    success_url = reverse_lazy('manufacturing:barcode_view')
    def get(self, request, *args, **kwargs):
        return render (self.request,"manufacturing/pdf_search.html",{})
    
    def post(self, request, *args, **kwargs):
        try:
            job_number = request.POST.get('_job_number', -1)
            print('job_number=',job_number)
            if job_number!=-1:
                return HttpResponseRedirect("http://innpriority:8888/manufacturing/pdf/?job_number=" + str(job_number))
                  
        except IOError as e:
            print ("Lists load Failure ", e)
            print('error = ',e) 
        return render (self.request,"manufacturing/pdf_search.html",{})
