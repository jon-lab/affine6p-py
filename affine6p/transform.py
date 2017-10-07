# -*- coding: utf-8 -*-

import math

class Transform(object):

    def __init__(self, params):
        # Public, to allow user access
        self.params = params

    def transform(self, p):
        '''
        Parameter
            p
                point [x, y] or list of points [[x1,y1], [x2,y2], ...]
        '''
        def transform_one(q):
            return [self.params[0] * q[0] + self.params[1] * q[1] + self.params[4],
                    self.params[2] * q[0] + self.params[3] * q[1] + self.params[5]]

        if not isinstance(p[0], list):
            # Single point
            return transform_one(p)
        # else
        return list(map(transform_one, p))

    def transform_inv(self, p):
        '''
        Parameter
            p
                point [x, y] or list of points [[x1,y1], [x2,y2], ...]
        '''
        def transform_inv_one(q):
            det = self.params[0] * self.params[3] - self.params[2] * self.params[1]
            return [(self.params[3] * (q[0] - self.params[4]) - self.params[1] * (q[1] - self.params[5])) / det,
                    (self.params[2] * (q[0] - self.params[4]) - self.params[0] * (q[1] - self.params[5])) / det * -1.0]

        if not isinstance(p[0], list):
            # Single point
            return transform_inv_one(p)
        # else
        return list(map(transform_inv_one, p))

    def get_matrix(self):
        return [[self.params[0], self.params[1], self.params[4]],
                [self.params[2], self.params[3], self.params[5]],
                [0,              0,              1]]

    def get_rotation_x(self):
        return math.atan2(-self.params[1], self.params[0])

    def get_rotation_y(self):
        return math.atan2(self.params[2], self.params[3])

    def get_scale_x(self):
        return math.sqrt(self.params[0] * self.params[0] + self.params[1] * self.params[1])

    def get_scale_y(self):
        return math.sqrt(self.params[2] * self.params[2] + self.params[3] * self.params[3])

    def get_scale(self):
        summed = self.get_scale_x() * self.get_scale_x() + self.get_scale_y() * self.get_scale_y()
        return math.sqrt(summed * 0.5)

    def get_translation(self):
        return [self.params[4], self.params[5]]


