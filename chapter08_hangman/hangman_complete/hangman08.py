def play_hangman():
    import random
    logo = '''
     __                                                                       
    |  \                                                                      
    | $$____    ______   _______    ______   ______ ____    ______   _______  
    | $$    \  |      \ |       \  /      \ |      \    \  |      \ |       \ 
    | $$$$$$$\  \$$$$$$\| $$$$$$$\|  $$$$$$\| $$$$$$\$$$$\  \$$$$$$\| $$$$$$$\
    | $$  | $$ /      $$| $$  | $$| $$  | $$| $$ | $$ | $$ /      $$| $$  | $$
    | $$  | $$|  $$$$$$$| $$  | $$| $$__| $$| $$ | $$ | $$|  $$$$$$$| $$  | $$
    | $$  | $$ \$$    $$| $$  | $$ \$$    $$| $$ | $$ | $$ \$$    $$| $$  | $$
     \$$   \$$  \$$$$$$$ \$$   \$$ _\$$$$$$$ \$$  \$$  \$$  \$$$$$$$ \$$   \$$
                                  |  \__| $$                                  
                                   \$$    $$                                  
                                    \$$$$$$                                   

    '''
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
              '''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
              =========
              ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    word_list = [
        'abruptly',
        'absurd',
        'abyss',
        'affix',
        'askew',
        'avenue',
        'awkward',
        'axiom',
        'azure',
        'bagpipes',
        'bandwagon',
        'banjo',
        'bayou',
        'beekeeper',
        'bikini',
        'blitz',
        'blizzard',
        'boggle',
        'bookworm',
        'boxcar',
        'boxful',
        'buckaroo',
        'buffalo',
        'buffoon',
        'buxom',
        'buzzard',
        'buzzing',
        'buzzwords',
        'caliph',
        'cobweb',
        'cockiness',
        'croquet',
        'crypt',
        'curacao',
        'cycle',
        'daiquiri',
        'dirndl',
        'disavow',
        'dizzying',
        'duplex',
        'dwarves',
        'embezzle',
        'equip',
        'espionage',
        'euouae',
        'exodus',
        'faking',
        'fishhook',
        'fixable',
        'fjord',
        'flapjack',
        'flopping',
        'fluffiness',
        'flyby',
        'foxglove',
        'frazzled',
        'frizzled',
        'fuchsia',
        'funny',
        'gabby',
        'galaxy',
        'galvanize',
        'gazebo',
        'giaour',
        'gizmo',
        'glowworm',
        'glyph',
        'gnarly',
        'gnostic',
        'gossip',
        'grogginess',
        'haiku',
        'haphazard',
        'hyphen',
        'iatrogenic',
        'icebox',
        'injury',
        'ivory',
        'ivy',
        'jackpot',
        'jaundice',
        'jawbreaker',
        'jaywalk',
        'jazziest',
        'jazzy',
        'jelly',
        'jigsaw',
        'jinx',
        'jiujitsu',
        'jockey',
        'jogging',
        'joking',
        'jovial',
        'joyful',
        'juicy',
        'jukebox',
        'jumbo',
        'kayak',
        'kazoo',
        'keyhole',
        'khaki',
        'kilobyte',
        'kiosk',
        'kitsch',
        'kiwifruit',
        'klutz',
        'knapsack',
        'larynx',
        'lengths',
        'lucky',
        'luxury',
        'lymph',
        'marquis',
        'matrix',
        'megahertz',
        'microwave',
        'mnemonic',
        'mystify',
        'naphtha',
        'nightclub',
        'nowadays',
        'numbskull',
        'nymph',
        'onyx',
        'ovary',
        'oxidize',
        'oxygen',
        'pajama',
        'peekaboo',
        'phlegm',
        'pixel',
        'pizazz',
        'pneumonia',
        'polka',
        'pshaw',
        'psyche',
        'puppy',
        'puzzling',
        'quartz',
        'queue',
        'quips',
        'quixotic',
        'quiz',
        'quizzes',
        'quorum',
        'razzmatazz',
        'rhubarb',
        'rhythm',
        'rickshaw',
        'schnapps',
        'scratch',
        'shiv',
        'snazzy',
        'sphinx',
        'spritz',
        'squawk',
        'staff',
        'strength',
        'strengths',
        'stretch',
        'stronghold',
        'stymied',
        'subway',
        'swivel',
        'syndrome',
        'thriftless',
        'thumbscrew',
        'topaz',
        'transcript',
        'transgress',
        'transplant',
        'triphthong',
        'twelfth',
        'twelfths',
        'unknown',
        'unworthy',
        'unzip',
        'uptown',
        'vaporize',
        'vixen',
        'vodka',
        'voodoo',
        'vortex',
        'voyeurism',
        'walkway',
        'waltz',
        'wave',
        'wavy',
        'waxy',
        'wellspring',
        'wheezy',
        'whiskey',
        'whizzing',
        'whomever',
        'wimpy',
        'witchcraft',
        'wizard',
        'woozy',
        'wristwatch',
        'wyvern',
        'xylophone',
        'yachtsman',
        'yippee',
        'yoked',
        'youthful',
        'yummy',
        'zephyr',
        'zigzag',
        'zigzagging',
        'zilch',
        'zipper',
        'zodiac',
        'zombie',
    ]
    chosen_word = random.choice(word_list)
    print(logo)
    display = []
    for letter in chosen_word:
        display.append("_")
    end_of_game = False

    lives = 6
    while not end_of_game:
        print(stages[lives])

        guess = input("알파벳을 하나 추측해서 입력하시오. >>> ").lower()

        for i in range(len(chosen_word)):

            if chosen_word[i] == guess:
                display[i] = guess

        if guess not in chosen_word:
            lives -= 1
            print(f"당신의 기회는 {lives}번 남았습니다.")

            if lives == 0:
                print("모든 기회를 잃었습니다.")
                end_of_game = True
                print(f"정답은 {chosen_word}입니다.")

        if "_" not in display:
            print("정답입니다.")
            end_of_game = True
        print(" ".join(display))
