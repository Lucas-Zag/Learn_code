## from itertools import chain
## from itertools import chain----tue 25 -1:57----1
from random import seed, shuffle
from collections import defaultdict
from random import randint
import sys

def play_one_game(seed_val):
    
    #L = int(input('Please enter an integer to feed the seed() function: '))
    print()
    print('Deck shuffled, ready to start!')
    unicode_cards = {
        i: ["]","[" ,unicode] for i, unicode in enumerate([
            "\U0001F0B1", "\U0001F0B2", "\U0001F0B3", "\U0001F0B4", "\U0001F0B5", "\U0001F0B6", "\U0001F0B7", "\U0001F0B8", "\U0001F0B9", "\U0001F0BA", "\U0001F0BB", "\U0001F0BD", "\U0001F0BE",  # 红心 ♥
            "\U0001F0C1", "\U0001F0C2", "\U0001F0C3", "\U0001F0C4", "\U0001F0C5", "\U0001F0C6", "\U0001F0C7", "\U0001F0C8", "\U0001F0C9", "\U0001F0CA", "\U0001F0CB", "\U0001F0CD", "\U0001F0CE",  # 方块 ♦
            "\U0001F0D1", "\U0001F0D2", "\U0001F0D3", "\U0001F0D4", "\U0001F0D5", "\U0001F0D6", "\U0001F0D7", "\U0001F0D8", "\U0001F0D9", "\U0001F0DA", "\U0001F0DB", "\U0001F0DD", "\U0001F0DE",  # 梅花 ♣
            "\U0001F0A1", "\U0001F0A2", "\U0001F0A3", "\U0001F0A4", "\U0001F0A5", "\U0001F0A6", "\U0001F0A7", "\U0001F0A8", "\U0001F0A9", "\U0001F0AA", "\U0001F0AB", "\U0001F0AD", "\U0001F0AE",  # 黑桃 ♠
    
        ])
    }
    num_map = {    1: "first",    2: "second",    3: "third",    4: "fourth",    5: "fifth",    6: "sixth",    7: "seventh",    8: "eighth",
       9: "ninth",    10: "tenth"}
    valid_index = [0,13,26,39]
    for add_nub in [0,13,26,39]:
        valid_index.extend(range(add_nub+6,add_nub+13))
    
    
    
    new_cards = {i : unicode_cards[i] for i in sorted(valid_index)}
    new_key = list(range(len(new_cards)))
    old_key = list(new_cards.keys())
    
    for i,j in zip(new_key,old_key):
        new_cards[i]= new_cards.pop(j)
    seed(seed_val)
    shuffle_index = new_key
    shuffle(shuffle_index)
    
    shuffle_cards = {}
    #print(shuffle_index)
    reversed_index = list(reversed(shuffle_index))
    shuffle_cards = {k: new_cards[k] for k in reversed_index}
    
    line_1 = ''.join(new_cards[i][0] for i in range(len(new_cards)) )#######------------------------------
    print(line_1)
    #分成4堆牌
    print()
    step_1 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==0}
    step_2 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==1}
    step_3 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==2}
    step_4 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==3}
    print('Distributing the cards in the deck into 4 stacks.')
    line_2_1 = ''.join(step_1[i][0] for i in step_1)
    line_2_2 = ''.join(step_2[i][0] for i in step_2)
    line_2_3 = ''.join(step_3[i][0] for i in step_3)
    line_2_4 = ''.join(step_4[i][0] for i in step_4)
    
    print(line_2_1, line_2_2, line_2_3, line_2_4,sep = '    ')
    print("\n" * 3)
    #print(f'{  card in first stack, after it has been turned over, is an ace.}')
    set_1 = [step_1, step_2, step_3, step_4]
    width_f = [len(step_1), len(step_2),len(step_3),len(step_4)]
    set_line_4 = [line_2_1, line_2_2, line_2_3, line_2_4]#显示扑克牌
    
    #左对齐，保持位置
    width_1 = len(line_2_2)
    #i = line_5_2
    #z = (f"{i:<{width}}")
    
    
    receive_bin = {}
    step_next_cards = {}
    line_step_next = ''
    pass_card_face = []
    line_receive_bin =''
    
    for step_1 in range(4):
        pass_card = {}
        
        #print(step_1)
        #阶段1 ，第一堆扑克
        face_up_1 = list(set_1[step_1].keys())
        for i in face_up_1:
            if  i not in [0, 8, 16, 24]:
                pass_card[i] = set_1[step_1].pop(i)
            else:
                break
        len_save = len(set_1[step_1])
        
        #step_next_cards.update(set_1[step_1])##元素复制到下一步的牌堆里--------
        #receive_bin.update(pass_card)##元素复制到丢弃的牌堆里------------------
        
        
        index_step1 = list(reversed(set_1[step_1].keys()))
        if len(set_1[step_1]) > 0: #判断剩余长度，牌有ace
            
            if len(set_1[step_1]) == 1:  #-----------判断是不是最后一张
                print(f'{ num_map[len(pass_card)+1].capitalize()} (and last) card in { num_map[step_1+1]} stack, after it has been turned over, is an ace.')
            else:
                print(f'{ num_map[len(pass_card)+1].capitalize()} card in { num_map[step_1+1]} stack, after it has been turned over, is an ace.')
    
            back_index_1 = len(index_step1)-1        
            line_3_1 = ''.join(list(set_1[step_1][i][1] for i in index_step1[:back_index_1]) +list((set_1[step_1][index_step1[-1]][2])))
             #重写第一行
            if step_1 != 3:   #-------                                                       
                set_line_4[step_1] = (f"{line_3_1:<{width_1}}")
            else:
                set_line_4[step_1] = line_3_1
            print(*set_line_4,sep = '    ')
            set_line_4[step_1] = " "*width_1
    
        
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            if len(pass_card) > 0: #第一章不是ace
                line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
                pass_card_face = [' '*12*step_1 + line_3_2]
                #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"---------------------
                print(*pass_card_face)  #第二行
                
    
                
                if step_1 == 0:
                    print("\n" * 2)
                else:
                    if len(receive_bin) != 0:
                        index_receive_bin = list(receive_bin.keys())
                        back_index_bin = len(index_receive_bin)-1
                        line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                        print(line_receive_bin)#pass扑克
                        receive_bin.update(pass_card)#----------
                    else:
                        print()
                    line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                    #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                    print(line_step_next)
                    print()
    
                
                
                if len(receive_bin) == 0  and len(pass_card) != 1:
                    print(f'Discarding the {len(pass_card)} cards before the ace.')
                elif len(receive_bin) == 0  and len(pass_card) == 1:
                    print(f'Discarding the card before the ace.')
                elif len(receive_bin) != 0  and len(pass_card) != 1:
                    print(f'Adding to the cards that have been discarded the {len(pass_card)} cards before the ace.')
                elif len(receive_bin) != 0  and len(pass_card) == 1:
                    print(f'Adding to the cards that have been discarded the card before the ace.')
    
                
                # if len(step_next_cards) == 0 and len(set_1[step_1]) == 1:
                #     print(f'Keeping the ace, turning it over.')
                # elif len(step_next_cards) == 0 and len(set_1[step_1]) != 1:
                #     print(f'Keeping the ace and the {len_save} cards after, turning it over.')
                # elif len(step_next_cards) != 0 and len(set_1[step_1]) == 1:
                #     print(f'Also keeping the ace, turning it over.')
                # elif len(step_next_cards) != 0 and len(set_1[step_1]) != 1:
                #     print(f'Also keeping the ace and the {len_save} cards after, turning them over.')
    
    
                if len(step_next_cards) == 0 and len(set_1[step_1]) == 1:
                    print(f'Keeping the ace, turning it over.')
                elif len(step_next_cards) == 0 and len(set_1[step_1]) > 2:
                    print(f'Keeping the ace and the {len_save - 1} cards after, turning them over.')
                elif len(step_next_cards) == 0 and len(set_1[step_1]) == 2:
                    print(f'Keeping the ace and the card after, turning them over.')
                elif len(step_next_cards) != 0 and len(set_1[step_1]) == 2:
                    print(f'Also keeping the ace and the card after, turning them over.')
                elif len(step_next_cards) != 0 and len(set_1[step_1]) == 1:
                    print(f'Also keeping the ace, turning it over.')
                elif len(step_next_cards) != 0 and len(set_1[step_1]) > 2:
                    print(f'Also keeping the ace and the {len_save - 1} cards after, turning them over.')
    
                    
    
                if step_1 == 3:
                    print()
                else:
                    print(*set_line_4,sep = '    ')
                print()
                receive_bin.update(pass_card)    
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                print(line_receive_bin)#pass扑克
               
                step_next_cards.update(set_1[step_1])#--------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
    
        
            #elif len(pass_card) == width_1:
                
            else: 
                if step_1 == 0:   #第一章是ace，判断是不是第一轮
                    print('\n' * 3)
                else:
                    print()
                    print(line_receive_bin)#pass扑克
                    print(line_step_next)
                    print()
    
                
                if len(step_next_cards) == 0:
                    print(f'Keeping the ace and the {width_f[step_1]-1} cards after, turning them over.')
                else:
                    print(f'Also keeping the ace and the {width_f[step_1]-1} cards after, turning them over.')
    
                if step_1 == 3:
                    print()
                else:
                    print(*set_line_4,sep = '    ')
                #print(*set_line_4,sep = '    ')
                print()
    
                if len(receive_bin) != 0:
                    index_receive_bin = list(receive_bin.keys())
                    back_index_bin = len(index_receive_bin)-1
                    line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                    print(line_receive_bin)#bin扑克
                else:
                    print()
    
    
                
                step_next_cards.update(set_1[step_1])#---------------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
            
        else:   #牌无ace
            print(f'No ace in {num_map[step_1+1]} stack, after it has been turned over.')
            set_line_4[step_1] = ' '*width_1
            if step_1 == 3:
                print()
            else :
                print(*set_line_4,sep = '    ') #第一行
    
            
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
            pass_card_face = [' '*12*step_1 + line_3_2]
            #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"
            print(*pass_card_face)
            
            
            if step_1 == 0:
                print("\n" * 2)
            else:
                if len(receive_bin) != 0:
                    index_receive_bin = list(receive_bin.keys())
                    back_index_bin = len(index_receive_bin)-1
                    line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                    print(line_receive_bin)#pass扑克
                else:
                    print()
                
                #receive_bin.update(pass_card)#---------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
                
            if len(receive_bin) != 0 :
                print(f'Adding to the cards that have been discarded all cards in the stack.')
            else:
                print(f'Discarding all cards in the stack.')
           
            if step_1 == 3:
                print()
            else:    
                print(*set_line_4,sep = '    ')
            print()
            receive_bin.update(pass_card)#-----------
            index_receive_bin = list(receive_bin.keys())
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
            print(line_receive_bin)#pass扑克
            print(line_step_next)
            print()
            
    shuffle_cards = {}#----2
    #print(shuffle_index)
    shuffle_index = list(step_next_cards.keys())
    reversed_index = list(reversed(shuffle_index))
    
    shuffle_cards = {k: new_cards[k] for k in reversed_index}
    
    step_2_1 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%3==0}
    step_2_2 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%3==1}
    step_2_3 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%3==2}
    print('Distributing the cards that have been kept into 3 stacks.')
    line_3_1 = ''.join(step_2_1[i][0] for i in step_2_1)
    line_3_2 = ''.join(step_2_2[i][0] for i in step_2_2)
    line_3_3 = ''.join(step_2_3[i][0] for i in step_2_3)
    
    #print(line_3_1, line_3_2, line_3_3,sep = '   ')
    #print(f'{  card in first stack, after it has been turned over, is an ace.}')
    set_2 = [step_2_1, step_2_2, step_2_3]
    set_line_3 = [f"{line_3_1:<{width_1}}", f"{line_3_2:<{width_1}}", line_3_3]#显示扑克牌
    
    
    print(*set_line_3,sep = '    ')
    #左对齐，保持位置
    print()
    print(line_receive_bin)#pass扑克
    print('\n')
    width_2 = [len(line_3_1), len(line_3_2),len(line_3_1)]
    
    
    
    step_next_cards = {}# 下阶段牌
    pass_card_face = [] # 面朝上pass牌
    line_step_next = ''#---------
    for step_2 in range(3):
        pass_card = {}
        #print(step_1)
        #阶段1 ，第一堆扑克
        face_up_1 = list(set_2[step_2].keys())
        for i in face_up_1:
            if  i not in [0, 8, 16, 24]:
                pass_card[i] = set_2[step_2].pop(i)
            else:
                break
        len_save = len(set_2[step_2])
        
        #step_next_cards.update(set_2[step_2])##元素复制到下一步的牌堆里
        #receive_bin.update(pass_card)##元素复制到丢弃的牌堆里
        
        
        index_step1 = list(reversed(set_2[step_2].keys()))
        if len(set_2[step_2]) > 0:
            if len(set_2[step_2]) == 1:
                print(f'{num_map[len(pass_card)+1].capitalize()} (and last) card in {num_map[step_2+1]} stack, after it has been turned over, is an ace.')
            else:
                print(f'{num_map[len(pass_card)+1].capitalize()} card in {num_map[step_2+1]} stack, after it has been turned over, is an ace.')
            
            back_index_1 = len(index_step1)-1        
            line_3_1 = ''.join(list(set_2[step_2][i][1] for i in index_step1[:back_index_1]) +list((set_2[step_2][index_step1[-1]][2])))
            #重写第一行
            if step_2 != 2:   #-------                                                       
                set_line_3[step_2] = (f"{line_3_1:<{width_1}}")
            else:
                set_line_3[step_2] = line_3_1
            
            #set_line_3[step_2] = (f"{line_3_1:<{width_1}}")
            print(*set_line_3,sep = '    ')
            set_line_3[step_2] = " "*width_1
    
    
    
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            if len(pass_card) > 0:
                line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
                pass_card_face = [' '*12*step_2 + line_3_2]
                #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"---------------------
                print(*pass_card_face)
                
    
                
                
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                print(line_receive_bin)#pass扑克
                receive_bin.update(pass_card)#--------
    
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
    
                if len(pass_card) == 1:
                    print(f'Adding to the cards that have been discarded the card before the ace.')
                else:
                    print(f'Adding to the cards that have been discarded the {len(pass_card)} cards before the ace.')
    
                    
    
    
                if len(step_next_cards) == 0 and len(set_2[step_2]) == 1:
                    print(f'Keeping the ace, turning it over.')
                elif len(step_next_cards) == 0 and len(set_2[step_2]) > 2:
                    print(f'Keeping the ace and the {len_save - 1} cards after, turning them over.')
                elif len(step_next_cards) == 0 and len(set_2[step_2]) == 2:
                    print(f'Keeping the ace and the card after, turning them over.')
                elif len(step_next_cards) != 0 and len(set_2[step_2]) == 2:
                    print(f'Also keeping the ace and the card after, turning them over.')
                elif len(step_next_cards) != 0 and len(set_2[step_2]) == 1:
                    print(f'Also keeping the ace, turning it over.')
                elif len(step_next_cards) != 0 and len(set_2[step_2]) > 2:
                    print(f'Also keeping the ace and the {len_save -1} cards after, turning them over.')
    
    
                    
                if step_2 == 2:
                    print()
                else:
                    print(*set_line_3,sep = '    ')
                #print(*set_line_3,sep = '    ')
                print()
    
                receive_bin.update(pass_card)#---------
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                print(line_receive_bin)#pass扑克
                
                step_next_cards.update(set_2[step_2])#--------
    
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
    
        
            #elif len(pass_card) == width_1:
                
            else:  #第一张是ace
                print()
                print(line_receive_bin)#pass扑克
                print(line_step_next)
                print()
    
                if len(step_next_cards) == 0:
                    print(f'Keeping the ace and the {width_2[step_2]-1} cards after, turning them over.')
                else:
                    print(f'Also keeping the ace and the {width_2[step_2]-1} cards after, turning them over.')
                if step_2 == 2:
                    print()
                else:
                    print(*set_line_3,sep = '    ')
                print()
    
    
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                print(line_receive_bin)#bin扑克
                
                step_next_cards.update(set_2[step_2])#------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
            
        else:    #牌无ace
            print(f'No ace in {num_map[step_2+1]} stack, after it has been turned over.')
            set_line_3[step_2] = ' '*width_1
            if step_2 == 2:
                print()
            else:
                print(*set_line_3,sep = '    ')
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
            pass_card_face = [' '*12*step_2 +line_3_2]
    
            #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"
            print(*pass_card_face)
            
                
            index_receive_bin = list(receive_bin.keys())#--------
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
            print(line_receive_bin)#bin扑克
    
            line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
            #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
            print(line_step_next)
            print()
    
            
            print(f'Adding to the cards that have been discarded all cards in the stack.')
            
            if step_2 == 2:
                print()
            else:
                print(*set_line_3,sep = '    ')
            #print(*set_line_3,sep = '    ')
            print()
            receive_bin.update(pass_card)#-----------
            index_receive_bin = list(receive_bin.keys())
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
            print(line_receive_bin)#bin扑克
    
            print(line_step_next)
            print()
    
    
    
    
    
    
    ## shuffle_cards = {}#----3
    #print(shuffle_index)
    shuffle_index = list(step_next_cards.keys())
    reversed_index = list(reversed(shuffle_index))
    
    shuffle_cards = {k: new_cards[k] for k in reversed_index}
    
    step_3_1 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%2==0}
    step_3_2 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%2==1}
    print('Distributing the cards that have been kept into 2 stacks.')
    line_4_1 = ''.join(step_3_1[i][0] for i in step_3_1)
    line_4_2 = ''.join(step_3_2[i][0] for i in step_3_2)
    
    #print(line_3_1, line_3_2, line_3_3,sep = '   ')
    #print(f'{  card in first stack, after it has been turned over, is an ace.}')
    set_2 = [step_3_1, step_3_2]
    set_line_3 = [f"{line_4_1:<{width_1}}", line_4_2]#显示扑克牌
    
    # if steo_2 != 2:
    print(*set_line_3,sep = '    ')
    # else:
    #     print()
    #左对齐，保持位置
    print()
    print(line_receive_bin)#pass扑克
    print('\n')
    width_2 = [len(line_4_1), len(line_4_2)]
    
    
    
    step_next_cards = {}# 下阶段牌
    pass_card_face = [] # 面朝上pass牌
    line_step_next = ''#--------
    for step_3 in range(2):
        pass_card = {}
        #print(step_1)
        #阶段1 ，第一堆扑克
        face_up_1 = list(set_2[step_3].keys())
        for i in face_up_1:
            if  i not in [0, 8, 16, 24]:
                pass_card[i] = set_2[step_3].pop(i)
            else:
                break
        len_save = len(set_2[step_3])
        
        #step_next_cards.update(set_2[step_3])##元素复制到下一步的牌堆里
        #receive_bin.update(pass_card)##元素复制到丢弃的牌堆里
        
        
        index_step1 = list(reversed(set_2[step_3].keys()))
        if len(set_2[step_3]) > 0:
            if len(set_2[step_3]) ==1:
                print(f'{num_map[len(pass_card)+1].capitalize()} (and last) card in {num_map[step_3+1]} stack, after it has been turned over, is an ace.')            
            else:
                print(f'{num_map[len(pass_card)+1].capitalize()} card in {num_map[step_3+1]} stack, after it has been turned over, is an ace.')
            
            back_index_1 = len(index_step1)-1
            line_3_1 = ''.join(list(set_2[step_3][i][1] for i in index_step1[:back_index_1]) +list((set_2[step_3][index_step1[-1]][2])))
            #重写第一行
    
            if step_3 != 1:   #-------                                                       
                set_line_3[step_3] = (f"{line_3_1:<{width_1}}")
            else:
                set_line_3[step_3] = line_3_1
    
            
            #set_line_3[step_3] = (f"{line_3_1:<{width_1}}")
            print(*set_line_3,sep = '    ')
            set_line_3[step_3] = " "*width_1
    
    
    
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            if len(pass_card) > 0: #牌堆有ace
                
                line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
                pass_card_face = [' '*12*step_3 + line_3_2]
                #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"---------------------
                print(*pass_card_face)
                
    
                
                if receive_bin:
                    index_receive_bin = list(receive_bin.keys())
                    back_index_bin = len(index_receive_bin)-1
                    line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                    print(line_receive_bin)#pass扑克
                    receive_bin.update(pass_card)#--------
    
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
    
                
                if len(pass_card) == 1:
                    print(f'Adding to the cards that have been discarded the card before the ace.')
                else:
                    print(f'Adding to the cards that have been discarded the {len(pass_card)} cards before the ace.')
                
                    
    
    
    
                
                if len(step_next_cards) == 0 and len(set_2[step_3]) == 1:
                    print(f'Keeping the ace, turning it over.')
                elif len(step_next_cards) == 0 and len(set_2[step_3]) > 2:
                    print(f'Keeping the ace and the {len_save - 1} cards after, turning them over.')
                elif len(step_next_cards) == 0 and len(set_2[step_3]) == 2:
                    print(f'Keeping the ace and the card after, turning them over.')
                elif len(step_next_cards) != 0 and len(set_2[step_3]) == 2:
                    print(f'Also keeping the ace and the card after, turning them over.')
                elif len(step_next_cards) != 0 and len(set_2[step_3]) == 1:
                    print(f'Also keeping the ace, turning it over.')
                elif len(step_next_cards) != 0 and len(set_2[step_3]) > 2:
                    print(f'Also keeping the ace and the {len_save - 1} cards after, turning them over.')
                
                
                if step_3 == 1:
                    print()
                else:
                    print(*set_line_3,sep = '    ')
                #print(*set_line_3,sep = '    ')
                print()
                
                receive_bin.update(pass_card)#---------
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                print(line_receive_bin)#pass扑克
                
                step_next_cards.update(set_2[step_3])#--------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
    
        
            #elif len(pass_card) == width_1:
                
            else:#第一章是ace
                print()
                print(line_receive_bin)#pass扑克
                print(line_step_next)
                print()
                if len(step_next_cards) == 0:
                    if len(set_2[step_3]) == 1:
                        print(f'Keeping the ace, turning it over.')
                    elif len(set_2[step_3]) ==2:
                        print(f'Keeping the ace and the card after, turning them over.')
                    else:
                        print(f'Keeping the ace and the {width_2[step_3]-1} cards after, turning them over.')
                else:
                    if len(set_2[step_3]) == 1:
                        print(f'Also keeping the ace, turning it over.')
                    elif len(set_2[step_3]) ==2:
                        print(f'Also keeping the ace and the card after, turning them over.')
                    else:                
                        print(f'Also keeping the ace and the {width_2[step_3]-1} cards after, turning them over.')
                if step_3 == 1:
                    print()
                else:
                    print(*set_line_3,sep = '    ')
                #print(*set_line_3,sep = '    ')
                print()
    
    
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                print(line_receive_bin)#pass扑克
    
                step_next_cards.update(set_2[step_3])
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                print(line_step_next)
                print()
            
        else:
            print(f'No ace in {step_3+1} stack, after it has been turned over.')
            if step_3 != 1:
                set_line_3[step_3] = ' '*width_1
                print(*set_line_3,sep = '    ')
            else:
                print()
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
            pass_card_face = [' '*12*step_3 +line_3_2]
    
            #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"
            print(*pass_card_face)
            
            index_receive_bin = list(receive_bin.keys())#--------
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
            print(line_receive_bin)#bin扑克
            
            line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
            #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
            print(line_step_next)
            print()
    
            print(f'Adding to the cards that have been discarded all cards in the stack.')
            
            if step_3 != 1:  
                print(*set_line_3,sep = '    ')
            else:
                print()
    
            print()
            receive_bin.update(pass_card)#-----------
            index_receive_bin = list(receive_bin.keys())
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
            print(line_receive_bin)#bin扑克
    
            
            line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
            #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
            print(line_step_next)
            print()
    
    print(f'Displaying the {len(step_next_cards)} cards that have been kept.')
    if len(step_next_cards) == 4:
        print('You won!')
    else:
        target_nb = {0, 8, 16, 24}
        test_nb = list(step_next_cards.keys())
        len_test = len(test_nb)
        for i in range(len_test-3):
            window = set(test_nb[i : i+4])
            if window == target_nb:
                print('You won!')
                break
        else:
            print('You lost!')
    print()
    print()
    print(line_receive_bin)
    last_line =list(reversed(list(step_next_cards[i][2] for i in step_next_cards)))
    print(*last_line,sep = '')

