import unittest
import db2cscsv

class TestDeckboxToCardSphereCSV(unittest.TestCase):

# Card Name Tests
    def test_quotes_removed_from_card_name(self):
        card = '"Lifetime" Pass Holder'
        ed = 'Unfinity'
        num = 65

        result = db2cscsv.process_name(card, ed, num)

        self.assertEqual(result, 'Lifetime Pass Holder')

    def test_dunedain_blade_accent_vowel(self):
        card = 'Dúnedain Blade'
        ed = 'The Lord of the Rings: Tales of Middle-earth'
        num = 6

        result = db2cscsv.process_name(card, ed, num)

        self.assertEqual(result, 'Dunedain Blade')

# Card Name Tests (Tokens)
    def test_two_sided_fallout_tokens(self):
        card = 'Alien // Clue'
        ed = 'Extras: Fallout'
        num = 29

        result = db2cscsv.process_name(card, ed, num)

        self.assertEqual(result, 'Alien Token | Clue Token')

    def test_emblem_token(self):
        card = 'Emblem: Gideon'
        ed = 'Extras: Battle for Zendikar'
        num = 12

        result = db2cscsv.process_name(card, ed, num)

        self.assertEqual(result, 'Gideon Emblem')

    def test_name_with_quotes(self):
        card = '"Bounty: Rissa ""Blades"" Lee // Bounty Rules"'
        ed = 'Extras: Outlaws of Thunder Junction Commander'
        num = 8

        result = db2cscsv.process_name(card, ed, num)

        self.assertEqual(result, 'Bounty: Rissa "Blades" Lee')

# Card Edition Tests
    def test_the_list_edition(self):
        ed = 'The List'
        num = 2

        result = db2cscsv.process_edition(ed, num, 95480, '')

        self.assertEqual(result, 'Mystery Booster')

    def test_mkm_borderless(self):
        ed = 'Murders at Karlov Manor'
        num = 329

        result = db2cscsv.process_edition(ed, num, '', '')

        self.assertEqual(result, 'Murders at Karlov Manor - Borderless')

    def test_rvr_retro(self):
        ed = 'Ravnica Remastered'
        num = 335

        result = db2cscsv.process_edition(ed, num, '', '')

        self.assertEqual(result, 'Ravnica Remastered - Retro Frame')

    def test_stx_showcase(self):
        ed = 'Strixhaven: School of Mages'
        num = 382

        result = db2cscsv.process_edition(ed, num, '', '')

        self.assertEqual(result, 'Strixhaven: School of Mages Promo Pack')

# Miscellaneous Tests
    def test_csv_header(self):
        # given a copied and pasted header from the latest Deckbox Tradelist export
        header = 'Count,Tradelist Count,Decks Count Built,Decks Count All,Name,Edition,Edition Code,Card Number,Condition,Language,Foil,Signed,Artist Proof,Altered Art,Misprint,Promo,Textless,Printing Id,Printing Note,Tags,My Price,Type,Cost,Rarity,Price,Image URL,Last Updated'

        cols = header.split(',')

        self.assertEqual(cols[db2cscsv.CSV_NAME], 'Name')
        self.assertEqual(cols[db2cscsv.CSV_EDITION], 'Edition')
        self.assertEqual(cols[db2cscsv.CSV_CARD_NUM], 'Card Number')
        self.assertEqual(cols[db2cscsv.CSV_FOIL], 'Foil')
        self.assertEqual(cols[db2cscsv.CSV_PRINTING_NOTE], 'Printing Note')

if __name__ == '__main__':
    unittest.main()