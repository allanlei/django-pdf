from django.views import generic

from djpdf.views import BasePDFResponseMixin
from response import PDFTemplateResponse

class PDFView(BasePDFResponseMixin, generic.base.TemplateView):
    response_class = PDFTemplateResponse
