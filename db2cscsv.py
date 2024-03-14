import sys
import csv

# Constants
CSV_NAME = 3
CSV_EDITION = 4
CSV_CARD_NUM = 6
CSV_FOIL = 9
CSV_PRINTING_NOTE = 17

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

    # Guildgates
    if edition == 'Ravnica Allegiance' or edition == 'Guilds of Ravnica':
        if name.endswith('Guildgate'):
            name += ' (#' + card_num + ')'

    # Duel Decks
    if edition == 'Duel Decks Anthology, Garruk vs. Liliana':
        if name == 'Corrupt':
            name = 'Corrupt (Garruk vs. Liliana)'
    elif edition == 'Duel Decks Anthology, Divine vs. Demonic':
        if name == 'Corrupt':
            name = 'Corrupt (Divine vs. Demonic)'


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
        if edition == 'Extras: Avacyn Restored':
            if name == 'Angel // Demon':
                name = 'Angel Token | Demon Token (Helvault) (Double-Sided)'
        elif edition == 'Extras: Commander 2020':
            if name == 'Angel // Elemental':
                name = 'Angel Token | Elemental Token (Red)'
            elif name == 'Bird Illusion // Beast':
                name = 'Beast Token | Bird Illusion Token'
            elif name == 'Drake // Goblin Warrior':
                name = 'Drake Token | Goblin Warrior Token'
            elif name == 'Drake // Insect':
                name = 'Drake Token | Insect Token (Blue/Red)'
        elif edition == 'Extras: Planechase Anthology':
            if name == 'Angel // Saproling':
                name = 'Angel Token | Saproling Token'
            elif name == 'Dragon // Saproling':
                name = 'Dragon Token | Saproling Token'
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
        elif edition == 'Extras: Commander 2018':
            if name == 'Angel // Soldier':
                name = 'Angel Token | Soldier Token'
            elif name == 'Angel // Zombie':
                name = 'Angel Token | Zombie Token'
            elif name == 'Cat // Soldier':
                name = 'Cat Token | Soldier Token'
            elif name == 'Construct // Myr':
                name = 'Construct Token (4/4) (2/1)'
            elif name == 'Token: Dragon Egg // Dragon':
                name = 'Dragon Token | Dragon Egg'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander 2017':
            if name == 'Cat // Cat Warrior':
                name = 'Cat Token | Cat Warrior Token'
            elif name == 'Dragon // Gold':
                name = 'Dragon Token | Gold Token (4/4)'
            elif name == 'Rat // Cat Warrior':
                name = 'Cat Warrior Token | Rat Token'
            else:
                name += ' Token'
        elif edition == 'Extras: Commander 2015':
            if name == 'Elephant // Saproling':
                name = 'Elephant Token | Saproling Token'
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
            else:
                name += ' Token'
        elif edition == 'Extras: Commander Anthology Volume II':
            if name == 'Emblem: Daretti, Scrap Savant':
                name = 'Daretti Emblem'
            else:
                name += ' Token'
        elif edition == 'Extras: Modern Horizons 2':
            if name == 'Beast // Clue':
                name = 'Beast Token | Clue Token (#15)'
            elif name == 'Clue':
                name = 'Clue Token (#014)'
            elif name == 'Crab // Food':
                name = 'Crab Token | Food Token (#18)'
            else:
                name += ' Token'
        elif edition == 'Extras: Unsanctioned':
            if name == 'Beeble // Dragon':
                name = 'Beeble Token | Dragon Token'
            elif name == 'Beeble // Squirrel':
                name = 'Beeble Token | Squirrel Token'
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
        elif edition == 'Extras: Ikoria: Lair of Behemoths':
            if name == 'Companion':
                pass
            else:
                name += ' Token'
        elif edition == 'Extras: Innistrad: Midnight Hunt':
            if name == 'Day // Night':
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
        elif edition == 'Extras: Kaldheim Placeholders':
            if name == 'Double-Faced Card Placeholder':
                name = 'Helper Card (#' + card_num + ')'
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
        elif edition == 'Extras: Battle for Zendikar':
            if name == 'Eldrazi Scion':
                name = 'Eldrazi Scion Token (#' + card_num + ')'
            elif name == 'Elemental':
                name = 'Elemental Token (Red)'
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
        elif edition == 'Extras: Eternal Masters':
            if name == 'Elemental':
                name = 'Elemental Token (Blue/Red)'
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
            else:
                name += ' Token'
        elif edition == 'Extras: Streets of New Capenna':
            if name == 'Copy // Treasure':
                name = 'Copy Token | Treasure Token (#17)'
            else:
                name += ' Token'
        else:
            name += ' Token'

        if name == 'Checklist Token':
            name = 'Checklist Card'

    # Two-faced cards
    if edition == 'Innistrad: Midnight Hunt' or edition == 'Innistrad: Crimson Vow' or edition == 'Champions of Kamigawa' or edition == 'Dark Ascension' or edition == 'Zendikar Rising Commander' or edition == 'Betrayers of Kamigawa' or edition == 'Innistrad' or edition == 'Shadows over Innistrad' or edition == 'Eldritch Moon':
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

    # Plains
    if name == 'Plains':
        name += ' (#' + card_num + ')'

    # Island
    if name == 'Island':
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
        else:
            name += ' (#' + card_num + ')'


    # Misc
    if edition == 'Champions of Kamigawa' and name == 'Brothers Yamazaki':
        name = 'Brothers Yamazaki (#160a)'

    return name



