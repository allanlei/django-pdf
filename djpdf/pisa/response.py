from django.template.response import TemplateResponse


class PDFTemplateResponse(TemplateResponse):
    def __init__(self, pdf_kwargs={}, *args, **kwargs):
        self.pdf_options = kwargs.pop('pdf_options', {})
        super(PDFTemplateResponse, self).__init__(*args, **kwargs)
        
    @property
    def rendered_content(self):
        from djpdf.utils import render as PDF
        rendered_template = super(PDFTemplateResponse, self).rendered_content
        return PDF.render(rendered_template, **self.pdf_options)
