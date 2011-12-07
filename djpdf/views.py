from django.views import generic
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.core.urlresolvers import get_callable
from django.http import HttpResponse

DefaultRenderingBackend = get_callable(getattr(settings, 'PDF_DEFAULT_RENDERER', 'djpdf.renderers.pisa.Renderer'))


class PDFResponseMixin(object):
    pdf_rendering_class = DefaultRenderingBackend
    
    def get_pdf_rendering_class(self):
        if self.pdf_rendering_class:
            cls = self.pdf_rendering_class
        else:
            raise ImproperlyConfigured('Provide pdf_rendering_class.')
        return cls

    def get_pdf_renderer(self):
        if not hasattr(self, 'pdf_renderer'):
            self.pdf_renderer = self.get_pdf_rendering_class()()
        return self.pdf_renderer
    
    def render_to_pdf_string(self, content):
        renderer = self.get_pdf_renderer()
        return renderer.render(content)
        
    def render_to_response(self, context, **kwargs):
        response = super(PDFResponseMixin, self).render_to_response(context, **kwargs)
        response.render()
        return HttpResponse(self.render_to_pdf_string(response.content), mimetype='application/pdf')
        
class PDFView(PDFResponseMixin, generic.base.TemplateView):
    pass