def process_edition(edition, card_num, printing_note):
    edition = edition.replace("Extras: ", "")

    if edition == 'Global Series: Jiang Yanggu and Mu Yanling':
        edition = 'Global Series: Jiang Yanggu & Mu Yanling'
    elif edition == 'World Championship Deck: 2004, Gabriel Nassif':
        edition = None
    elif edition == 'World Championship Deck: 1999, Kai Budde':
        edition = None
    elif edition == 'World Championship Deck: 2000, Jon Finkel':
        edition = None
    elif edition == 'World Championship Deck: 2000, Nicolas Labarre':
        edition = None
    elif edition == 'World Championship Deck: 2000, Janosch Kühn':
        edition = 'World Championship'
    elif edition == 'Avacyn Restored (The Helvault Experience)':
        edition = 'Avacyn Restored'
    elif edition == 'Media Inserts':
        edition = 'Resale Promos'
    elif edition.startswith('Oversized'):
        edition = None
    elif edition == 'Promo Pack: Theros Beyond Death':
        edition = 'Theros: Beyond Death - Promo Pack'
    elif edition.startswith('Promo Pack: '):
        edition = edition[12:] + ' - Promo Pack'
    elif edition.startswith('Duel Decks Anthology'):
        edition = 'Duel Decks: Anthology'
    elif edition == 'Throne of Eldraine Foil Double Sided':
        edition = 'Throne of Eldraine'
    elif edition == 'Innistrad: Midnight Hunt':
        if int(card_num) >= 278 and int(card_num) <= 379:
            edition = 'Innistrad: Midnight Hunt - Showcase'
    elif edition == 'Prerelease Events: Modern Horizons 2':
        edition = 'Modern Horizons 2 Prerelease Promos'
    elif edition == 'Kaldheim Commander':
        edition = 'Kaldheim Commander Decks'
    elif edition == 'Legends Italian':
        edition = 'Legends'
    elif edition == 'Prerelease Events: Innistrad: Midnight Hunt':
        edition = 'Innistrad: Midnight Hunt - Prerelease Promos'
    elif edition == 'Prerelease Events: Innistrad: Crimson Vow':
        edition = 'Innistrad: Crimson Vow - Prerelease Promos'
    elif edition == 'Standard Showdown Promos':
        edition = 'Store Championship Promos'
    elif edition == 'Jumpstart Front Cards':
        edition = None
    elif edition == 'Kaldheim Placeholders':
        edition = 'Kaldheim'
    elif edition == 'Prerelease Events: War of the Spark':
        edition = 'Prerelease Promos'
    elif edition == 'Ikoria: Lair of Behemoths':
        if printing_note == 'Showcase':
            edition = 'Ikoria: Lair of Behemoths - Alternate Art'
    elif edition == 'The Brothers\' War Retro Artifacts':
        edition = 'The Brothers\' War - Retro Artifacts'
    elif edition == 'Dominaria Remastered':
        if int(card_num) >= 262 and int(card_num) <= 401:
            edition = 'Dominaria Remastered - Retro Frame'
        elif int(card_num) >= 412 and int(card_num) <= 456:
            edition = 'Dominaria Remastered - Borderless'
    elif edition == 'Unfinity':
        if int(card_num) >= 287 and int(card_num) <= 537:
            edition = 'Unfinity Galaxy Foil'
    # TODO: Mondern Horizons 2 retro border
    # TODO: Phyrexia All will be One full art

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

            for col in row:
                if i == CSV_NAME:
                    col = process_name(col, row[CSV_EDITION], row[CSV_CARD_NUM])
                    if col is None:
                        omitRow = True
                        break
                if i == CSV_EDITION:
                    col = process_edition(col, row[CSV_CARD_NUM], row[CSV_PRINTING_NOTE])
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