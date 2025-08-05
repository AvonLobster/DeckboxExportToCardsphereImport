import sys
import csv

# Constants
CSV_NAME = 4
CSV_EDITION = 5
CSV_CARD_NUM = 7
CSV_CONDITION = 8
CSV_FOIL = 10
CSV_PRINTING_ID = 17
CSV_PRINTING_NOTE = 18

DROP_CARD = 'DROP_CARD'

def process_name(name, edition, card_num):
    name = name.replace('"', '') # Remove quoted card name. CS doesn't like quotes.

    # Alliances, Fallen Empires, Homelands, and Portal variants
    if edition == 'Alliances' or edition == 'Homelands' or edition == 'Fallen Empires' or edition == 'Portal':
        if name == 'Abbey Matron':
            name += ' (Hood)' if card_num == '102' else ' (No Hood)'
        elif name == 'Aesthir Glider':
            name += ' (Facing Left)' if card_num == '156' else ' (Facing Right)'
        elif name == 'Agent of Stromgald':
            name += ' (Staff)' if card_num == '94' else ' (Doorway)'
        elif name == 'Aliban\'s Tower':
            name += ' (Horses)' if card_num == '76' else ' (Glowing)'
        elif name == 'Ambush Party':
            name += ' (Doorway)' if card_num == '79' else ' (Mountain)'
        elif name == 'Anaba Bodyguard':
            name += ' (Alone)' if card_num == '83' else ' (With Human)'
        elif name == 'Anaconda':
            name += ' (Flavor text)' if card_num == '82' else ' (No flavor text)'
        elif name == 'Armor Thrull':
            if card_num == '1':
                name += ' (Pete Venters)'
            elif card_num == '2':
                name += ' (Ron Spencer)'
            elif card_num == '3':
                name += ' (Jeff A. Menges)'
            else:
                name += ' (Scott Kirschner)'
        elif name == 'Astrolabe':
            name += ' (Close-up)' if card_num == '160' else ' (Full Room View)'
        elif name == 'Awesome Presence':
            name += ' (Open Arms)' if card_num == '34' else ' (Man Being Attacked)'
        elif name == 'Aysen Bureaucrats':
            name += ' (Two Men)' if card_num == '104' else ' (One Man)'
        elif name == 'Balduvian War-Makers':
            name += ' (Sky Background)' if card_num == '97' else ' (Green Background)'
        elif name == 'Basal Thrull':
            if card_num == '5':
                name += ' (Kaja Foglio)'
            elif card_num == '6':
                name += ' (Phil Foglio)'
            elif card_num == '7':
                name += ' (Richard Kane-Ferguson)'
            else:
                name += ' (Christopher Rush)'
        elif name == 'Goblin Chirurgeon':
            if card_num == '110':
                name += ' (Daniel Gelon)'

    # Guildgates
    if edition == 'Ravnica Allegiance' or edition == 'Guilds of Ravnica':
        if name.endswith('Guildgate'):
            name += ' (#' + card_num + ')'

    # Duel Decks
    if edition == 'Duel Decks Anthology, Garruk vs. Liliana':
        if name == 'Corrupt':
            name = 'Corrupt (Garruk vs. Liliana)'
        elif name == 'Forest':
            name = 'Forest (#' + card_num + ') (Garruk vs. Liliana)'
    elif edition == 'Duel Decks Anthology, Divine vs. Demonic':
        if name == 'Corrupt':
            name = 'Corrupt (Divine vs. Demonic)'
    elif edition == 'Duel Decks Anthology, Elves vs. Goblins':
        if name == 'Flamewave Invoker':
            name = 'Flamewave Invoker (Elves vs. Goblins)'
        elif name == 'Forest':
            name = 'Forest (#' + card_num + ') (Elves vs. Goblins)'
    elif edition == 'Duel Decks Anthology, Jace vs. Chandra':
        if name == 'Flamewave Invoker':
            name = 'Flamewave Invoker (Jace vs. Chandra)'


    # Un variants
    if edition == 'Unstable' or edition == 'Unglued':
        if name == 'B.F.M. (Big Furry Monster Left)':
            name = 'B.F.M. (Big Furry Monster) (left)'
        elif name == 'B.F.M. (Big Furry Monster Right)':
            name = 'B.F.M. (Big Furry Monster) (right)'
    elif edition == 'Unfinity':
        if name == 'Centrifuge':
            name = 'Centrifuge (4/6)'

    # Tokens
    if edition.startswith('Extras'):
        # Not quite a token
        if name == 'Experience':
            name = 'Experience Counter'
        # Cardsphere unique names
        # A
        elif edition == 'Extras: Adventures in the Forgotten Realms':
            if name == 'Goblin // Dungeon of the Mad Mage':
                name = 'Dungeon of the Mad Mage Dungeon | Goblin Token'
            elif name == 'Skeleton // Lost Mine of Phandelver':
                name = 'Lost Mine of Phandelver Dungeon | Skeleton Token'
            elif name == 'The Atropal // Tomb of Annihilation':
                name = 'The Atropal Token | Tomb of Annihilation Dungeon'
            else:
                name += ' Token'
        elif edition == 'Extras: Avacyn Restored':
            if name == 'Angel // Demon':
                name = 'Angel Token | Demon Token (Helvault) (Double-Sided)'
            elif name == 'Human':
                name = 'Human Token (Red)'
            elif name == 'Spirit':
                name = 'Spirit Token (Blue)'
            else:
                name += ' Token'
        #C
        elif edition == 'Extras: Commander 2015':
            if ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander 2016':
            if name == 'Saproling // Saproling':
                name = 'Saproling Token (#16) (#17)'
            elif name == 'Zombie // Worm':
                name = 'Worm Token | Zombie Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander 2017':
            if name == 'Cat // Cat Warrior':
                name = 'Cat Token | Cat Warrior Token'
            elif name == 'Dragon // Gold':
                name = 'Dragon Token | Gold Token (4/4)'
            elif name == 'Rat // Cat Warrior':
                name = 'Cat Warrior Token | Rat Token'
            elif name == 'Zombie // Gold':
                name = 'Gold Token | Zombie Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander 2018':
            if name == 'Clue // Construct':
                name = 'Clue Token | Construct Token (6/12)'
            elif name == 'Construct // Myr':
                name = 'Construct Token (4/4) (2/1)'
            elif name == 'Token: Dragon Egg // Dragon':
                name = 'Dragon Token | Dragon Egg'
            elif name == 'Myr // Thopter':
                if int(card_num) == 35:
                    name = 'Myr Token (2/1) (#8)'
                else:
                    name = 'Myr Token (1/1) (#25)'
            elif name == 'Servo // Thopter':
                name = 'Servo Token | Thopter Token (#25)'
            elif name == 'Survivor // Myr':
                name = 'Myr Token | Survivor Token (1/1)'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander 2019':
            if name == 'Angel of Sanctions // Horror':
                name = 'Angel of Sanctions Token | Horror Token'
            elif name == 'Assassin // Morph':
                name = 'Assassin Token | Morph Token'
            elif name == 'Beast // Wurm':
                name = 'Beast Token | Wurm Token (3/3)'
            elif name == 'Bird // Sculpture':
                if card_num == '30':
                    name = 'Bird Token | Sculpture Token (3/4)'
                else:
                    name = 'Bird Token | Sculpture Token (3/3)'
            elif name == 'Centaur // Egg':
                name = 'Centaur Token | Egg Token'
            elif name == 'Eldrazi // Egg':
                name = 'Egg Token | Eldrazi Token'
            elif name == 'Emblem: Ob Nixilis Reignited // Zombie':
                name = 'Ob Nixilis Emblem | Zombie Token (#10)'
            elif name == 'Gargoyle // Egg':
                name = 'Egg Token | Gargoyle Token'
            elif name == 'Heart-Piercer Manticore // Dragon':
                name = 'Dragon Token | Heart-Piercer Manticore Token'
            elif name == 'Plant // Morph':
                name = 'Morph Token | Plant Token'
            elif name == 'Plant // Snake':
                name = 'Plant Token | Snake Token'
            elif name == 'Rhino // Egg':
                name = 'Egg Token | Rhino Token'
            elif name == 'Saproling // Manifest':
                name = 'Manifest Token | Saproling Token'
            elif name == 'Saproling // Morph':
                name = 'Morph Token | Saproling Token'
            elif name == 'Spirit // Human':
                name = 'Human Token | Spirit Token '
            elif name == 'Treasure // Human':
                name = 'Human Token | Treasure Token'
            elif name == 'Zombie // Zombie':
                name = 'Zombie Token | Zombie Token (#10) (#11)'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander 2020':
            if name == 'Angel // Elemental':
                name = 'Angel Token | Elemental Token (Red)'
            elif name == 'Bird Illusion // Beast':
                name = 'Beast Token | Bird Illusion Token'
            elif name == 'Drake // Insect':
                name = 'Drake Token | Insect Token (Blue/Red)'
            elif name == 'Human Soldier // Drake':
                name = 'Drake Token | Human Soldier Token (#05)'
            elif name == 'Ability Punchcard':
                name = 'Punch Card'
            elif name == 'Human Soldier // Zombie':
                name = DROP_CARD
            elif name == 'Hydra // Beast':
                name = DROP_CARD
            elif name == 'Spirit // Insect':
                name = ' Insect Token | Spirit Token (Green)'
            elif name == 'Treasure // Human':
                name = 'Human Token | Treasure Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander Masters':
            if name == 'Assassin // Servo':
                name = 'Assassin Token | Servo Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Conspiracy: Take the Crown':
            if name == 'Soldier':
                name = 'Soldier Token (1/1)'
            else:
                name += ' Token'
        #D
        elif edition == 'Extras: Dominaria':
            if name == 'Knight':
                name = 'Knight Token (#' + card_num +')'
            elif name == 'Saproling':
                name = 'Saproling Token (#' + card_num + ')'
            else:
                name += ' Token'
        elif edition == 'Duel Decks: Zendikar vs. Eldrazi':
            if name == 'Hellion':
                name = 'Hellion Token'
        #E
        elif edition == 'Extras: Eternal Masters':
            if name == 'Elemental':
                name = 'Elemental Token (Blue/Red)'
            elif name == 'Spirit':
                if int(card_num) == 1:
                    name = 'Spirit Token (Colorless)'
                else:
                    name = 'Spirit Token (White)'
            else:
                name += ' Token'
        elif edition == 'Extras: Explorers of Ixalan':
            if name == 'Saproling // Treasure':
                if int(card_num) == 4:
                    name = 'Saproling Token | Treasure Token (#7)'
                else:
                    name = 'Saproling Token | Treasure Token (#10)'
        #F
        elif edition == 'Extras: Fallout':
            if name == 'Copy // Clue':
                name = 'Clue Token | Copy Token'
            elif name == 'Energy Reserve // Treasure':
                name = 'Energy Reserve | Treasure Token'
            elif name == 'Human Knight // Copy':
                name = 'Copy Token | Human Knight Token'
            elif name == 'Human Knight // Food':
                name = 'Food Token | Human Knight Token'
            elif name == 'Radiation // Copy':
                name = 'Copy Token | Radiation Token'
            elif name == 'Radiation // Zombie Mutant':
                name = 'Radiation | Zombie Mutant Token'
            elif name == 'Settlement // Human Soldier':
                name = 'Human Soldier Token | Settlement Token'
            elif name == 'Soldier // Human Soldier':
                name = 'Human Soldier Token | Soldier Token'
            elif name == 'Squirrel // Food':
                name = 'Food Token | Squirrel Token'
            elif name == 'Treasure // Human Knight':
                name = 'Human Knight Token | Treasure Token'
            elif name == 'Warrior // Soldier':
                name = 'Soldier Token | Warrior Token'
            elif name == 'Zombie Mutant // Clue':
                name = 'Clue Token | Zombie Mutant Token'
            elif name == 'Zombie Mutant // Copy':
                name = 'Copy Token | Zombie Mutant Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        #I
        elif edition == 'Extras: Ixalan':
            if name == 'Treasure':
                name = 'Treasure Token (#' + card_num + ')'
            else:
                name += ' Token'
        #K
        elif edition == 'Extras: Khans of Tarkir':
            if name == 'Warrior':
                name = 'Warrior Token (#' + card_num + ')'
            else:
                name += ' Token'
        #M
        elif edition == 'Extras: Magic 2011':
            if name == 'Ooze':
                name = 'Ooze Token (2/2)'
            else:
                name += ' Token'
        elif edition == 'Extras: Magic 2015 Core Set':
            if name == 'Wolf':
                name = 'Wolf Token (Prerelease Promo)'
            else:
                name += ' Token'
        elif edition == 'Extras: Magic Origins':
            if name == 'Thopter':
                name = 'Thopter Token (#' + card_num + ')'
            else:
                name += ' Token'
        elif edition == 'Extras: Mirrodin Besieged':
            if name == 'Poison Counter':
                name = name
            else:
                name += ' Token'
        elif edition == 'Extras: Murders at Karlov Manor':
            if name == 'Ability Punchcard':
                name = 'Punch Card | Punch Card'
            else:
                name += ' Token'
        elif edition == 'Extras: Murders at Karlov Manor Commander':
            if name == 'City\'s Blessing // Human Soldier':
                name = 'City\'s Blessing | Human Soldier Token'
            elif name == 'Drake // Cat':
                name = 'Cat Token | Drake Token'
            elif name == 'Insect // Clue':
                name = 'Clue Token | Insect Token'
            elif name == 'Tentacle // Koma\'s Coil':
                name = 'Koma\'s Coil Token | Tentacle Token'
            elif name == 'Thopter // Rhino Warrior':
                name = 'Rhino Warrior Token | Thopter Token (1/1)'
            elif name == 'Thopter // Treasure':
                name = 'Thopter Token | Treasure Token (1/1)'
            elif name == 'Tiny // Eldrazi':
                name = 'Eldrazi Token | Tiny Token'
            elif name == 'Zombie // City\'s Blessing':
                name = 'City\'s Blessing | Zombie Token'
            elif name == 'Zombie // Salamander Warrior':
                name = 'Salamander Warrior Token | Zombie Token'
            elif name == 'Merfolk // Detective':
                name = 'Detective Token | Merfolk Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        #O
        elif edition == 'Extras: Outlaws of Thunder Junction Commander':
            if name == 'Bounty: Rissa Blades Lee // Bounty Rules':
                name = 'Bounty: Rissa "Blades" Lee'
            elif name.startswith('Bounty:'):
                name = name.split(' // ')[0]
            elif name == 'Dragon Elemental // Bird Illusion':
                name = 'Bird Illusion Token | Dragon Elemental Token'
            elif name == 'Soldier // Drake':
                name = 'Drake Token | Soldier Token'
            elif name == 'Soldier // Elemental':
                name = 'Elemental Token | Soldier Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        #P
        elif edition == 'Extras: Phyrexia: All Will Be One':
            if name == 'Emblem: Koth, Fire of Resistance':
                name = 'Koth, Fire of Resistance Emblem'
            elif name == 'Phyrexian Goblin // Poison Counter':
                name = 'Phyrexian Goblin Token | Poison Counter'
            elif name == 'Phyrexian Mite // Phyrexian Mite':
                name = 'Phyrexian Mite Token | Phyrexian Mite Token'
            elif name == 'Rebel // Phyrexian Goblin':
                name = 'Phyrexian Goblin Token | Rebel Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Planechase Anthology':
            if name == 'Ooze // Ooze':
                name = 'Ooze Token (1/1) (2/2)'
            elif name == 'Ooze // Plant':
                name = 'Ooze Token | Plant Token (1/1)'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        #S
        elif edition == 'Extras: Scars of Mirrodin':
            if name == 'Poison Counter':
                name = name
            else:
                name += ' Token'
        #T
        elif edition == 'Extras: Throne of Eldraine':
            if name == 'Food':
                name = 'Food Token (#' + card_num + ')'
            else:
                name += ' Token'
        elif edition == 'Extras: Throne of Eldraine Foil Double Sided':
            if name == 'Bear // Food':
                name = 'Bear Token | Food Token'
                if card_num == '29':
                    name += ' (#15)'
                elif card_num == '30':
                    name += ' (#16)'
                elif card_num == '31':
                    name += ' (#17)'
                else:
                    name += ' (#18)'
        elif edition == 'Extras: Duel Decks: Garruk vs. Liliana':
            if name == 'Beast':
                name = 'Beast Token (3/3)'
        elif edition == 'Extras: Commander Anthology':
            if name == 'Beast':
                name = 'Beast Token (3/3)'
            elif name == 'Wolf':
                name = 'Wolf Token (#' + card_num + ')'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander Anthology Volume II':
            if name == 'Emblem: Daretti, Scrap Savant':
                name = 'Daretti Emblem'
            elif name == 'Wurm':
                if int(card_num) == 16:
                    name = 'Wurm Token (Deathtouch)'
                else:
                    name = 'Wurm Token (Lifelink)'
            else:
                name += ' Token'
        elif edition == 'Extras: The Lord of the Rings: Tales of Middle-earth':
            if name == 'Food':
                name = 'Food Token (#009)'
            elif name == 'Human Soldier':
                name = 'Human Soldier Token (#00' + card_num + ')'
            else:
                name += ' Token'
        elif edition == 'Extras: Modern Horizons 2':
            if name == 'Beast // Clue':
                #name = 'Beast Token | Clue Token (#15)' Cardsphere only has this card in foil
                name = DROP_CARD
            elif name == 'Clue':
                #name = 'Clue Token (#014)' Cardsphere failed to categorize this with a MKM duplicate
                name = DROP_CARD
            elif name == 'Crab // Food':
                #name = 'Crab Token | Food Token (#18)' Cardsphere only has this card in foil
                name = DROP_CARD
            elif name == 'Food':
                #name = 'Food Token (#0' + card_num + ')' This looks like it perfectly matches CS' entry but it fails
                name = DROP_CARD
            elif name == 'Phyrexian Germ // Squirrel':
                name = DROP_CARD
            elif name =='Zombie Army // Thopter':
                name = DROP_CARD
            else:
                name += ' Token'
        elif edition == 'Extras: Modern Horizons 3':
            if name == 'Cat // Energy Reserve':
                name = 'Cat Token | Energy Reserve'
            elif name == 'Eldrazi Spawn // Energy Reserve':
                name = 'Eldrazi Spawn Token | Energy Reserve'
            elif name == 'Servo // Energy Reserve':
                name = 'Energy Reserve | Servo Token'
            elif name == 'Zombie // Energy Reserve':
                name = 'Energy Reserve | Zombie Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Modern Horizons 3 Commander':
            if name == 'Copy // Eldrazi Angel':
                name = 'Copy Token | Eldrazi Angel Token'
            elif name == 'Eldrazi Spawn // Eldrazi Scion':
                name = 'Eldrazi Scion Token | Eldrazi Spawn Token'
            elif name == 'Shapeshifter // Copy':
                name = 'Copy Token | Shapeshifter Token'
            elif name == 'Dragon // Copy':
                name = 'Copy Token | Dragon Token'
            elif name == 'Saproling // Emblem: Garruk, Apex Predator':
                name = 'Garruk, Apex Predator Emblem | Saproling Token'
            elif name == 'Shapeshifter // Dragon':
                name = 'Dragon Token | Shapeshifter Token'
            elif name == 'Tarmogoyf // Goblin':
                name = 'Goblin Token | Tarmogoyf Token'
            elif name == 'Tarmogoyf // Saproling':
                name = 'Saproling Token | Tarmogoyf Token'
            elif name == 'Thopter // Copy':
                name = 'Copy Token | Thopter Token'
            elif name == 'Copy // Beast':
                name = 'Beast Token | Copy Token (4/4)'
            elif name == 'Zombie // Elephant':
                name = 'Elephant Token | Zombie Token'
            elif name == 'Beast // Elephant':
                name = 'Beast Token | Elephant Token (4/4)'
            elif name == 'Beast // Insect':
                name = 'Beast Token | Insect Token (3/3)'
            elif name == 'Forest Dryad // Emblem: Vivien Reid':
                name = 'Forest Dryad Token | Vivien Reid Emblem'
            elif name == 'Hydra // Boar':
                name = 'Boar Token | Hydra Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Unsanctioned':
            if name == 'Beeble // Dragon':
                name = 'Beeble Token | Dragon Token'
            elif name == 'Beeble // Squirrel':
                name = 'Beeble Token | Squirrel Token'
            elif name == 'Goblin // Giant Teddy Bear':
                name = 'Giant Teddy Bear Token | Goblin Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Born of the Gods':
            if name == 'Bird':
                name = 'Bird Token (Blue)'
        elif edition == 'Extras: Shadows over Innistrad':
            if name == 'Clue':
                name = 'Clue Token (#' + card_num + ')'
            elif name == 'Checklist':
                if card_num == '19':
                    name = 'Checklist Card (CH1) (Common/Uncommon)'
                else:
                    name = 'Checklist Card (CH2) (Rare/Mythic)'
            else:
                name += ' Token'
        elif edition == 'Extras: Guilds of Ravnica':
            if name == 'Emblem: Ral, Izzet Viceroy':
                name = 'Ral Emblem'
            else:
                name += ' Token'
        elif edition == 'Extras: Kaladesh':
            if name == 'Energy Reserve':
                name = 'Energy Reserve'
            elif name == 'Servo':
                name = 'Servo Token (#' + card_num + ')'
            elif name == 'Thopter':
                name = 'Thopter Token (#' + card_num + ')'
            else:
                name += ' Token'
        elif edition == 'Extras: Kaldheim':
            if name == 'Emblem: Tyvar Kell':
                name = 'Tyvar Emblem'
            elif name == 'Foretell':
                name += '' # Do nothing
            else:
                name += ' Token'
        elif edition == 'Extras: Ikoria: Lair of Behemoths':
            if name == 'Companion':
                pass
            elif name == 'Emblem: Narset of the Ancient Way':
                name = 'Narset Emblem'
            elif name == 'Ability Punchcard':
                name = 'Punch Card'
            elif name == 'Human Soldier':
                name = 'Human Soldier Token (#0' + card_num + ')'
            else:
                name += ' Token'
        elif edition == 'Extras: Innistrad: Midnight Hunt':
            if name == 'Double-Faced Card Placeholder':
                db_weirdness = str(int(card_num) - 79)
                name = 'Helper Card (#' + db_weirdness + ')'
            elif name == 'Day // Night':
                name = 'Day | Night (Token)'
            else:
                name += ' Token'
        elif edition == 'Extras: Innistrad: Crimson Vow':
            if name == 'Day // Night':
                name = 'Day | Night (Token)'
            elif name == 'Emblem: Chandra, Dressed to Kill':
                name = 'Chandra Emblem'
            else:
                name += ' Token'
        elif edition == 'Extras: Iconic Masters':
            if name == 'Dragon':
                if card_num == '5':
                    name = 'Dragon Token (2/2)'
                else:
                    name = 'Dragon Token (5/5)'
            else:
                name += ' Token'
        elif edition == 'Extras: Core Set 2019':
            if name == 'Dragon':
                name = 'Dragon Token (#9)'
            else:
                name += ' Token'
        elif edition == 'Extras: Core Set 2020':
            if name == 'Emblem: Mu Yanling, Sky Dancer':
                name = 'Mu Yanling Emblem'
            else:
                name += ' Token'
        elif edition == 'Extras: Battle for Zendikar':
            if name == 'Eldrazi Scion':
                name = 'Eldrazi Scion Token (#' + card_num + ')'
            elif name == 'Elemental':
                name = 'Elemental Token (Red)'
            elif name == 'Emblem: Gideon':
                name = 'Gideon Emblem'
            elif name == 'Emblem: Kiora, Master of the Depths':
                name = 'Kiora Emblem'
            else: 
                name += ' Token'
        elif edition == 'Extras: Oath of the Gatewatch':
            if name == 'Eldrazi Scion':
                name = 'Eldrazi Scion Token (#' + card_num + ')'
            elif name == 'Elemental':
                if card_num == '9':
                    name = 'Elemental Token (Red)'
                else:
                    name = 'Elemental Token (Green)'
            else: 
                name += ' Token'
        elif edition == 'Extras: Ravnica Allegiance':
            if name == 'Emblem: Domri, Chaos Bringer':
                name = 'Domri Emblem'
            else:
                name += ' Token'
        elif edition == 'Extras: War of the Spark':
            if name == 'Zombie Army':
                name = 'Zombie Army Token (#08)'
            else:
                name += ' Token'
        elif edition == 'Extras: The Brothers\' War':
            if name == 'Construct':
                if card_num == '4':
                    name = 'Construct Token (2/2)'
                else:
                    name = 'Construct Token (0/0)'
            elif name == 'Double-Faced Card Placeholder':
                name = 'Helper Card'
            elif name == 'Emblem: Saheeli, Filigree Master':
                name = 'Saheeli, Filigree Master Emblem'
            elif name == 'Ability Punchcard':
                name = DROP_CARD
            else:
                name += ' Token'
        elif edition == 'Extras: The Brothers\' War Commander':
            if name == 'Construct // Phyrexian Myr':
                name = 'Construct Token | Phyrexian Myr Token (1/1)'
            elif name == 'Goat // Construct':
                name = 'Construct Token | Goat Token (1/1)'
            elif name == 'Mishra\'s Warform // Inkling':
                name = 'Inkling Token | Mishra\'s Warform Token'
            elif name == 'Scrap // Powerstone':
                name = 'Powerstone Token | Scrap Token'
            elif name == 'Thopter // Faerie':
                name = 'Faerie Token | Thopter Token'
            elif name == 'Construct // Thopter':
                name = 'Construct Token | Thopter Token (*/*)'
            elif name == 'Powerstone // Faerie':
                name = 'Faerie Token | Powerstone Token'
            elif name == 'Powerstone // Myr':
                name = 'Myr Token | Powerstone Token'
            elif name == 'Scrap // Phyrexian Myr':
                name = 'Phyrexian Myr Token | Scrap Token'
            elif name == 'Servo // Eldrazi':
                name = 'Eldrazi Token | Servo Token'
            elif name == 'Servo // Powerstone':
                name = 'Powerstone Token | Servo Token'
            elif name == 'Thopter // Copy':
                name = 'Copy Token | Thopter Token'
            elif name == 'Construct // Servo':
                name = 'Construct Token | Servo Token (*/*)'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: March of the Machine':
            if name == 'Double-Faced Card Placeholder':
                name = 'Helper Card'
            elif name == 'Incubator // Phyrexian':
                name = 'Incubator Token | Phyrexian Token'
            else:
                name += ' Token'
        elif edition == 'Extras: The Lost Caverns of Ixalan':
            if name == 'Double-Faced Card Placeholder':
                name = 'Helper Card'
            elif name == 'Bat // Treasure':
                name = 'Bat Token | Treasure Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Streets of New Capenna':
            if name == 'Copy // Treasure':
                name = 'Copy Token | Treasure Token (#17)'
            else:
                name += ' Token'
        elif edition == 'Extras: Wilds of Eldraine':
            if name == 'Rat // Food':
                name = ' Food Token | Rat Token'
            elif ' // ' in name:
                two_sided_token = name.split(' // ')
                name = two_sided_token[0] + ' Token | ' + two_sided_token[1] + ' Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Zendikar Rising Commander':
            if name == 'Faerie Rogue // Goblin Rogue':
                #name = Faerie Rogue Token | Goblin Rogue Token -- Cardsphere does not have this card
                name = DROP_CARD
            elif name == 'Faerie Rogue // Rat':
                #name = Faerie Rogue Token | Rat Token -- Cardsphere does not have this card
                name = DROP_CARD
            elif name == 'Faerie Rogue // Thopter':
                #name = Faerie Rogue Token | Thopter Token
                name = DROP_CARD
            else:
                name += ' Token'
        elif edition == 'Extras: Ravnica Remastered':
            if name == 'Goblin':
                name = 'Goblin Token (1/1)'
            elif name == 'Emblem: Domri Rade':
                name = 'Domri Rade Emblem'
            else:
                name += ' Token'
        # Double-Faced Card Placeholders aka Helper Cards
        elif edition.endswith(' Placeholders'):
            name = 'Helper Card (#' + card_num + ')'
        else:
            name += ' Token'

        if name == 'Checklist Token':
            name = 'Checklist Card'

    # Two-faced cards
    if (edition == 'Innistrad: Midnight Hunt' 
        or edition == 'Innistrad: Crimson Vow' 
        or edition == 'Champions of Kamigawa' 
        or edition == 'Dark Ascension' 
        or edition == 'Zendikar Rising Commander' 
        or edition == 'Betrayers of Kamigawa' 
        or edition == 'Innistrad' 
        or edition == 'Shadows over Innistrad' 
        or edition == 'Eldritch Moon' 
        or edition == 'March of the Machine' 
        or edition == 'Wilds of Eldraine' 
        or edition == 'Innistrad: Double Feature' 
        or edition == 'Murders at Karlov Manor' 
        or edition == 'The Lost Caverns of Ixalan'
        or edition == "Commander Legends: Battle for Baldur's Gate"
        or edition == 'Throne of Eldraine'
        or edition == 'The List'):
        if ' // ' in name:
            name = name.split(' // ')[0]

    # Deckbox is stupid
    if edition == '':
        if name == 'Angel // Elemental':
            edition = 'Commander 2020'
            name = 'Angel Token | Elemental Token (Red)'
    elif edition == 'Duel Decks: Nissa vs. Ob Nixilis':
        if name == 'Eldrazi Scion' or name == 'Zombie Giant':
            name += ' Token'

    # Art cards
    if name.startswith('Art Card:'):
        return
    
    # Secret Lair
    if edition == 'Secret Lair Drop Series':
        if name.startswith('Walker'):
            if int(card_num) == 703 or int(card_num) == 704:
                name = 'Walker Token (Metal Head)'
            elif int(card_num) == 706:
                name = 'Walker Token (Bicycle Girl)'
            elif int(card_num) == 701 or int(card_num == 705):
                name = 'Walker Token (Well Walker)'
            elif int(card_num) == 702:
                name = 'Walker Token (Winslow)'
            else:
                name = 'Walker Token (Blade Walker)'

    # Plains
    if name == 'Plains':
        name += ' (#' + card_num + ')'

    # Island
    if name == 'Island':
        if edition == 'Mirage':
            name += ' (C)'
        elif edition == 'Amonkhet':
            if card_num == '251':
                name = 'Island (#251) (Full Art)'
        elif edition == 'Zendikar Rising':
            if card_num == '269':
                name = 'Island (#269) (Full Art)'
        else:
            name += ' (#' + card_num + ')'

    # Swamp
    if name == 'Swamp':
        name += ' (#' + card_num + ')'

    # Mountain
    if name == 'Mountain':
        name += ' (#' + card_num + ')'

    # Forest
    if name == 'Forest':
        if edition == 'Portal':
            name += ' (C)'
        elif edition == 'Portal Second Age':
            name += ' (B)'
        elif edition == 'Battlebond' or edition == 'Guilds of Ravnica':
            name += '' # Do nothing
        elif edition == 'Ixalan' or edition == 'Core Set 2020':
            if card_num == '278':
                name = 'Forest (#278) (Full Art)'
            else:
                name += ' (#' + card_num + ')'
        else:
            name += ' (#' + card_num + ')'


    # Misc
    if edition == 'Champions of Kamigawa' and name == 'Brothers Yamazaki':
        name = 'Brothers Yamazaki (#160a)'
    elif edition == 'The Lord of the Rings: Tales of Middle-earth':
        if int(card_num) == 6:
            name = 'Dunedain Blade'
        if int(card_num) == 10:
            name = 'Eowyn, Lady of Rohan'
        if int(card_num) == 134:
            name = 'Grishnakh, Brash Instigator'

    # Thick Stock
    if edition == 'Fallout':
        if int(card_num) >= 1064 and int(card_num) <= 1067:
            name = DROP_CARD

    # Archenemy
    if edition == 'Archenemy: Nicol Bolas':
        if name == 'My Laughter Echoes' or name == 'Power Without Equal' or name == 'When Will You Learn?' or name == 'Choose Your Demise':
            name = DROP_CARD

    # Clean up
    if name == DROP_CARD:
        name = None

    return name



