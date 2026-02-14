# Сервис по отслеживанию автомобилей

### Учебный проект по управлению флотом автомобилей разных предприятий, с водителями 

## Основные возможности:

- отслеживание, управление предприятиями, автомобилями и водителями
- учёт автомобилей и их поездок по геолокации и времени
- хранение и анализ GPS-телеметрии
- отправка запросов и получение данных REST API (в том числе добавление в БД)
- веб-интерфейс для менеджеров
- отображение треков на карте
- различная отчетность по множеству параметров
- импорт/экспорт данных
- Уведомления на e-mail и в telegram бота
- развертывание через github actions
- отслеживание состояния через prometheus

Общий вид экрана менеджера

[![Снимок экрана 2026-02-14 в 00.29.14.png](https://iimg.su/s/13/g4tCAIpxggVthNyAdTDinHzzSnS4WAvETw91C88J.png)](https://iimg.su/i/4tCAIp)

Список доступных автомобилей
[![Снимок экрана 2026-02-14 в 00.29.31.png](https://iimg.su/s/13/gEJ8sbvxzDRuUmX1yZ9LG8ze1JqkoBnKdGWzaeac.png)](https://iimg.su/i/EJ8sbv)


## Архитектура
  
Проект реализован на Django и PostgreSQL (GeoDjango).  
Тажке используется Django REST Framework, Kafka, Redis, Prometheus + Grafana
Функционал сервиса частично (отчеты и уведомления) доступен через telegram бота
Развертка сервиса через Github Actions и Docker

---

##  REST API

Основные эндпоинты:

Аунтификация  
`/api-token-auth/`

Автомобили  
```
/api/vehicles/
/api/enterprises/<int:enterprise_id>/vehicles/
/api/vehicles/<int:pk>/info/
/api/vehicles/<int:pk>/edit/
/api/vehicles/<int:pk>/delete/
```
Трекинг поездок
```
/api/vehicles/<int:vehicle_id>/track/
/api/vehicles/<int:vehicle_id>/trips/
/api/vehicles/<int:vehicle_id>/trip_summary/
/api/vehicles/<int:vehicle_id>/upload_trip/
```
Отчеты
```
/report-api/
```
Экспорт/импорт
```
/api/export-data/
/api/import-data/
```
Документация:

```
cars/swagger/
```
Пример запроса
[![Снимок экрана 2026-02-14 в 00.57.24.png](https://iimg.su/s/13/gzG0fQix3drhXNOEO436YYJPHbHpGUVVvc3d0BRp.png)](https://iimg.su/i/zG0fQi)
---

##  Отображение треков

Для идетификации треков используется YandexMapsAPI и Leaflet 

[![jbmYU24LRl3eA-StTZlro1PIz1jyxmbxu6Jhp6-U2akLDOCtEEWmCWzVixo75OGO0uzf5cl5b0LXQXHPcA8kG_aQ.jpg](https://iimg.su/s/13/gYWreOOxHyEL7vcawvwzdXMO325SzsHXALecvG1C.jpg)](https://iimg.su/i/YWreOO)
---

##  Telegram Bot
 
Команды:  
/login <логин> <пароль> - Авторизация менеджера  
/car_mileage <vehicle_id> <start_date> <end_date> [period] - Пробег автомобиля  
/driver_time <driver_id> <start_date> <end_date> [period] - Время езды водителя  
/enterprise_active <enterprise_id> <start_date> <end_date> [period] - Пробег активных автомобилей предприятия  

---

##  Тестирование

В проекте реализовано интеграционное, сквозное и нагрузочное тестирование

---

##  Генерация отчетов

[![Снимок экрана 2026-02-14 в 00.30.37.png](https://iimg.su/s/13/g54LoYVxzRv4XH007ocjpLdVT7jfFsBvR1R70LFh.png)](https://iimg.su/i/54LoYV)

---

## Развёртывание

Образ Docker:  
https://hub.docker.com/repository/docker/hunter6868/project_cars/tags/0.3/

Скрипт GitHub Actions:

https://github.com/ragnos6/project/blob/master/.github/workflows/deploy_cars_vps.yml

---

##  Мониторинг

- Prometheus
- Grafana dashboard
- Логирование запросов

---

##  Теги

`#Django`  
`#CarsService`  
`#GeoDjango`  
`#Kafka`  
`#RESTAPI`  
`#Docker`   
`#Python`  
