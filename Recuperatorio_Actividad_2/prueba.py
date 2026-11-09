with open ("texto.txt","r", encoding="utf-8") as f:
    for p in f.read().lower().split():
        if p.strip(".,:;?!()-¿¡")in ("los", "un", "que", "y") and p not in ("los", "un", "que", "y"):
            print(p)



 