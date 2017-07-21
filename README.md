# decent_parser
The website http://decentralization.gov.ua/ has the information which should be shown on the otg map. Parser would help to check the current state of data in the service and get that data.

## Збір даних
### Отримання посилань на існуючі ОТГ
[Розроблений код](https://github.com/mykolakozyr/decent_parser/blob/master/dec_pars.py) переходить на сторінки областей (напр. [Вінницька область](http://decentralization.gov.ua/region/item/id/1)) та зберігає в [окремий документ](https://github.com/mykolakozyr/decent_parser/blob/master/url_real.txt) посилання на існуючі ОТГ.
### Збір даних по ОТГ (паспорт громади)
[Розроблений код](https://github.com/mykolakozyr/decent_parser/blob/master/otg_pars.py) переходить на сторінки кожної окремої громади і зберігає в окремий файл (напр. [Вапнярська ОТГ](https://github.com/mykolakozyr/decent_parser/blob/master/data/otg_3.csv)) головні атрибути ОТГ. *В процесі доопрацювання з метою збору більшої кількості інформації* 
### Опрацювання даних
Структура таблиць, на порталі Децентралізація влади та характер збереження даних парсеру [Pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html) вимагає подальшої обробки отриманих даних. [Розроблений код](https://github.com/mykolakozyr/decent_parser/blob/master/data_pars.py) перетворює дані у таблицю формату (key|value)
### Створення єдиної таблиці
[Розроблений код](https://github.com/mykolakozyr/decent_parser/blob/master/csv_creator.py) створює єдиний .csv файл. До уваги беруться файли розміром більше 3 кілобайт, тобто ті, що містять паспорт об'єкту. Фінальний результат знаходиться [тут](https://github.com/mykolakozyr/decent_parser/blob/master/data_csv.csv).

## Доопрацювання алгоритму
Фінальні дані потребують обробки. Розробляється алгоритм удосконалення збору та обробки даних.
