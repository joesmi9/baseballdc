# import sys
# import os

# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

# import baseballdc
# import unittest

# class TestTest(unittest.TestCase):

#         def test_test_test(self):

#                 baseballdc_request_player = {
#                         'data_source': 'BASEBALL_REFERENCE',
#                         'query_params': {
#                         'scope': 'INDIVIDUAL_PLAYER',
#                         'table': 'Standard Batting',
#                         'first_name': 'Miguel',
#                         'last_name': 'Cabrera'
#                         }
#                 }

#                 df = baseballdc.get_data(baseballdc_request_player)

#                 df_columns = list(df.columns.values)
#                 expected_columns = ['Year', 'Age', 'Tm', 'Lg', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR',
#                                         'RBI', 'SB', 'CS', 'BB', 'SO', 'BA', 'OBP', 'SLG', 'OPS', 'OPS+', 'TB',
#                                         'GDP', 'HBP', 'SH', 'SF', 'IBB', 'Pos', 'Awards']

#                 self.assertEqual(df_columns, expected_columns)



# if __name__ == '__main__':
#         unittest.main()

