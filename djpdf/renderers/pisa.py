from djpdf.exceptions import RenderingError

import ho.pisa as pisa
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class Renderer(object):
    def __init__(self, options={}):
        self.options = options
    
    def get_command(self):
        return [WKHTMLTOPDF_CMD] + self.get_options() + ['-', '-']
        
    def render(self, html, fileObj=None):
        buff = StringIO()
        
        try:
            pdf = pisa.CreatePDF(html, buff, **self.options)

            if not pdf.err:
                pdf_content = buff.getvalue()
                buff.close()
                
                if not pdf_content:
                    raise RenderingError('Rendering came back empty!')
                    
                if fileObj:
                    fileObj.write(pdf_content)
                return pdf_content
            raise RenderingError(pdf.err)
        except Exception, err:
            raise RenderingError(err)
