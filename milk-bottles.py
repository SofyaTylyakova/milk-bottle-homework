def cycle_milk_poem(bottles):
    for bottle in reversed(range(bottles)): 
        if bottle > 20 :
            print(dynamic_helper(bottle))
        elif bottle < 21 and bottle > 4:
             print('%d бутылок на борту...'%(bottle))
             print('берешь одну, пускаешь ко дну')  
             print('%d осталось на борту'%(bottle - 1))
        elif bottle < 5 and bottle > 0:
            print(dynamic_helper(bottle))
        else: 
            print('Нет бутылок молока на борту!\nПойди в магазин и стяни ещё!\n99 бутылок молока на борту!')


def dynamic_helper(bottle):
    bottles_in_string = str(bottle)
    last_symbols = create_last_symbols(int(bottles_in_string[-1]))
    return'%d бутыл%s на борту...\nберешь одну, пускаешь ко дну\n%d осталось на борту'%(bottle, last_symbols, bottle - 1)


def create_last_symbols(bottle):
    match bottle:
        case 1:
            return 'кa'
        case 2 | 3 | 4:
            return 'ки'
        case default:
            return 'ок'
        
cycle_milk_poem(100)
