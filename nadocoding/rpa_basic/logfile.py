import logging
from datetime import datetime

# 터미널 로그
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# logging.debug("아 이거 누가 짠거야~~~")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 조금 오래 되었습니다.")
# logging.error("에러가 발생했습니다.")
# logging.critical("심학한 문제가 발생 했습니다.")

# 로그
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 터미널 로그
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일로그
filename = datetime.now().strftime("mylogfile_%Y%m%d_%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)


logging.debug("Log 남기기 TEST 입니다.")
logging.info("자동화 수행 준비")
logging.warning("이 스크립트는 조금 오래 되었습니다.")
logging.error("에러가 발생했습니다.")
logging.critical("심학한 문제가 발생 했습니다.")