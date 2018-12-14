class RuntimeErrorCustom(Exception):
    """
    Exception raised when a specific error code is need
    please check the return code
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

err = RuntimeErrorCustom('An Error as occured', 500)
print(err.__doc__)
print(err)