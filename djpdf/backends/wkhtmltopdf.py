from djpdf.backends import RenderingBackend as BaseRenderingBackend
from django.conf import settings

from subprocess import Popen, PIPE, STDOUT

WKHTMLTOPDF_CMD = getattr(settings, 'PDF_WKHTMLTOPDF_CMD', 'wkhtmltopdf')

'''
If the content has resources that link back to the same server generating the PDF, the server must be able to handle more than 1 connection at a time or else the PDF generation will block.  This will happen with runserver if you also use it to server staticfilesas this is a single connection server for development purposes.
'''

class RenderingBackend(BaseRenderingBackend):
    def render_to_string(self):
        if self._rendered_content is not None:
            return self._rendered_content
    
        options = ' '.join([' '.join('--%s %s'.split(' ')) % (key, value) for key, value in self._options.items()])
        cmd = [WKHTMLTOPDF_CMD]
        for key, value in self._options.items():
            cmd.append('--%s' % key)
            cmd.append(value)
        cmd.append('-q')
        cmd.append('-')
        cmd.append('-')
        
        p = Popen(' '.join(cmd), shell=True, stdin=PIPE, stdout=PIPE)
        rendered_content = p.communicate(self.content)[0]
            
        if rendered_content is None:
            raise Exception('There was a error generating PDF')
            
        self._rendered_content = rendered_content
        return rendered_content
