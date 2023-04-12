# from app import SlotMachine
import art
from casino import Casino
from slot_machine_play import SlotMachine

machine = SlotMachine()
casino = Casino("SkyWinnings", "New York")
print(f'--->>> WELCOME, WELCOME\n          to\n {casino.name},\n The {casino.city} city best place for casino slot games! <<<---\n')

insert_money = int(input('Please, insert virtual money to your account: '))
machine.add_money(insert_money)
print(f'{"🍀"*35}{art.message}{"🍀"*35}\n')

enter_action = input('Press enter to continue...')
print(f'--->>> The sky is the limit of virtual money. Can you reach it now? <<<---')
answer = input('Please, enter Yes/No:   ').lower()
if answer == 'no':
    print('Dream on and bet!')

while machine.balance > 0:
    machine.play()
