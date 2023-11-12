# Final-project
# Описание поставленной задачи 

Для финального проекта выбрана следующая задача - файнтюниг модели T5 на русскоязычных текстах с последующим деплоем  модели на виртуальный сервер.

-------------

План работы следующий: 

1) Обучение модели Т5 для задач QA. В качестве обчающего датасета выбран SberSQUAD. Это набор данных. состоящий из фрагментов статей из Википедии, вопросов по ним и правильных ответов.

2) Деплой модели. Для этого на хостинге iphoster.net арендован виртуальный сервер VPS-NVE-X. На сервере установлена Ubuntu 20.04. Технические параметры сервера следующие: 30 Гб SSD, процессор Xeon™ @ 3.40GHz 8 ядер, 4 Гб DDR4 памяти.
3) Чтобы получать данные ответы от модели в человекочитаемом формате, был написан простейший сайт. Для разработки сайта использован фреймворк Flask в связке с HTML+CSS. 

-------------

Библиотеки, используемые моделью в работе часто меняются, поэтому создан docker image, развёрнутый на сайте при помощи docker-compose.yaml файла. 


Сайт не имеет доменного имени, доступ к сайту осуществляется по ip адресу 31.24.253.86:8000/

-------------
Все файлы хранятся в соответствующем репозитории на GitHub
