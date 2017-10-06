# -*- coding: utf-8 -*-
import unittest2 as unittest  # to support Python 2.6
import affine6p

samples = [
  {
    'id': 'N is 1',
    'a': [[0, 0]],
    'b': [[1, 1]],
    'params': [1, 0, 0, 1, 0, 0]
  },
  {
    'id': 'N is 2',
    'a': [[1, 0], [0, 1]],
    'b': [[0, 2], [-2, 0]],
    'params': [1, 0, 0, 1, 0, 0]
  },
  {
    'id': 'N is 3',
    'a': [[0, 0], [1, 0], [0, 1 ]],
    'b': [[0, 0], [1, 0], [0, 1.1]],
    'params': [1, 0, 0, 1.1, 0, 0],
    'error': 0
  },
  {
    'id': 'N is 4',
    'a': [[0, 0], [1, 0], [0, 1 ], [2, 2]],
    'b': [[0, 0], [1, 0], [0, 1.1],[2, 2]],
    'params': [1, 0, -0.05556, 1.04444, 0, 0.03333],
    'error': 0.02357
  },
  {
    'id': 'N is 5',
    'a': [[0, 0], [1, 0], [0, 1 ], [2, 2], [5, 87]],
    'b': [[0, 0], [1, 0], [0, 1.1],[2, 2], [3, 4 ]],
    'params': [1.01448, -0.02390, 0.57171, 0.00951, 0.00694, 0.33402],
    'error': 0.59314 
  }

]

class TestEstimate(unittest.TestCase):

    def test_estimation(self):
        '''
        should estimate correctly
        '''
        for sple in samples:
            t = affine6p.estimate(sple['a'], sple['b'])
            for k in range(0,6):
                msg = sple['id'] + ': ' + str(k) + '=' + str(t.params[k])
                self.assertTrue(abs(t.params[k] - sple["params"][k])<0.001, msg)

            if len(sple['a']) < 3:
                continue

            e = affine6p.estimate_error(t, sple['a'], sple['b'])
            msg = sple['id'] + ': error =' + str(e)
            self.assertTrue(abs(e - sple["error"])<0.001, msg)


if __name__ == '__main__':
    unittest.main()