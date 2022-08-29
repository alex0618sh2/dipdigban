# dipdigban
Бан доменов по ip в iptables

Запуск:
EXAMPLE sudo python3 dipdigban2.py -a file-domen-IN file-rezult-OUT

file-domen-IN:
domen1
domen2
-------------

file-rezult-OUT-xxxxxx-command:
Сформированные команды для запуска в iptables через bash

Работает так:
Берет домена из входного файла.
Проверяет их на доступность.
Если домен доступен, определяет ip адрес и сохраняет в файл.
Затем на всякий случай проверяет в iptables нет ли уже такого ip
Последнее, генерирует командный файл, для iptables. file-rezult-OUT-xxxxxx-command, который уже подготовленн для запуска в bash

Дополнительныйе опции - можно выполнять все действия по этапно:
        - man flage - 
        -a [start all file :input file domen]
        -t [start test domen :input file domen]
        -e [start explore ip :input file domen]
        -d [start dabl check :input file IP]
        -c [start command generator :input file IP]
        -ta [start test domen and explore ip :input file domen]
        -dc [start dabl check and command generator :input file IP]
        EXAMPLE sudo python3 dipdigban2.py -[xx] file-INPUT file-rezult-OUT
