## Принципы повторного использования

#### 1. Новый модуль может задавать некоторый базовый тип, который потенциально должен допускать параметризацию другими типами (обобщённые типы, типы-генерики);
#### 2. Новый модуль может объединять несколько функций, которые активно обращаются друг к другу;
#### 3. Новый модуль может входить в семейство модулей, ориентированных на решение некоторой общей задачи, которую не удаётся решить с помощью одного модуля;
#### 4. Новый модуль может предлагать конкретную реализацию родительского модуля, которая должна выбираться динамически (полиморфно) -- например, реализация обобщённого типа для конкретного типа-параметра;
#### 5. Новый модуль может интегрировать общее поведение нескольких модулей, которые различаются лишь деталями.

В python используются 2, 3 и 5 принципы повторного использования.  
2. Модуль точно может объединять несколько функций.  
3. Модуль может входить в семейство модулей с помощью __init__.py
  
  
5. Модуль может импортировать другие модули и использовать в своей работе.
  
  
1. Модуль не может генерировать типы.


4. Модуль без дополнительных ухищрений не может динамически выбирать реализацию. 