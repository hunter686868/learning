import rx
from rx import operators as ops

# Поток чисел с фильтрацией по четности и их умножением
numbers = rx.from_iterable(range(1, 11))

numbers.pipe(
    ops.filter(lambda x: x % 2 == 0),
    ops.map(lambda x: x * 10)
).subscribe(
    on_next=lambda x: print(f"Получено: {x}"),
    on_completed=lambda: print("Обработка завершена")
)

# ------------------
def sensor_emitter(observer, _):
    for _ in range(10):
        value = random.randint(15, 30)
        observer.on_next(value)
        time.sleep(0.5)
    observer.on_completed()

sensor_stream = rx.create(sensor_emitter)

sensor_stream.pipe(
    ops.filter(lambda temp: temp > 25),   # тревога при t > 25
).subscribe(
    on_next=lambda t: print(f"⚠ Высокая температура: {t}°C"),
    on_completed=lambda: print("Мониторинг завершён")
)