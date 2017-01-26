class SporeMethod():

    def __init__(self, http_method, regex, optional_params=None,
                 formats=None, documentation=''):
        self.method = http_method
        self.regex = regex.pattern
        self.required_params = regex.groupindex.values()
        self.optional_params = optional_params or []
        self.formats = formats or []
        self.documentation = documentation
