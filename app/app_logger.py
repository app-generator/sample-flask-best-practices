def message_handle(**kwargs):
    """
    this is the logging/message handler function for the entire application
    :param kwargs: here the kwargs contains `msg` param that contains the message as string :TODO add params for type/severity
    :return: N/A
    """
    print(kwargs.get("msg"))