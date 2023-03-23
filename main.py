import ccxt
import time

binance = ccxt.binance()
symbol = 'ETH/USDT'

# инициализация переменных для определения движения цены
last_price = None
change_threshold = 0.01
change_interval = 60 * 60  # 60 минут

while True:
    # получаем актуальную цену фьючерса ETHUSDT с биржи Binance
    ticker = binance.fetch_ticker(symbol)
    current_price = ticker['last']

    # выводим цену и временную метку
    print(f'{symbol} цена: {current_price} USD ({time.strftime("%H:%M:%S")})')

    # определяем движение цены
    if last_price is not None:
        price_change = (current_price - last_price) / last_price
        if abs(price_change) >= change_threshold:
            print(f'Движение цены на {change_threshold*100:.2f}% за последние {change_interval/60:.0f} минут')
    last_price = current_price

    # ждем 1 секунду перед повторным запросом к бирже
    time.sleep(1)