def process_edition(edition, card_num, printing_id, printing_note):
    edition = edition.replace("Extras: ", "")
    edition = edition.replace(" Placeholders", "")

    # A
    if edition == 'Avacyn Restored (The Helvault Experience)':
        edition = 'Avacyn Restored'
    # B
    elif edition == 'Battlebond Promos':
        edition = 'Launch Promos'
    elif edition == 'Bloomburrow':
        if int(card_num) >= 282 and int(card_num) <= 286:
            edition = 'Bloomburrow - Borderless'
        elif int(card_num) >= 287 and int(card_num) <= 294:
            edition = 'Bloomburrow - Borderless Field Notes'
        elif int(card_num) >= 295 and int(card_num) <= 336:
            edition = 'Bloomburrow - Showcase'
        elif int(card_num) >= 341 and int(card_num) <= 342:
            edition = 'Bloomburrow - Borderless'
        elif int(card_num) >= 356 and int(card_num) <= 368:
            edition = 'Bloomburrow - Extended Art'
    elif edition == 'The Brothers\' War':
        if int(card_num) >= 293 and int(card_num) <= 300:
            edition = 'The Brothers\' War - Borderless'
        elif int(card_num) >= 301 and int(card_num) <= 377:
            edition = 'The Brothers\' War - Extended Art'
    elif edition == 'The Brothers\' War Commander':
        if int(card_num) in [2, 3, 11, 15]:
            edition = 'The Brothers\' War'
    elif edition == 'The Brothers\' War Retro Artifacts':
        if int (card_num) >= 64:
            edition = 'The Brothers\' War - Retro Artifacts (Schematic)'
        else:
            edition = 'The Brothers\' War - Retro Artifacts'
    elif edition == 'Dominaria Remastered':
        if int(card_num) >= 262 and int(card_num) <= 411:
            edition = 'Dominaria Remastered - Retro Frame'
    # F
    elif edition == 'Fallout':
        if int(card_num) >= 327 and int(card_num) <= 352:
            edition = 'Fallout - Showcase'
        elif int(card_num) >= 353 and int(card_num) <= 361:
            edition = 'Fallout - Borderless'
        elif int(card_num) >= 362 and int(card_num) <= 528:
            edition = 'Fallout - Extended Art'

    # G
    elif edition == 'Global Series: Jiang Yanggu and Mu Yanling':
        edition = 'Global Series: Jiang Yanggu & Mu Yanling'
    # I
    elif edition == 'Ikoria: Lair of Behemoths':
        if printing_note == 'Showcase':
            edition = 'Ikoria: Lair of Behemoths - Alternate Art'
    elif edition == 'Prerelease Events: Ikoria: Lair of Behemoths':
        edition = 'Ikoria: Lair of Behemoths Prerelease Promos'
    elif edition == 'Innistrad: Crimson Vow':
        if int(card_num) >= 278 and int(card_num) <= 285:
            edition = 'Innistrad: Crimson Vow - Borderless'
        elif int(card_num) >= 286 and int(card_num) <= 316:
            edition = 'Innistrad: Crimson Vow - Showcase Fang Frame'
        elif int(card_num) >= 317 and int(card_num) <= 328:
            edition = 'Innistrad: Crimson Vow - Showcase'
        elif int (card_num) >= 346 and int(card_num) <= 397:
            edition = 'Innistrad: Crimson Vow - Extended Art'
    elif edition == 'Innistrad: Midnight Hunt':
        if int(card_num) >= 278 and int(card_num) <= 379:
            edition = 'Innistrad: Midnight Hunt - Showcase'
    # K
    elif edition == 'Prerelease Events: Kaladesh':
        edition = 'Prerelease Promos'
    elif edition == 'Kaldheim':
        if int(card_num) >= 286 and int(card_num) <= 298:
            edition = 'Kaldheim - Alternate Art'
        elif int(card_num) >= 299 and int(card_num) <= 332:
            edition = 'Kaldheim - Showcase'
        elif int(card_num) >= 334 and int(card_num) <= 373:
            edition = 'Kaldheim - Extended Art'
    elif edition == 'Kaldheim Commander':
        edition = 'Kaldheim Commander Decks'
    elif edition == 'Kamigawa: Neon Dynasty':
        if (int(card_num) >= 303 and int(card_num) <= 306) or (int(card_num) >= 406 and int(card_num) <= 416):
            edition = 'Kamigawa: Neon Dynasty - Borderless'
        elif int(card_num) >= 309 and int(card_num) <= 405:
            edition = 'Kamigawa: Neon Dynasty - Showcase'
        elif int (card_num) >= 433 and int(card_num) <= 505:
            edition = 'Kamigawa: Neon Dynasty - Extended Art'
    # L
    elif edition == 'The List':
        if int(printing_id) == 59150:
            edition = "The List - Adventures in the Forgotten Realms"
        elif int(printing_id) == 81919:
            edition = "The List - Wilds of Eldraine"
        elif int(printing_id) == 88397:
            edition = "The List - Murders at Karlov Manor"
        elif int(printing_id) == 61972:
            edition = 'The List - Innistrad: Crimson Vow'
        elif int(printing_id) >= 85709 and int (printing_id) <= 85719:
            edition = 'The List - The Lost Caverns of Ixalan'
        elif int(printing_id) >= 53273 and int(printing_id) <= 53309:
            edition = 'The List - Zendikar Rising'
        elif int(printing_id) == 73284:
            edition = "The List - The Brothers' War"
        elif int(printing_id) == 80086:
            edition = 'The List - Lord of the Rings: Tales of Middle-earth'
        elif int(printing_id) > 95481:
            edition = 'Mystery Booster 2'
        else:
            edition = 'Mystery Booster'
    elif edition == 'The Lord of the Rings: Tales of Middle-earth':
        edition = 'Lord of the Rings: Tales of Middle-earth'
    elif edition == 'The Lost Caverns of Ixalan':
        if int(card_num) >= 292 and int(card_num) <= 319:
            edition = 'The Lost Caverns of Ixalan - Showcase'
        elif int(card_num) >= 320 and int(card_num) <= 352:
            edition = 'The Lost Caverns of Ixalan - Borderless'
        elif int(card_num) >= 353 and int(card_num) <= 392:
            edition = 'The Lost Caverns of Ixalan - Extended Art'
    # M
    elif edition == 'March of the Machine':
        if int(card_num) == 24:
            edition = 'March of the Machine - Promo Pack'
    elif edition == 'Media Inserts':
        if int(card_num) == 78 or int(card_num) == 99 or int(card_num) == 115:
            edition = 'Gift Box Promos'
        elif int(card_num) == 61:
            edition = 'Buy-a-Box Promos'
        else:
            edition = 'Resale Promos'
    elif edition == 'Modern Horizons Foil':
        edition = 'Modern Horizons'
    elif edition == 'Modern Horizons 2':
        if int(card_num) >= 327 and int(card_num) <= 380:
            edition = 'Modern Horizons 2 Showcase'
        elif int(card_num) >= 381 and int(card_num) <= 441:
            edition = 'Modern Horizons 2 Retro Frame'
    elif edition == 'Prerelease Events: Modern Horizons 2':
        edition = 'Modern Horizons 2 Prerelease Promos'
    elif edition == 'Modern Horizons 3 Commander':
        if int (card_num) in [1, 3, 5, 13, 23, 28, 29, 30]:
            edition = 'Modern Horizons 3'
    elif edition == 'Multiverse Legends':
        edition = 'March of the Machine - Multiverse Legends'
    elif edition == 'Murders at Karlov Manor':
        if int(card_num) >= 287 and int(card_num) <= 316:
            edition = 'Murders at Karlov Manor - Showcase Magnified'
        elif int(card_num) >= 317 and int(card_num) <= 323:
            edition = 'Murders at Karlov Manor - Showcase Ravnica City'
        elif int(card_num) >= 324 and int(card_num) <= 335:
            edition = 'Murders at Karlov Manor - Borderless'
        elif int(card_num) >= 336 and int(card_num) <= 376:
            edition = 'Murders at Karlov Manor - Showcase Dossier'
        elif int(card_num) >= 390 and int(card_num) <= 422:
            edition = 'Murders at Karlov Manor - Extended Art'
    elif edition == 'Murders at Karlov Manor Commander':
        if int(card_num) == 15:
            edition = 'Murders at Karlov Manor'
        elif int(card_num) >= 312 and int(card_num) <= 358:
            edition = ' Murders at Karlov Manor - Commander Extended Art'
        else:
            edition = 'Murders at Karlov Manor - Commander'
    elif edition == 'Mystery Booster Playtest Cards 2021':
        edition = 'Mystery Booster (No PW Symbol)'
    # O
    elif edition == 'Prerelease Events: Oath of the Gatewatch':
        edition = 'Prerelease Promos'
    elif edition == 'Outlaws of Thunder Junction Commander':
        edition = 'Outlaws of Thunder Junction - Commander'
    # P
    elif edition == 'Phyrexia: All Will Be One':
        if (int(card_num) == 271):
            edition = 'Phyrexia: All Will Be One - Phyrexian Language'
        elif int(card_num) >= 285 and int(card_num) <= 324:
            edition = 'Phyrexia: All Will Be One - Borderless Ichor'
    # R
    elif edition == 'Ravnica Remastered':
        if int(card_num) >= 292 and int(card_num) <= 301:
            edition = 'Ravnica Remastered - Borderless'
        elif int(card_num) >= 302 and int(card_num) <= 415:
            edition = 'Ravnica Remastered - Retro Frame'
    # S
    elif edition == 'Strixhaven: School of Mages':
        if int(card_num) >= 378 and int(card_num) <= 382:
            edition = 'Strixhaven: School of Mages Promo Pack'
    elif edition == 'Promo pack: Strixhaven: School of Mages':
        edition = 'Strixhaven: School of Mages Promo Pack'
    # T
    elif edition == 'Promo Pack: Theros Beyond Death':
        edition = 'Theros: Beyond Death - Promo Pack'
    elif edition == 'Throne of Eldraine Foil Double Sided':
        edition = 'Throne of Eldraine'
    # U
    elif edition == 'The List (Unfinity Foil Edition)':
        edition = 'The List - Unfinity'
    # W
    elif edition == 'Prerelease Events: War of the Spark':
        edition = 'Prerelease Promos'
    elif edition == 'World Championship Deck: 2004, Gabriel Nassif':
        edition = None
    elif edition == 'World Championship Deck: 1999, Kai Budde':
        edition = None
    elif edition == 'World Championship Deck: 2000, Jon Finkel':
        edition = None
    elif edition == 'World Championship Deck: 2000, Nicolas Labarre':
        edition = None
    elif edition == 'World Championship Deck: 1997, Paul McCabe':
        edition = None
    elif edition == 'World Championship Deck: 2000, Janosch Kühn':
        edition = 'World Championship'
    # Misc
    elif edition.startswith('Oversized'):
        edition = None
    elif edition.startswith('Prerelease Events: '):
        edition = edition[19:] + ' - Prerelease Promos'
    elif edition.startswith('Promo Pack: '):
        edition = edition[12:] + ' - Promo Pack'
    elif edition.startswith('Duel Decks Anthology'):
        edition = 'Duel Decks: Anthology'
    elif edition == 'Legends Italian':
        edition = 'Legends'
    elif edition == 'Standard Showdown Promos':
        edition = 'Store Championship Promos'
    elif edition == 'Jumpstart Front Cards':
        edition = None
    elif edition == 'Dominaria Remastered':
        if int(card_num) >= 262 and int(card_num) <= 401:
            edition = 'Dominaria Remastered - Retro Frame'
        elif int(card_num) >= 412 and int(card_num) <= 456:
            edition = 'Dominaria Remastered - Borderless'
    elif edition == 'Unfinity':
        if int(card_num) >= 287 and int(card_num) <= 537:
            edition = 'Unfinity Galaxy Foil'
    elif edition == 'Renaissance':
        edition = None

    return edition



def process_foil(foil, name):
    if name == 'Avenger of Zendikar':
        foil = ''

    return foil



def process_csv(dbcsv):
    with open(dbcsv, 'r') as input, open('cardsphere_import.csv', 'w', newline='', encoding='utf-8') as output:
        reader = csv.reader(input, delimiter=',')
        writer = csv.writer(output, delimiter=',')
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            colValues = []
            i = 0
            omitRow = False

            if len(row) >= 18 and row[CSV_CONDITION] == 'Poor':
                continue

            for col in row:
                if i == CSV_NAME:
                    col = process_name(col, row[CSV_EDITION], row[CSV_CARD_NUM])
                    if col is None:
                        omitRow = True
                        break
                if i == CSV_EDITION:
                    col = process_edition(col, row[CSV_CARD_NUM], row[CSV_PRINTING_ID], row[CSV_PRINTING_NOTE])
                    if col is None:
                        omitRow = True
                        break
                if i == CSV_FOIL:
                    col = process_foil(col, row[2])
                
                colValues.append(col)

                i += 1

            if not omitRow:
                writer.writerow(colValues)

if len(sys.argv) != 2:
    print("usage: db2cscsv.py <inputFile>")
else:
    process_csv(sys.argv[1])