def play_one_game_silent(seed_val):


 #L = int(input('Please enter an integer to feed the seed() function: '))
    unicode_cards = {
        i: ["]","[" ,unicode] for i, unicode in enumerate([
            "\U0001F0B1", "\U0001F0B2", "\U0001F0B3", "\U0001F0B4", "\U0001F0B5", "\U0001F0B6", "\U0001F0B7", "\U0001F0B8", "\U0001F0B9", "\U0001F0BA", "\U0001F0BB", "\U0001F0BD", "\U0001F0BE",  # 红心 ♥
            "\U0001F0C1", "\U0001F0C2", "\U0001F0C3", "\U0001F0C4", "\U0001F0C5", "\U0001F0C6", "\U0001F0C7", "\U0001F0C8", "\U0001F0C9", "\U0001F0CA", "\U0001F0CB", "\U0001F0CD", "\U0001F0CE",  # 方块 ♦
            "\U0001F0D1", "\U0001F0D2", "\U0001F0D3", "\U0001F0D4", "\U0001F0D5", "\U0001F0D6", "\U0001F0D7", "\U0001F0D8", "\U0001F0D9", "\U0001F0DA", "\U0001F0DB", "\U0001F0DD", "\U0001F0DE",  # 梅花 ♣
            "\U0001F0A1", "\U0001F0A2", "\U0001F0A3", "\U0001F0A4", "\U0001F0A5", "\U0001F0A6", "\U0001F0A7", "\U0001F0A8", "\U0001F0A9", "\U0001F0AA", "\U0001F0AB", "\U0001F0AD", "\U0001F0AE",  # 黑桃 ♠
    
        ])
    }
    num_map = {    1: "first",    2: "second",    3: "third",    4: "fourth",    5: "fifth",    6: "sixth",    7: "seventh",    8: "eighth",
       9: "ninth",    10: "tenth"}
    valid_index = [0,13,26,39]
    for add_nub in [0,13,26,39]:
        valid_index.extend(range(add_nub+6,add_nub+13))
    
    
    
    new_cards = {i : unicode_cards[i] for i in sorted(valid_index)}
    new_key = list(range(len(new_cards)))
    old_key = list(new_cards.keys())
    
    for i,j in zip(new_key,old_key):
        new_cards[i]= new_cards.pop(j)
    seed(seed_val)
    shuffle_index = new_key
    shuffle(shuffle_index)
    
    shuffle_cards = {}
    reversed_index = list(reversed(shuffle_index))
    shuffle_cards = {k: new_cards[k] for k in reversed_index}
    
    line_1 = ''.join(new_cards[i][0] for i in range(len(new_cards)) )#######------------------------------
    #分成4堆牌
    step_1 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==0}
    step_2 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==1}
    step_3 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==2}
    step_4 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%4==3}
    line_2_1 = ''.join(step_1[i][0] for i in step_1)
    line_2_2 = ''.join(step_2[i][0] for i in step_2)
    line_2_3 = ''.join(step_3[i][0] for i in step_3)
    line_2_4 = ''.join(step_4[i][0] for i in step_4)
    
    set_1 = [step_1, step_2, step_3, step_4]
    width_f = [len(step_1), len(step_2),len(step_3),len(step_4)]
    set_line_4 = [line_2_1, line_2_2, line_2_3, line_2_4]#显示扑克牌
    
    #左对齐，保持位置
    width_1 = len(line_2_2)
    #i = line_5_2
    #z = (f"{i:<{width}}")
    
    
    receive_bin = {}
    step_next_cards = {}
    line_step_next = ''
    pass_card_face = []
    line_receive_bin =''
    
    for step_1 in range(4):
        pass_card = {}
        
        #阶段1 ，第一堆扑克
        face_up_1 = list(set_1[step_1].keys())
        for i in face_up_1:
            if  i not in [0, 8, 16, 24]:
                pass_card[i] = set_1[step_1].pop(i)
            else:
                break
        len_save = len(set_1[step_1])
        
        #step_next_cards.update(set_1[step_1])##元素复制到下一步的牌堆里--------
        #receive_bin.update(pass_card)##元素复制到丢弃的牌堆里------------------
        
        
        index_step1 = list(reversed(set_1[step_1].keys()))
        if len(set_1[step_1]) > 0: #判断剩余长度，牌有ace
            
            
    
            back_index_1 = len(index_step1)-1        
            line_3_1 = ''.join(list(set_1[step_1][i][1] for i in index_step1[:back_index_1]) +list((set_1[step_1][index_step1[-1]][2])))
             #重写第一行
            if step_1 != 3:   #-------                                                       
                set_line_4[step_1] = (f"{line_3_1:<{width_1}}")
            else:
                set_line_4[step_1] = line_3_1
            
            set_line_4[step_1] = " "*width_1
    
        
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            if len(pass_card) > 0: #第一章不是ace
                line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
                pass_card_face = [' '*12*step_1 + line_3_2]
                #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"---------------------
                 #第二行
                
    
                
                
                if len(receive_bin) != 0:
                    index_receive_bin = list(receive_bin.keys())
                    back_index_bin = len(index_receive_bin)-1
                    line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                    receive_bin.update(pass_card)#----------
                   
                    line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                    #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
    
           
                    
    
                
                
                receive_bin.update(pass_card)    
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                
               
                step_next_cards.update(set_1[step_1])#--------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                
    
        
            #elif len(pass_card) == width_1:
                
            else: 
                
    
                
                
    
                if len(receive_bin) != 0:
                    index_receive_bin = list(receive_bin.keys())
                    back_index_bin = len(index_receive_bin)-1
                    line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                    
    
    
                
                step_next_cards.update(set_1[step_1])#---------------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                
            
        else:   #牌无ace
            set_line_4[step_1] = ' '*width_1
            
    
            
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
            pass_card_face = [' '*12*step_1 + line_3_2]
            #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"
          
            
            
            
            if len(receive_bin) != 0:
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                    
                
                #receive_bin.update(pass_card)#---------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                
                
           
           
            
            receive_bin.update(pass_card)#-----------
            index_receive_bin = list(receive_bin.keys())
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
            
            
    shuffle_cards = {}#----2
    shuffle_index = list(step_next_cards.keys())
    reversed_index = list(reversed(shuffle_index))
    
    shuffle_cards = {k: new_cards[k] for k in reversed_index}
    
    step_2_1 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%3==0}
    step_2_2 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%3==1}
    step_2_3 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%3==2}
    line_3_1 = ''.join(step_2_1[i][0] for i in step_2_1)
    line_3_2 = ''.join(step_2_2[i][0] for i in step_2_2)
    line_3_3 = ''.join(step_2_3[i][0] for i in step_2_3)
    

    set_2 = [step_2_1, step_2_2, step_2_3]
    set_line_3 = [f"{line_3_1:<{width_1}}", f"{line_3_2:<{width_1}}", line_3_3]#显示扑克牌
    
    
   
    width_2 = [len(line_3_1), len(line_3_2),len(line_3_1)]
    
    
    
    step_next_cards = {}# 下阶段牌
    pass_card_face = [] # 面朝上pass牌
    line_step_next = ''#---------
    for step_2 in range(3):
        pass_card = {}
        #阶段1 ，第一堆扑克
        face_up_1 = list(set_2[step_2].keys())
        for i in face_up_1:
            if  i not in [0, 8, 16, 24]:
                pass_card[i] = set_2[step_2].pop(i)
            else:
                break
        len_save = len(set_2[step_2])
        
        #step_next_cards.update(set_2[step_2])##元素复制到下一步的牌堆里
        #receive_bin.update(pass_card)##元素复制到丢弃的牌堆里
        
        
        index_step1 = list(reversed(set_2[step_2].keys()))
        if len(set_2[step_2]) > 0:
            
            
            back_index_1 = len(index_step1)-1        
            line_3_1 = ''.join(list(set_2[step_2][i][1] for i in index_step1[:back_index_1]) +list((set_2[step_2][index_step1[-1]][2])))
            #重写第一行
            if step_2 != 2:   #-------                                                       
                set_line_3[step_2] = (f"{line_3_1:<{width_1}}")
            else:
                set_line_3[step_2] = line_3_1
            
            #set_line_3[step_2] = (f"{line_3_1:<{width_1}}")
            set_line_3[step_2] = " "*width_1
    
    
    
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            if len(pass_card) > 0:
                line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
                pass_card_face = [' '*12*step_2 + line_3_2]
                #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"---------------------
                
    
                
                
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                receive_bin.update(pass_card)#--------
    
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                
    
                    
    
    
    
                receive_bin.update(pass_card)#---------
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                
                step_next_cards.update(set_2[step_2])#--------
    
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
              
    
        
            #elif len(pass_card) == width_1:
                
            else:  #第一张是ace
                
    
    
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                
                step_next_cards.update(set_2[step_2])#------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
              
        else:    #牌无ace
            set_line_3[step_2] = ' '*width_1
            
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
            pass_card_face = [' '*12*step_2 +line_3_2]
    
            #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"
          
            
                
            index_receive_bin = list(receive_bin.keys())#--------
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
    
            line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
            #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )

            

            receive_bin.update(pass_card)#-----------
            index_receive_bin = list(receive_bin.keys())
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
 
    
    
    
    
    
    
    ## shuffle_cards = {}#----3
    shuffle_index = list(step_next_cards.keys())
    reversed_index = list(reversed(shuffle_index))
    
    shuffle_cards = {k: new_cards[k] for k in reversed_index}
    
    step_3_1 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%2==0}
    step_3_2 = {i : shuffle_cards[i] for j,(i,v) in enumerate(shuffle_cards.items()) if j%2==1}
    line_4_1 = ''.join(step_3_1[i][0] for i in step_3_1)
    line_4_2 = ''.join(step_3_2[i][0] for i in step_3_2)
    

    set_2 = [step_3_1, step_3_2]
    set_line_3 = [f"{line_4_1:<{width_1}}", line_4_2]#显示扑克牌
    
    
    width_2 = [len(line_4_1), len(line_4_2)]
    
    
    
    step_next_cards = {}# 下阶段牌
    pass_card_face = [] # 面朝上pass牌
    line_step_next = ''#--------
    for step_3 in range(2):
        pass_card = {}
        #阶段1 ，第一堆扑克
        face_up_1 = list(set_2[step_3].keys())
        for i in face_up_1:
            if  i not in [0, 8, 16, 24]:
                pass_card[i] = set_2[step_3].pop(i)
            else:
                break
        len_save = len(set_2[step_3])
        
        #step_next_cards.update(set_2[step_3])##元素复制到下一步的牌堆里
        #receive_bin.update(pass_card)##元素复制到丢弃的牌堆里
        
        
        index_step1 = list(reversed(set_2[step_3].keys()))
        if len(set_2[step_3]) > 0:
            
            
            back_index_1 = len(index_step1)-1
            line_3_1 = ''.join(list(set_2[step_3][i][1] for i in index_step1[:back_index_1]) +list((set_2[step_3][index_step1[-1]][2])))
            #重写第一行
    
            if step_3 != 1:   #-------                                                       
                set_line_3[step_3] = (f"{line_3_1:<{width_1}}")
            else:
                set_line_3[step_3] = line_3_1
    
            
            #set_line_3[step_3] = (f"{line_3_1:<{width_1}}")
            set_line_3[step_3] = " "*width_1
    
    
    
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            if len(pass_card) > 0: #牌堆有ace
                
                line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
                pass_card_face = [' '*12*step_3 + line_3_2]
                #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"---------------------
               
                
    
                
                if receive_bin:
                    index_receive_bin = list(receive_bin.keys())
                    back_index_bin = len(index_receive_bin)-1
                    line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                    receive_bin.update(pass_card)#--------
    
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                
    
                
                
                
                    
    
    
    
                
                
                
                receive_bin.update(pass_card)#---------
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                
                step_next_cards.update(set_2[step_3])#--------
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                
    
        
            #elif len(pass_card) == width_1:
                
            else:#第一章是ace
               
                
    
    
                index_receive_bin = list(receive_bin.keys())
                back_index_bin = len(index_receive_bin)-1
                line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
                
    
                step_next_cards.update(set_2[step_3])
                line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
                #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
                
            
        else:
            if step_3 != 1:
                set_line_3[step_3] = ' '*width_1
            
    
            index_pass_card = list(pass_card.keys())
            back_index_2 = len(index_pass_card)-1
            line_3_2 = ''.join(list(pass_card[i][1] for i in index_pass_card[:back_index_2]) +list((pass_card[index_pass_card[-1]][2])))
            pass_card_face = [' '*12*step_3 +line_3_2]
    
            #pass_card_face.append(line_3_2)#' '*(width_1) + f"{line_3_2:<{width_1}}"
            
            index_receive_bin = list(receive_bin.keys())#--------
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
            
            line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
            #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
    
            
            
            receive_bin.update(pass_card)#-----------
            index_receive_bin = list(receive_bin.keys())
            back_index_bin = len(index_receive_bin)-1
            line_receive_bin = ''.join(list(receive_bin[i][1] for i in index_receive_bin[:back_index_bin]) +list((receive_bin[index_receive_bin[-1]][2])))#丢弃牌堆
    
            
            line_step_next = ''.join(step_next_cards[i][0] for i in step_next_cards)
            #line_1 = ''.join(unicode_cards[i][0] for i in range(len(unicode_cards)) )
            
    
    
            
    









    

    final_keys = list(step_next_cards.keys())
    if len(final_keys) == 4:
        return 4
    for i in range(len(final_keys) - 3):
        if set(final_keys[i:i+4]) == {0, 8, 16, 24}:
            return len(final_keys)
    return 0
    




    
def simulate(n, i):
    result_count = defaultdict(int)

    for k in range(n):
        seed_val = i + k
        cards_left = play_one_game_silent(seed_val)
        if cards_left is not None and cards_left > 0:
            result_count[cards_left] += 1

    print("Number of cards left when winning | Frequency")
    print("-" * 45)

    total = n #sum(result_count.values())
    for cards_left in sorted(result_count):
        freq = result_count[cards_left] / total
        if freq > 0:
            percentage = f"{freq * 100:.2f}%"
            print(f"{cards_left:>32} | {percentage:>8}")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        i = int(sys.argv[2])
        simulate(n, i)
    else:
        L = int(input("Please enter an integer to feed the seed() function: "))
        play_one_game(L)
