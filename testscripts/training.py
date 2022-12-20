class Training:
    vocab = {}
    def trainer(vocab):

        destroy = False

        while True:

            orig_vokabel = input("Bitte geb die Vokabel ein von dem die Lösung abgefragt werden soll. Wenn du das Eingeben beeden willst geb c für Continue ein. Wenn du den Trainer komplett beenden willst gebe q für Quit ein.\n")
            
            if orig_vokabel == "q":
                destroy = True
                break
            if orig_vokabel == "c":
                break
            lösungs_vokabel = input("Bitte geb die Lösung von der Vokabel die abgefragt wird ein.\n")

            vocab[orig_vokabel] = lösungs_vokabel


        if destroy == True:
                quit()
        score = 0
        for word, translated_word in vocab.items():
            guess = input(f"Was ist die korrekte Übersetzung von {word}? ")
            if guess == translated_word:
                score += 1
                print("Richtig!\n")
            else:
                print(f"Leider falsch! Richtig wäre {word} gewesen.\n")
        print(f"Du hast {score} von {len(vocab)} Vokabeln richtig beantwortet!")
        input()
    trainer(vocab)
Training()