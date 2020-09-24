from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import InquiryForm
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def forms_valid(self, form):
        form.send_email()
        return super().form_valid(form)