from random import seed, shuffle
from collections import defaultdict





def play_one_game(seed_val):
    suits = ['♦', '♣', '♠', '♥']
    values_full = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    values = [v for v in values_full if v != '7']
    
    unicode_base = {'♠': 0x1F0A0, '♥': 0x1F0B0, '♦': 0x1F0C0, '♣': 0x1F0D0}
    value_index = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    
    value_to_unicode = {
        '♠': ['\U0001F0A1','\U0001F0A2','\U0001F0A3','\U0001F0A4','\U0001F0A5','\U0001F0A6','\U0001F0A7','\U0001F0A8','\U0001F0A9','\U0001F0AA','\U0001F0AB','\U0001F0AD','\U0001F0AE'],
        '♥': ['\U0001F0B1','\U0001F0B2','\U0001F0B3','\U0001F0B4','\U0001F0B5','\U0001F0B6','\U0001F0B7','\U0001F0B8','\U0001F0B9','\U0001F0BA','\U0001F0BB','\U0001F0BD','\U0001F0BE'],
        '♦': ['\U0001F0C1','\U0001F0C2','\U0001F0C3','\U0001F0C4','\U0001F0C5','\U0001F0C6','\U0001F0C7','\U0001F0C8','\U0001F0C9','\U0001F0CA','\U0001F0CB','\U0001F0CD','\U0001F0CE'],
        '♣': ['\U0001F0D1','\U0001F0D2','\U0001F0D3','\U0001F0D4','\U0001F0D5','\U0001F0D6','\U0001F0D7','\U0001F0D8','\U0001F0D9','\U0001F0DA','\U0001F0DB','\U0001F0DD','\U0001F0DE']
    }
    
    
    suits = ['♦', '♣', '♠', '♥']
    values_full = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    values = [v for v in values_full if v != '7']
    
    unicode_base = {'♠': 0x1F0A0, '♥': 0x1F0B0, '♦': 0x1F0C0, '♣': 0x1F0D0}
    value_index = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    
    #value_index_knight = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 14, 'K': 13}
    
    unicode_cards = {
        i: ["]", "[", unicode] for i, unicode in enumerate([
            "\U0001F0B1", "\U0001F0B2", "\U0001F0B3", "\U0001F0B4", "\U0001F0B5", "\U0001F0B6", "\U0001F0B8", "\U0001F0B9", "\U0001F0BA", "\U0001F0BB","\U0001F0BC", "\U0001F0BD", 
            "\U0001F0C1", "\U0001F0C2", "\U0001F0C3", "\U0001F0C4", "\U0001F0C5", "\U0001F0C6", "\U0001F0C8", "\U0001F0C9", "\U0001F0CA", "\U0001F0CB","\U0001F0CC", "\U0001F0CD", 
            "\U0001F0D1", "\U0001F0D2", "\U0001F0D3", "\U0001F0D4", "\U0001F0D5", "\U0001F0D6", "\U0001F0D8", "\U0001F0D9", "\U0001F0DA", "\U0001F0DB","\U0001F0DC", "\U0001F0DD", 
            "\U0001F0A1", "\U0001F0A2", "\U0001F0A3", "\U0001F0A4", "\U0001F0A5", "\U0001F0A6", "\U0001F0A8", "\U0001F0A9", "\U0001F0AA", "\U0001F0AB","\U0001F0AC", "\U0001F0AD"
        ])
    }
    
    value_to_unicode = {
        '♠': ['🂡','🂢','🂣','🂤','🂥','🂦','🂧','🂨','🂩','🂪','🂫','🂭','🂮'],
        '♥': ['🂱','🂲','🂳','🂴','🂵','🂶','🂷','🂸','🂹','🂺','🂻','🂽','🂾'],
        '♦': ['🃁','🃂','🃃','🃄','🃅','🃆','🃇','🃈','🃉','🃊','🃋','🃍','🃎'],
        '♣': ['🃑','🃒','🃓','🃔','🃕','🃖','🃗','🃘','🃙','🃚','🃛','🃝','🃞']
    }
    
    
    
    L = int(input('Please enter an integer to feed the seed() function: '))
    
    
    
    #print('\nDeck shuffled, ready to start!')
    print
    keys_1 = list(unicode_cards.keys())
    seed(L)
    shuffle(keys_1)
    shuffle_cards = {k: unicode_cards[k] for k in keys_1}
    last_line = [shuffle_cards[i][2] for i in shuffle_cards]
    
    
    unicode_to_card = {}
    for s in suits:
        for v in values_full:  
            uni = chr(unicode_base[s] + value_index[v])
            unicode_to_card[uni] = v + s
    
    
    
    
    deck = [unicode_to_card[c] for c in reversed(last_line) if c in unicode_to_card]
    
    table = [['7' + s] for s in suits]
    
    
    
    output = []
    
    output.append("All 7s removed and placed, rest of deck shuffled, ready to start!")
    output.append("]" * len(deck))
    output.append("")
    output.extend([""] * 6)
    output.append('	' + '	'.join(chr(unicode_base[s] + 7) for s in suits))
    output.extend([""] * 6)
    output.append("")
    
    aside = []
    stage = 1
    first_q = 0
    aside_z = ""   #---------


    def print_table():
        rows = [''] * 13
        for col_idx, col in enumerate(table):
            for card in col:
                v_, s_ = card[:-1], card[-1]
                if v_ in value_index:
                    line = 13 - value_index[v_] 
                    if 0 <= line < 13:
                        idx = value_index[v_]  
                        c = value_to_unicode[s_][idx - 1]
                        existing = rows[line].split('\t') if rows[line] else []
                        cells = [''] * 4
                        for i in range(min(len(existing), 4)):
                            cells[i] = existing[i]
                        cells[col_idx] = c
                        rows[line] = '\t'.join(cells)
        for row in rows:
            if row.strip():
                output.append('\t' + row.rstrip())
            else:
                output.append("")
    
    
    
    def can_place(card, col):
        v = card[:-1]
        if v not in value_index:
            return False
        vi = value_index[v]
        return any(value_index[c[:-1]] == vi - 1 or value_index[c[:-1]] == vi + 1 for c in col)
    
    while stage <= 3:
        if stage != 1:
            output.append("")
        output.append(f"Starting {['first', 'second', 'third'][stage - 1]} round...")
        output.append("")
        i = 0
        while i < len(deck):
            card = deck[i]
            v, s = card[:-1], card[-1]
            suit_idx = suits.index(s)
            col = table[suit_idx]
            vi = value_index[v]
    
            can_place_head = col and value_index[col[0][:-1]] == vi + 1
            can_place_tail = col and value_index[col[-1][:-1]] == vi - 1
    
            if vi == 8 or can_place_head or can_place_tail:
                output.append("Placing card from top of stack of cards left 😊️")
                deck.pop(i)
                if can_place_tail or vi > 7:#-------------
                     
                    col.append(card)
                else:
                    col.insert(0, card)
                output.append("]" * (len(deck)-i))
                #aside_z = "[" * (len(aside) - 1) + (chr(unicode_base[s] + vi) if aside else "")
                output.append(aside_z)  # 打印上一步剩下的
                print_table()
                output.append("")
    
                while aside:
                    top = aside[-1]
                    v2, s2 = top[:-1], top[-1]
                    suit2 = suits.index(s2)
                    col2 = table[suit2]
                    vi2 = value_index[v2]
    
                    can_place_head2 = col2 and value_index[col2[0][:-1]] == vi2 + 1
                    can_place_tail2 = col2 and value_index[col2[-1][:-1]] == vi2 - 1
    
                    if vi2 == 8 or can_place_head2 or can_place_tail2:
                        output.append("Placing card from top of stack of cards put aside 😊️")
                        aside.pop()
                        if vi2 > 7:#----------
                            col2.append(top)
                        else:
                            col2.insert(0, top)
                            
                        output.append("]" * (len(deck)-i))
                        
                        if aside:
                            val = aside[-1][:-1]
                            suit = aside[-1][-1]
                            idx = value_index[val]
                            unicode_card = value_to_unicode[suit][idx - 1]
                            aside_z = "[" * (len(aside) - 1) + unicode_card
                        else:
                            aside_z = ""
                        
                        output.append(aside_z)
                        print_table()
                        output.append("")
    
                        
                    else:
                        output.append("Cannot place card from top of stack of cards put aside ☹️")
                        output.append("")
                        break
            else:
                output.append("Cannot place card from top of stack of cards left ☹️")
                aside.append(card)
                i += 1
                output.append("]" * (len(deck) - i))
                # if vi == 12:     #-------------
                #     vi += 2
                #aside_z = "[" * (len(aside) - 1)+ chr(unicode_base[s] + vi)
                val = card[:-1]
                suit = card[-1]
                idx = value_index[val]
                # if idx >= 8:   #--------
                #     idx -= 1
                unicode_card = value_to_unicode[suit][idx - 1]
                aside_z = "[" * (len(aside) - 1) + unicode_card
    
                output.append(aside_z)
                output.append("")
    
        placed = sum(len(c) for c in table)
        if stage == 3 and len(aside) == 0:
            output.append("You placed all cards, you won 👍")
            #output.append("")
            break
        elif stage == 3 and len(aside) != 0:
            output.append(f"You could not place {len(aside)} cards, you lost 👎")
            #output.append("")
            break
        else:
            deck = aside#------------------
            aside = []
            stage += 1
    
    while True:
        
        if first_q == 0:
            print(f"\nThere are {len(output)} lines of output; what do you want me to do?\n")
            first_q += 1
        else:
            print()
        print("Enter: q to quit")
        print(f"       a last line number (between 1 and {len(output)})")
        print(f"       a first line number (between -1 and -{len(output)})")
        print(f"       a range of line numbers (of the form m--n with 1 <= m <= n <= {len(output)})")
        
        input_line = input("       ")
        cmd = input_line.strip()
        if cmd == 'q':
            break
        elif cmd.isdigit():
            n = int(cmd)
            
            if 1 <= n <= len(output):
                print("")
                for line in output[:n]:
                    print(line)
        elif cmd.startswith('-') and cmd[1:].isdigit():
            n = int(cmd)
            
            if -len(output) <= n <= -1:
                print("")
                for line in output[n:]:
                    print(line)
        elif '--' in cmd:
            try:
                m, n = map(int, cmd.split('--'))
                
                if 1 <= m <= n <= len(output):
                    print("")
                    for line in output[m-1:n]:
                        print(line)
            except:
                continue










