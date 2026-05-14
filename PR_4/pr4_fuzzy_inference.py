import sys

def trapezoidal(x, a, b, c, d=None):
    if d is None:
        # Для случая "очень большое" (f(x)=1 при x > b)
        if x <= a:
            return 0.0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif x > b:
            return 1.0
    else:
        # Стандартная трапециевидная функция
        if x <= a or x >= d:
            return 0.0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x <= c:
            return 1.0
        elif c < x < d:
            return (d - x) / (d - c)
    return 0.0

def main():
    print("=" * 60)
    print("ПРАКТИЧЕСКАЯ РАБОТА №4: АЛГОРИТМЫ НЕЧЕТКОГО ВЫВОДА")
    print("Вычисление коэффициента овладения навыком оператора")
    print("Вариант 20")
    print("=" * 60)
    
    try:
        x = float(input("\nВведите время выполнения упражнения (β1, например от 0 до 120): "))
    except ValueError:
        print("Ошибка ввода. Ожидается число.")
        sys.exit(1)
        
    print(f"\n--- ШАГ 1: ФАЗЗИФИКАЦИЯ (для времени x = {x}) ---")
    # Параметры функций принадлежности для Варианта 20
    mu_vsmall = trapezoidal(x, 0, 9, 18, 27)
    mu_small = trapezoidal(x, 22, 31, 40, 49)
    mu_med = trapezoidal(x, 44, 53, 62, 71)
    mu_big = trapezoidal(x, 66, 75, 84, 93)
    mu_vbig = trapezoidal(x, 88, 96, None) # f(x)=1 при x > 96
    
    print(f"μ 'очень маленькое' : {mu_vsmall:.3f}")
    print(f"μ 'маленькое'       : {mu_small:.3f}")
    print(f"μ 'среднее'         : {mu_med:.3f}")
    print(f"μ 'большое'         : {mu_big:.3f}")
    print(f"μ 'очень большое'   : {mu_vbig:.3f}")
    
    print("\n--- ШАГ 2: ВЫЧИСЛЕНИЕ АКТИВАЦИИ ПРАВИЛ ---")
    # Синглтоны выходной переменной (Вариант 20)
    K_otl = 1.0
    K_hor = 0.6
    K_ud = 0.45
    K_ploh = 0.2
    K_neud = 0.0
    
    # Степень активации правил совпадает со степенью принадлежности (простые условия)
    # ПРАВИЛО 1: ЕСЛИ β1 "оч.маленькое", ТО β2 "отличный" (K=1.0)
    # ПРАВИЛО 2: ЕСЛИ β1 "маленькое", ТО β2 "хороший" (K=0.6)
    # ПРАВИЛО 3: ЕСЛИ β1 "среднее", ТО β2 "удовлетворительный" (K=0.45)
    # ПРАВИЛО 4: ЕСЛИ β1 "большое", ТО β2 "плохой" (K=0.2)
    # ПРАВИЛО 5: ЕСЛИ β1 "оч.большое", ТО β2 "неудовлетворительный" (K=0.0)
    
    rules = [
        ("ПРАВИЛО 1 (Отличный)", mu_vsmall, K_otl),
        ("ПРАВИЛО 2 (Хороший)", mu_small, K_hor),
        ("ПРАВИЛО 3 (Удовлетворительный)", mu_med, K_ud),
        ("ПРАВИЛО 4 (Плохой)", mu_big, K_ploh),
        ("ПРАВИЛО 5 (Неудовлетворительный)", mu_vbig, K_neud)
    ]
    
    numerator = 0.0
    denominator = 0.0
    
    for name, mu, k in rules:
        status = "АКТИВНО" if mu > 0 else "НЕ АКТИВНО"
        print(f"{name:32} | Активация: {mu:.3f} | {status}")
        numerator += mu * k
        denominator += mu
        
    print("\n--- ШАГ 3: ДЕФАЗЗИФИКАЦИЯ (Метод средневзвешенного) ---")
    if denominator == 0:
        print("Введенное время не попадает ни в один из термов. Невозможно вычислить коэффициент.")
    else:
        y = numerator / denominator
        print(f"Итоговый коэффициент овладения навыком (β2) = {y:.3f}")

if __name__ == "__main__":
    main()
