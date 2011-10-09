from django.views import generic
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.core.urlresolvers import get_callable


DefaultRenderingBackend = get_callable(getattr(settings, 'PDF_DEFAULT_RENDERING_BACKEND', 'djpdf.backends.wkhtmltopdf.RenderingBackend'))


class HtmlToPdfMixin(object):
    def render_to_response(self, context, **kwargs):
        response = super(HtmlToPdfMixin, self).render_to_response(context, **kwargs)
        print response.mimetype
        if response.mimetype in ['text/html']:
            pass
        return response
        
class PDFMixin(object):
    pdf_backend_class = DefaultRenderingBackend
    pdf_options = {}
    
    def get_pdf_backend_class(self):
        if self.pdf_backend_class:
            backend = self.pdf_backend_class
        else:
            raise ImproperlyConfigured('Provide pdf_backend')
        return backend

    def get_pdf_options(self):
        if self.pdf_options is not None:
            options = self.pdf_options.copy()
        else:
            raise ImproperlyConfigured('Provide pdf_options')
        return options
    
    def get_pdf_backend(self):
        return self.get_pdf_backend_class()(**self.get_pdf_options())

    def get_pdf_content(self, content):
        if not hasattr(self, 'pdf_backend'):
            self.pdf_backend = self.get_pdf_backend()
        self.pdf_backend.content = content
        return self.pdf_backend.render_to_string()



class PDFView(PDFMixin, generic.base.TemplateView):
    def render_to_response(self, context, **kwargs):
        html = super(PDFView, self).render_to_response(context, **kwargs).render
        return HttpResponse(self.get_pdf_content(html), mimetype='application/pdf')
