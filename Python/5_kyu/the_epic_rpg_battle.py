'''
[ The epic RPG battle ]

Task
Your task is to create a class called Battle and also the characters that will be part of the battle.
The class should take two of these character objects when initialized and include a method named play_turn to handle the actions taken during each turn.
The characters have attributes and abilities and you should implemente them according to the descriptions provided below.

There are three character classes Warrior, Mage, Assassin:
🛡️ Warrior 
  - Attributes
      HP = 260
      Power = 40  
  - Abilities 
      Iron Skin: Reduce damage of the next attack received in 50% and regenerate your health by 40 points. (buff)       
      Blade Storm: Attacks with a power of 75 points.(special attack)  

🧙 Mage 
  - Attributes
      HP = 200
      Power = 50
  - Abilities
      Arcane Shield: Absorb the next damage received. (buff)
      Fireball: Attacks with a power of 90 points.(special attack) 

🗡️ Assassin
    - Attributes
        HP = 235
        Power = 30
    - Abilities
        Assassin's instinct: Increases your power by 40 points for three attacks. (buff)
        Lacerate: Inflicts the equivalent of 2x your power points. (special attack)
        
Obs.: HP Abbreviation for Hit Points or Health Points, this attribute indicates how many life points the player has.
The characters can execute one of the three actions per turn:

Buff, temporary effects that enhance attributes or abilities.
Normal attack, inflicting damage equals to the attack power (assassins can modify this value).
Special attack, an ability that deals more damage than normal.
These actions are will be indicated by a Enum:

class Actions(Enum):
    BUFF = 1
    NORMAL_ATTACK = 2
    SPECIAL_ATTACK = 3 
The test cases will call the method play_turn, and two of these constants will be passed as arguments.
The first (act_1) must correspond to the action of the first character passed when instantiating the Battle object, and the second (act_2) for the second character.

The first character executes their action first, giving them an advantage in the battle.

Furthermore the characters maybe receive damage originating of your adversary, and you must implement this taking into account each character's abilities and attributes.

Examples:
beowulf = Warrior()
merlin = Mage()
epic_battle = Battle(beowulf, merlin)

# 1: epic_battle.play_turn(Actions.NORMAL_ATTACK, Actions.NORMAL_ATTACK) 
# 2: epic_battle.play_turn(Actions.NORMAL_ATTACK, Actions.BUFF) 
# 3: epic_battle.play_turn(Actions.SPECIAL_ATTACK, Actions.SPECIAL_ATTACK) 

Here beowulf and merlin lose hp (Warrior HP = 210, Mage HP = 160).
Now only merlin loses hp, beowulf hits first, merlin conjures arcane shield after (Warrior HP = 210, Mage HP = 120).
Now merlin absorbes damage and uses special attack, beowulf loses hp (Warrior HP = 120, Mage HP = 120).
Returns
After completing the characters' actions, the method play_turn must return:

The winning character with your current HP when the opponent's HP is reduced to 0 this turn, examples: "The Warrior won! Remaining HP = 50", "The Mage won! Remaining HP = 30" or "The Assassin won. Remaining HP = 95".
"This battle is over!" for other play_turn calls after one of the characters has their hp reduced to 0.
In the other cases, the only respective hp of the classes after the actions: "Warrior HP = 210, Mage HP = 160"

Some Rules and Considerations
1. The warrior does not regenerate more than his maximum hp, in this case 260.
2. The only way for a warrior or mage to lose their buff effects is by suffering an attack from the opponent, whether normal or special.
3. The shield of mage absorbes only one attack, after that, the shield will be consumed.
4. In a similar way, iron skin of warrior, reduces only one attack.
5. Remember that the assassin increases his power, and this influences the damage of the lacerate and normal attack. 
6. Assassin's instinct lasts for three attacks, and each attack consumes one charge.
7. Buffs do not stack, for example: The wizard cannot have more than one shield, and the assassin cannot have more than 3 charges.
However, if the assassin uses assassin's instinct while he still has charges remaining, they will be renewed.
The warrior can heal whenever he uses iron skin, even if its effect is active.
8. Consider only the integer part when performing calculations.

Good Coding =)
'''




# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
