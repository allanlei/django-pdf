from optparse import make_option
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-l', '--lowquality', action='store', dest='lowquality', default=False, help='Generates lower quality pdf/ps. Useful to shrink the result document space'),
        make_option('-g', '--grayscale', action='store', dest='grayscale', default=False, help='PDF will be generated in grayscale'),
        make_option('--encoding', action='store', dest='encoding', default='utf-8', help='Set the default text encoding, for input'),
        
        make_option('-B', '--margin-bottom', action='store', dest='margin-bottom', default='10mm', help='Set the page bottom margin'),
        make_option('-L', '--margin-left', action='store', dest='margin-left', default='10mm', help='Set the page left margin'),
        make_option('-R', '--margin-right', action='store', dest='margin-right', default='10mm', help='Set the page right margin'),
        make_option('-T', '--margin-top', action='store', dest='margin-top', default='10mm', help='Set the page top margin'),

        make_option('-s', '--page-size', action='store', dest='page-size', default='A4', help='Paper size'),
        make_option('--page-height', action='store', dest='page-height', default='1mm', help='Page height'),
        make_option('--page-width', action='store', dest='page-width', default='1mm', help='Page width'),
        make_option('--page-number-offset', action='store', dest='page-offset', default=1, help='Set the starting page number'),
        make_option('-O', '--orientation', action='store', dest='orientation', default='Portrait', help='Set orientation to Landscape or Portrait'),
        
        make_option('--title', action='store', dest='title', default='', help='The title of the generated pdf file (The title of the first document is used if not specified)'),
    )
    help = 'Converts HTML to PDF'
