## Описание
Это телеграм-бот, производяющий транслитерацию ФИО по НД РФ.

## Предварительные требования
Docker

## Шаги для запуска

# Клонируйте репозиторий:
git clone <ссылка>
cd ~/my-tg-bot-transliteration/сам тг-канал

# Воспроизведите Docker

docker build -t transliteration_rum_bot .
docker run -d -e TOKEN=<ВАШ_ТОКЕН> --name transliteration_rum_bot transliteration_rum_bot

## Использование

1. По команде /start бот Вас приветствует и объявляет актуальную нормативную документацию, согласно которой производится транслитерация.
2. Поступающие далее сообщения бот обрабатывает и возвращает транслитерированными.
3. Все логи записываются в файл app.log
