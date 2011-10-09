class RenderingBackend(object):
    def __init__(self, **kwargs):
        self._unrendered_content = None
        self._rendered_content = None
        self._options = kwargs

    @property
    def content(self):
        return self._unrendered_content

    @content.setter
    def content(self, value):
        if self._unrendered_content is not None:
            if value == self._unrendered_content:
                return
        self._unrendered_content = value
        self._rendered_content = None
        
    def render_to_string(self):
        if self._rendered_content is not None:
            return self._rendered_content
        raise NotImplementedError

    def __unicode__(self):
        return self.render_to_string()
