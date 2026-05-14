import sys

class FuzzyRule:
    def __init__(self, conditions, operator, conclusion, cf_rule):
        self.conditions = conditions
        self.operator = operator
        self.conclusion = conclusion
        self.cf_rule = cf_rule

    def evaluate(self, facts):
        # facts is a dict: {fact_name: cf_value}
        cf_cond = 0.0
        
        if self.operator == 'SIMPLE':
            cf_cond = facts.get(self.conditions[0], 0.0)
        elif self.operator == 'AND':
            cf1 = facts.get(self.conditions[0], 0.0)
            cf2 = facts.get(self.conditions[1], 0.0)
            cf_cond = min(cf1, cf2)
        elif self.operator == 'OR':
            cf1 = facts.get(self.conditions[0], 0.0)
            cf2 = facts.get(self.conditions[1], 0.0)
            cf_cond = max(cf1, cf2)
            
        return cf_cond * self.cf_rule

    def __str__(self):
        if self.operator == 'SIMPLE':
            cond_str = self.conditions[0]
        else:
            cond_str = f" {self.operator} ".join(self.conditions)
        return f"ЕСЛИ {cond_str} ТО {self.conclusion} (CF правила = {self.cf_rule})"

def main():
    print("=" * 60)
    print("ПРАКТИЧЕСКАЯ РАБОТА №3: НЕЧЕТКИЕ ПРОДУКЦИОННЫЕ СИСТЕМЫ")
    print("Тема ВКР: Выбор архитектуры базы данных")
    print("=" * 60)
    
    rules = []
    
    choice = input("Использовать готовые нечеткие правила для БД? (y/n): ").strip().lower()
    if choice == 'y':
        rules.append(FuzzyRule(["Сложные ACID транзакции"], "SIMPLE", "Использовать Реляционную БД (PostgreSQL)", 0.95))
        rules.append(FuzzyRule(["Высокая нагрузка на чтение", "Высокая нагрузка на запись"], "AND", "Использовать NoSQL (Cassandra/MongoDB)", 0.85))
        rules.append(FuzzyRule(["Графовые связи", "Неструктурированные данные"], "OR", "Использовать Графовую БД (Neo4j)", 0.80))
        rules.append(FuzzyRule(["Высокая скорость поиска текста"], "SIMPLE", "Использовать Поисковый движок (Elasticsearch)", 0.90))
        rules.append(FuzzyRule(["Временные ряды", "Аналитика в реальном времени"], "AND", "Использовать БД временных рядов (InfluxDB)", 0.85))
    else:
        num_rules = int(input("Введите количество правил: "))
        for i in range(num_rules):
            print(f"\n--- Добавление правила {i+1} ---")
            op = input("Тип условия (SIMPLE, AND, OR): ").strip().upper()
            if op == 'SIMPLE':
                c = input("Введите условие: ").strip()
                conds = [c]
            else:
                c1 = input("Введите условие 1: ").strip()
                c2 = input("Введите условие 2: ").strip()
                conds = [c1, c2]
            concl = input("Введите заключение: ").strip()
            cf_r = float(input("Введите коэффициент уверенности правила (CF от 0 до 1): "))
            rules.append(FuzzyRule(conds, op, concl, cf_r))
            
    print("\nВаша нечеткая продукционная система:")
    for i, r in enumerate(rules):
        print(f"Правило {i+1}: {r}")
        
    print("\n--- ПРОЦЕСС ПРЯМОГО ВЫВОДА ---")
    print("Введите исходные факты и их CF в формате 'Факт1:CF1, Факт2:CF2'")
    print("Пример: Сложные ACID транзакции:0.9, Высокая нагрузка на запись:0.8")
    facts_input = input("Ваш ввод: ")
    
    facts = {}
    if facts_input.strip():
        for item in facts_input.split(','):
            parts = item.split(':')
            if len(parts) == 2:
                facts[parts[0].strip()] = float(parts[1].strip())
    
    print("\nРезультаты вывода по каждому правилу:")
    results = []
    for i, r in enumerate(rules):
        cf_result = r.evaluate(facts)
        status = f"АКТИВНО (CF = {cf_result:.2f})" if cf_result > 0 else "НЕ АКТИВНО (CF = 0.0)"
        print(f"Правило {i+1}: {status}")
        if cf_result > 0:
            results.append((r.conclusion, cf_result))
            
    print("\nИТОГОВЫЕ РЕКОМЕНДАЦИИ (по убыванию CF):")
    if results:
        results.sort(key=lambda x: x[1], reverse=True)
        for c, cf in results:
            print(f"- {c} с уверенностью {cf:.2f}")
    else:
        print("- Нет подходящих рекомендаций (все CF = 0).")
        
if __name__ == "__main__":
    main()
