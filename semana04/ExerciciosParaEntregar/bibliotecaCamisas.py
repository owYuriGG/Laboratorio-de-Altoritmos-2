def main():
    shirts = {
        'Duda' : 'Preta',
        'Thevis' : 'Preta',
        'Mel' : 'Branca',
        'Lucas' : 'Verde',
        'Jardel' : 'Preta'
    }
    print("----- Cores das camisetas -----")
    for key in shirts:
        print(f"{key} -> {shirts[key]}")

main()