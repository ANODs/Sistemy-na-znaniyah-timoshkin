import sys

class Rule:
    def __init__(self, conditions, operator, conclusion):
        # conditions is a list of strings
        # operator is 'AND', 'OR', or 'SIMPLE'
        self.conditions = conditions
        self.operator = operator
        self.conclusion = conclusion

    def evaluate(self, facts):
        if self.operator == 'SIMPLE':
            return self.conditions[0] in facts
        elif self.operator == 'AND':
            return all(cond in facts for cond in self.conditions)
        elif self.operator == 'OR':
            return any(cond in facts for cond in self.conditions)
        return False

    def __str__(self):
        if self.operator == 'SIMPLE':
            cond_str = self.conditions[0]
        else:
            cond_str = f" {self.operator} ".join(self.conditions)
        return f"ЕСЛИ {cond_str} ТО {self.conclusion}"

def main():
    print("=" * 60)
    print("ПРАКТИЧЕСКАЯ РАБОТА №2: ПРОДУКЦИОННЫЕ СИСТЕМЫ")
    print("Тема ВКР: Выбор архитектуры базы данных")
    print("=" * 60)
    
    rules = []
    
    choice = input("Использовать готовые правила для БД? (y/n): ").strip().lower()
    if choice == 'y':
        rules.append(Rule(["Сложные ACID транзакции"], "SIMPLE", "Использовать Реляционную БД (PostgreSQL)"))
        rules.append(Rule(["Высокая нагрузка на чтение", "Высокая нагрузка на запись"], "AND", "Использовать NoSQL (Cassandra/MongoDB)"))
        rules.append(Rule(["Графовые связи", "Неструктурированные данные"], "OR", "Использовать Графовую БД (Neo4j)"))
        rules.append(Rule(["Высокая скорость поиска текста"], "SIMPLE", "Использовать Поисковый движок (Elasticsearch)"))
        rules.append(Rule(["Временные ряды", "Аналитика в реальном времени"], "AND", "Использовать БД временных рядов (InfluxDB)"))
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
            rules.append(Rule(conds, op, concl))
            
    print("\nВаша продукционная система:")
    for i, r in enumerate(rules):
        print(f"Правило {i+1}: {r}")
        
    print("\n--- ПРОЦЕСС ПРЯМОГО ВЫВОДА ---")
    facts_input = input("Введите исходные факты через запятую: ")
    facts = [f.strip() for f in facts_input.split(',')]
    
    print("\nРезультаты вывода по каждому правилу:")
    active_conclusions = set()
    for i, r in enumerate(rules):
        result = r.evaluate(facts)
        status = "АКТИВНО" if result else "НЕ АКТИВНО"
        print(f"Правило {i+1}: {status}")
        if result:
            active_conclusions.add(r.conclusion)
            
    print("\nИТОГОВЫЕ РЕКОМЕНДАЦИИ:")
    if active_conclusions:
        for c in active_conclusions:
            print(f"- {c}")
    else:
        print("- Нет подходящих рекомендаций на основе введенных фактов.")
        
if __name__ == "__main__":
    main()
