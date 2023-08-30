def add_class(week):
    for key in week:
        class_today = str(input(f"Qual aula você tem {week[key]}? "))
        week[key] = class_today
    return week

def main():
    week = {
        'Segunda': 'segunda',
        'Terça' : 'terça',
        'Quarta' : 'quarta',
        'Quinta' : 'quinta',
        'Sexta' : 'sexta',
        'Sábado' : 'sábado',
        'Domingo' : 'domingo'
    }
    week = add_class(week)
    print("----- Calendario Semanal de Aulas -----")
    for key in week:
        print(f"{key} --> {week[key]}")

main()