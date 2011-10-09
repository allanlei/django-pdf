from django.conf.urls.defaults import patterns, include, url

from djpdf.wkhtmltopdf.views import PDFView as WebkitPDFView
from djpdf.pisa.views import PDFView as PisaPDFView


urlpatterns = patterns('',
    url(r'^pisa/1.pdf$', PisaPDFView.as_view(template_name='pdf1.html')),
    url(r'^wk/1.pdf$', WebkitPDFView.as_view(template_name='pdf1.html')),

    url(r'^pisa/1.pdf$', PisaPDFView.as_view(template_name='pdf2.html')),
    url(r'^wk/1.pdf$', WebkitPDFView.as_view(template_name='pdf2.html')),

    url(r'^pisa/1.pdf$', PisaPDFView.as_view(template_name='pdf3.html')),
    url(r'^wk/1.pdf$', WebkitPDFView.as_view(template_name='pdf3.html')),
)
