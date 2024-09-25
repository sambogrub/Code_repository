
## custom error loggin class
 This will class will create a single instance on a logger and call only that logger throughout other classes

 #custom error logging class
class ErrorLogger():
    _logger = None  # private class logger attribute to store logger instance

    @staticmethod
    def get_logger():
        # create or return the logger
        if ErrorLogger._logger is None: #if a logger has not be set up yet
            # set up the logger only once
            logger = logging.getLogger('recipe_book_error_logger')
            logger.setLevel(logging.ERROR)

            # logging file handler
            file_handler = logging.FileHandler('error.log')

            # creating formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            # add handler to the logger
            logger.addHandler(file_handler)

            # assign logger to class variable
            ErrorLogger._logger = logger
        
        return ErrorLogger._logger