def play_one_game_silent(seed_val):
    suits = ['♦', '♣', '♠', '♥']
    values_full = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    values = [v for v in values_full if v != '7']
    
    unicode_base = {'♠': 0x1F0A0, '♥': 0x1F0B0, '♦': 0x1F0C0, '♣': 0x1F0D0}
    value_index = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    
    value_to_unicode = {
        '♠': ['\U0001F0A1','\U0001F0A2','\U0001F0A3','\U0001F0A4','\U0001F0A5','\U0001F0A6','\U0001F0A7','\U0001F0A8','\U0001F0A9','\U0001F0AA','\U0001F0AB','\U0001F0AD','\U0001F0AE'],
        '♥': ['\U0001F0B1','\U0001F0B2','\U0001F0B3','\U0001F0B4','\U0001F0B5','\U0001F0B6','\U0001F0B7','\U0001F0B8','\U0001F0B9','\U0001F0BA','\U0001F0BB','\U0001F0BD','\U0001F0BE'],
        '♦': ['\U0001F0C1','\U0001F0C2','\U0001F0C3','\U0001F0C4','\U0001F0C5','\U0001F0C6','\U0001F0C7','\U0001F0C8','\U0001F0C9','\U0001F0CA','\U0001F0CB','\U0001F0CD','\U0001F0CE'],
        '♣': ['\U0001F0D1','\U0001F0D2','\U0001F0D3','\U0001F0D4','\U0001F0D5','\U0001F0D6','\U0001F0D7','\U0001F0D8','\U0001F0D9','\U0001F0DA','\U0001F0DB','\U0001F0DD','\U0001F0DE']
    }
    
    
    suits = ['♦', '♣', '♠', '♥']
    values_full = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    values = [v for v in values_full if v != '7']
    
    unicode_base = {'♠': 0x1F0A0, '♥': 0x1F0B0, '♦': 0x1F0C0, '♣': 0x1F0D0}
    value_index = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    
    #value_index_knight = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 14, 'K': 13}
    
    unicode_cards = {
        i: ["]", "[", unicode] for i, unicode in enumerate([
            "\U0001F0B1", "\U0001F0B2", "\U0001F0B3", "\U0001F0B4", "\U0001F0B5", "\U0001F0B6", "\U0001F0B8", "\U0001F0B9", "\U0001F0BA", "\U0001F0BB","\U0001F0BC", "\U0001F0BD", 
            "\U0001F0C1", "\U0001F0C2", "\U0001F0C3", "\U0001F0C4", "\U0001F0C5", "\U0001F0C6", "\U0001F0C8", "\U0001F0C9", "\U0001F0CA", "\U0001F0CB","\U0001F0CC", "\U0001F0CD", 
            "\U0001F0D1", "\U0001F0D2", "\U0001F0D3", "\U0001F0D4", "\U0001F0D5", "\U0001F0D6", "\U0001F0D8", "\U0001F0D9", "\U0001F0DA", "\U0001F0DB","\U0001F0DC", "\U0001F0DD", 
            "\U0001F0A1", "\U0001F0A2", "\U0001F0A3", "\U0001F0A4", "\U0001F0A5", "\U0001F0A6", "\U0001F0A8", "\U0001F0A9", "\U0001F0AA", "\U0001F0AB","\U0001F0AC", "\U0001F0AD"
        ])
    }
    
    value_to_unicode = {
        '♠': ['🂡','🂢','🂣','🂤','🂥','🂦','🂧','🂨','🂩','🂪','🂫','🂭','🂮'],
        '♥': ['🂱','🂲','🂳','🂴','🂵','🂶','🂷','🂸','🂹','🂺','🂻','🂽','🂾'],
        '♦': ['🃁','🃂','🃃','🃄','🃅','🃆','🃇','🃈','🃉','🃊','🃋','🃍','🃎'],
        '♣': ['🃑','🃒','🃓','🃔','🃕','🃖','🃗','🃘','🃙','🃚','🃛','🃝','🃞']
    }
    
    
    
    #L = int(input('Please enter an integer to feed the seed() function: '))
    
    
    
    
    keys_1 = list(unicode_cards.keys())
    seed(seed_val)
    shuffle(keys_1)
    shuffle_cards = {k: unicode_cards[k] for k in keys_1}
    last_line = [shuffle_cards[i][2] for i in shuffle_cards]
    
    
    unicode_to_card = {}
    for s in suits:
        for v in values_full:  
            uni = chr(unicode_base[s] + value_index[v])
            unicode_to_card[uni] = v + s
    
    
    
    
    deck = [unicode_to_card[c] for c in reversed(last_line) if c in unicode_to_card]
    
    table = [['7' + s] for s in suits]
    
    
    
    output = []
    
    # output.append("All 7s removed and placed, rest of deck shuffled, ready to start!")
    # output.append("]" * len(deck))
    # output.append("")
    # output.extend([""] * 6)
    # output.append('	' + '	'.join(chr(unicode_base[s] + 7) for s in suits))
    # output.extend([""] * 6)
    # output.append("")
    
    aside = []
    stage = 1
    first_q = 0
    aside_z = ""   #---------


    def print_table():
        rows = [''] * 13
        for col_idx, col in enumerate(table):
            for card in col:
                v_, s_ = card[:-1], card[-1]
                if v_ in value_index:
                    line = 13 - value_index[v_] 
                    if 0 <= line < 13:
                        idx = value_index[v_]  
                        c = value_to_unicode[s_][idx - 1]
                        existing = rows[line].split('\t') if rows[line] else []
                        cells = [''] * 4
                        for i in range(min(len(existing), 4)):
                            cells[i] = existing[i]
                        cells[col_idx] = c
                        rows[line] = '\t'.join(cells)
        for row in rows:
            if row.strip():
                output.append('\t' + row.rstrip())
            else:
                output.append("")
    
    
    
    def can_place(card, col):
        v = card[:-1]
        if v not in value_index:
            return False
        vi = value_index[v]
        return any(value_index[c[:-1]] == vi - 1 or value_index[c[:-1]] == vi + 1 for c in col)
    
    while stage <= 3:
        if stage != 1:
            output.append("")
        output.append(f"Starting {['first', 'second', 'third'][stage - 1]} round...")
        output.append("")
        i = 0
        while i < len(deck):
            card = deck[i]
            v, s = card[:-1], card[-1]
            suit_idx = suits.index(s)
            col = table[suit_idx]
            vi = value_index[v]
    
            can_place_head = col and value_index[col[0][:-1]] == vi + 1
            can_place_tail = col and value_index[col[-1][:-1]] == vi - 1
    
            if vi == 8 or can_place_head or can_place_tail:
                output.append("Placing card from top of stack of cards left 😊️")
                deck.pop(i)
                if can_place_tail or vi > 7:#-------------
                     
                    col.append(card)
                else:
                    col.insert(0, card)
                output.append("]" * (len(deck)-i))
                #aside_z = "[" * (len(aside) - 1) + (chr(unicode_base[s] + vi) if aside else "")
                output.append(aside_z)  # 打印上一步剩下的
                print_table()
                output.append("")
    
                while aside:
                    top = aside[-1]
                    v2, s2 = top[:-1], top[-1]
                    suit2 = suits.index(s2)
                    col2 = table[suit2]
                    vi2 = value_index[v2]
    
                    can_place_head2 = col2 and value_index[col2[0][:-1]] == vi2 + 1
                    can_place_tail2 = col2 and value_index[col2[-1][:-1]] == vi2 - 1
    
                    if vi2 == 8 or can_place_head2 or can_place_tail2:
                        output.append("Placing card from top of stack of cards put aside 😊️")
                        aside.pop()
                        if vi2 > 7:#----------
                            col2.append(top)
                        else:
                            col2.insert(0, top)
                            
                        output.append("]" * (len(deck)-i))
                        
                        if aside:
                            val = aside[-1][:-1]
                            suit = aside[-1][-1]
                            idx = value_index[val]
                            unicode_card = value_to_unicode[suit][idx - 1]
                            aside_z = "[" * (len(aside) - 1) + unicode_card
                        else:
                            aside_z = ""
                        
                        output.append(aside_z)
                        print_table()
                        output.append("")
    
                        
                    else:
                        output.append("Cannot place card from top of stack of cards put aside ☹️")
                        output.append("")
                        break
            else:
                output.append("Cannot place card from top of stack of cards left ☹️")
                aside.append(card)
                i += 1
                output.append("]" * (len(deck) - i))
                # if vi == 12:     #-------------
                #     vi += 2
                #aside_z = "[" * (len(aside) - 1)+ chr(unicode_base[s] + vi)
                val = card[:-1]
                suit = card[-1]
                idx = value_index[val]
                # if idx >= 8:   #--------
                #     idx -= 1
                unicode_card = value_to_unicode[suit][idx - 1]
                aside_z = "[" * (len(aside) - 1) + unicode_card
    
                output.append(aside_z)
                output.append("")
        if stage == 3:
            return len(aside)
        else:
            deck = aside
            aside = []
            stage += 1

    return 0

def simulate(n, i):
    result_count = defaultdict(int)

    for k in range(n):
        cards_left = play_one_game_silent(i + k)
        result_count[cards_left] += 1

    total = n
    results = sorted(result_count.items(), key=lambda x: -x[0])

    print("Number of cards left | Frequency")
    print("-" * 32)
    for cards_left, count in results:
        freq = count / total
        if freq >= 0.00005:
            print(f"{cards_left:>21} | {freq:>7.2%}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        simulate(int(sys.argv[1]), int(sys.argv[2]))
    else:
        seed_val = int(input("Please enter an integer to feed the seed() function: "))
        play_one_game(L)
