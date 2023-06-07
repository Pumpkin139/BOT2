def add():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # 创建 handler 输出到文件
    file_handler = logging.FileHandler("file.log", mode='w') # 一定要加上 mode='w'
    file_handler.setLevel(logging.INFO)

    # handler 输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 创建 logging format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("hello, logging")
    logger.debug("print to debug")
    logger.error("error logging")
    logger.warning("warning logging")
    logger.critical("critical logging")