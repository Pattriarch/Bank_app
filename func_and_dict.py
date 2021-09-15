import logging.config
from logger_for_bank import logger_config
logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')

class Bank:
    def __init__(self, money):
        self._money = money
        logger.info(f"Инициализация баланса, на балансе '{self._money}' рублей")

    def top_up_balance(self, value):
        ans = self._money + value
        self._money = ans
        print(f'Ваш баланс был пополнен на {value} рублей, теперь на вашем счету: {self._money} рублей.')
        logger.info(f"Теперь на балансе:'{self._money}' рублей")
        return ans

    def remove_from_balance(self, value):
        if self._money - value > 0:
            ans = self._money - value
            self._money = ans
            print(f'С вашего баланса было снято {value} рублей, теперь на вашем счету: {self._money} рублей.')
            logger.info(f"Теперь на балансе:'{self._money}' рублей")
            return ans
        else:
            logger.info(f"Недостаточно средств на балансе ({self._money}) рублей"
                        f", чтобы снять {value} рублей")
            return print(f'На вашем балансе недостаточно средств. На вашем счету {self._money} рублей'
                         f', а вы хотите снять {value} рублей.')

    def check_balance(self):
        logger.info(f"На балансе: '{self._money} рублей'")
        return print(f'На вашем счету {self._money} рублей')

