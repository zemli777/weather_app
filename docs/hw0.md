# Задание 0

## Про жизнь

 Студент 1 курса магистратуры [факультета информатики и вычислительной техники ИТМО](https://abit.itmo.ru/program/master/computer_systems) \
 Выпускник [МГТУ им Н.Э. Баумана кафедра ИУ6](https://bmstu.ru/chair/komputernye-sistemy-i-seti) \
 Немного схемотехник, [Github](https://github.com/zemli777) \
 [Telegram](@zemli_777) \
 [Вк](https://vk.com/zemli_777)

## Последовательность действий

1) Cоздаем токен в git, сохраняем
2) Клонируем репу

```bash
git clone https://gitlab-pub.yadro.com/devops-school-2024/student/p.zemlyansky.git
```

3) Переходим в директорию и создаем файл описания проекта

```bash
cd p.zemlyansky/
echo "# Петр Землянский" >> README.md
```

4) Конфигурируем гит

```bash
git config user.name "Петр Землянский"
git config user.email "zemlyanskij.petya29@gmail.com"
```

5) Создаем ветку master

```bash
git checkout -b master
```

6) Добавляем изменение проекта в Staging Area, прописываем коммит и пушим в мастем

```bash
git add .
git commit -m "create rep"
git push --set-upstream origin master
```

7) Создаем ветку hw0

```bash
git checkout -b hw0
```

8) Добавляем изменение проекта в Staging Area, прописываем коммит и пушим в ветку hw0

```bash
git add .
git commit -m "#1: add hw0 and bio"
git push --set-upstream origin hw0
```
