from django.conf import settings
from djpdf.exceptions import RenderingError
import subprocess

WKHTMLTOPDF_CMD = getattr(settings, 'PDF_WKHTMLTOPDF_CMD', 'wkhtmltopdf')


class Renderer(object):
    def __init__(self, options={'quiet': None}):
        self.options = options
        
    def get_options(self):
        args = []
        for arg, val in self.options.items():
            args.append('--{0}'.format(arg))
            if val:
                args.append(val)
        return args
    
    def get_command(self):
        return [WKHTMLTOPDF_CMD] + self.get_options() + ['-', '-']
        
    def render(self, html, fileObj=None):
        proc = subprocess.Popen(self.get_command(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = proc.communicate(html)
        if result[1]:
            raise RenderingError(result[1].split('\n')[0])
        pdf_content = result[0]
        
        if fileObj:
            fileObj.write(pdf_content)
        return pdf_content
