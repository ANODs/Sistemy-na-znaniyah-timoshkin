import random

def max_min_composition(S, T):
    n = len(S)
    m = len(T[0])
    k_len = len(T)
    Q = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            max_val = 0
            for k in range(k_len):
                val = min(S[i][k], T[k][j])
                if val > max_val:
                    max_val = val
            Q[i][j] = round(max_val, 2)
    return Q

def print_matrix(matrix, row_labels, col_labels, row_name=""):
    print(" " * 10, end="")
    for col in col_labels:
        print(f"{col:10}", end="")
    print()
    for i, row in enumerate(matrix):
        print(f"{row_labels[i]:10}", end="")
        for val in row:
            print(f"{val:<10.2f}", end="")
        print()
    print("-" * 50)

def main():
    print("=" * 50)
    print("ПРАКТИЧЕСКАЯ РАБОТА №1 (Вариант 20)")
    print("=" * 50)
    
    # Variant 20 parameters
    num_specs = 4
    num_chars = 3
    num_cands = 4
    
    # Generate random matrices
    S = [[round(random.uniform(0.1, 0.95), 2) for _ in range(num_chars)] for _ in range(num_specs)]
    T = [[round(random.uniform(0.1, 0.95), 2) for _ in range(num_cands)] for _ in range(num_chars)]
    
    spec_labels = [f"Спец_{i+1}" for i in range(num_specs)]
    char_labels = [f"Характ_{i+1}" for i in range(num_chars)]
    cand_labels = [f"Канд_{i+1}" for i in range(num_cands)]
    
    print("Психо-физиологическое профилирование специальностей (S):")
    print_matrix(S, spec_labels, char_labels)
    
    print("Психо-физиологическое профилирование кандидатов на обучение (T):")
    print_matrix(T, char_labels, cand_labels)
    
    Q = max_min_composition(S, T)
    print("Соответствие между специальностями и кандидатами (Q = S ⊗ T):")
    print_matrix(Q, spec_labels, cand_labels)
    
    print("Рекомендуемые специальности для обучения (по каждому кандидату):")
    for j in range(num_cands):
        max_val = max([Q[i][j] for i in range(num_specs)])
        recommended = [str(i+1) for i in range(num_specs) if Q[i][j] == max_val]
        print(f"Кандидат №{j+1} – специальность №{', №'.join(recommended)}")
    print("-" * 50)
    
    print("Рекомендуемые кандидаты для обучения (по каждой специальности):")
    for i in range(num_specs):
        max_val = max(Q[i])
        recommended = [str(j+1) for j in range(num_cands) if Q[i][j] == max_val]
        print(f"Специальность №{i+1} – кандидат №{', №'.join(recommended)}")
    print("=" * 50)

if __name__ == "__main__":
    main()
