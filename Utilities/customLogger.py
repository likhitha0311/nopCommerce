import logging

class LogGen:


  @staticmethod
  def log_generator():
      ''''
      logging.basicConfig(
                   level=logging.INFO,
                   format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                   datefmt='%H:%M:%S',
                   force=True,
                    handlers=[
                       logging.FileHandler("C:\\Users\\karti\\PycharmProjects\\nopCommerce\\Logs\\Automation.log",mode='a'),
                       logging.StreamHandler()
                    ]
                    )

#if above code is used then we will get get chrome driver info messages in terminal, to avoid that we are using below valid code

      #logging.basicConfig(filename="C:\\Users\\karti\\PycharmProjects\\nopCommerce\\Logs\\Automation.log", format='%(asctime)s : %(levelname)s: %(message)s',
    #                   datefmt='%m %d %Y %I:%M:%S %p')

     '''
      logger = logging.getLogger()

      fhandler = logging.FileHandler(filename="C:\\Users\\karti\\PycharmProjects\\nopCommerce\\Logs\\Automation.log", mode='a')
      #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', %H:%M:%S)
      formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s", "%Y-%m-%d %H:%M:%S")
      fhandler.setFormatter(formatter)
      logger.addHandler(fhandler)
      logger.setLevel(logging.INFO)
      return logger


# Below is the working code without any handlers and without class name
# logging.basicConfig(filename="C:\\Users\\karti\\PycharmProjects\\nopCommerce\\Logs\\Automation.log",format='%(asctime)s: %(levelname)s: %(message)s',
#                        datefmt='%H:%M:%S')
# logger=logging.getLogger()
# logger.setLevel(logging.INFO)
# #logger=logging.getLogger()
# logger.debug('debug Spam message')
# logger.debug('debug Spam message')
# logger.info('info Ham message')
# logger.warning('warn Eggs message')
# logger.error('error Spam and Ham message')
# logger.critical('critical Ham and Eggs message')
# ###
