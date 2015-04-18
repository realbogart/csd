# Copyright (C) 2009 Jacob Joaquin
#
# This file is part of csd.
# 
# csd is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# csd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with csd.  If not, see <http://www.gnu.org/licenses/>.

'''Python Score. Currently unstable.'''


#!/usr/bin/python
import sys
from sys import argv
from itertools import imap
from itertools import chain
import csd
from csd import sco
import atexit

class PCallback(object):

    def __init__(self, statement, identifier, pfield, function, *args,
                 **kwargs):
        self.statement = statement
        self.identifier = identifier
        self.pfield = pfield
        self.function = function
        self.args = args
        self.kwargs = kwargs
        

class PythonScore(object):
    score_non_floats = ('.', '+', '<', '!') 

    # TODO: 
    # Add reset()
    # Output thus far feature
    # score_data should be considered private
    # p_callbacks should be considered private
    
    def __init__(self):
        self.cue = Cue(self)
        self.score_data = []
        self.p_callbacks = [[]]

    def _map_process(self, data, statement, identifier, pfield, function,
                     *args, **kwargs):
        convert_numeric = True
        sco_statements_enabled = True

        # Convert pfield to list if it isn't one
        if not isinstance(pfield, list):
            pfield = [pfield]

        selection = sco.select(data, {0: statement, 1: identifier})

        for k, v in selection.iteritems():
            for p in pfield:
                element = sco.event.get(v, p)

                # Bypass if score statement like carry
                # TODO: ^+x, npx, ppx, etc...
                if sco_statements_enabled and element in score_non_floats:
                    break

                # Convert value to float
                if convert_numeric:
                    try:
                        element = float(element)
                    except Exception:
                        pass

                deez_args = (element,) + args
                selection[k] = sco.event.set(v, p,
                                             function(*deez_args, **kwargs))

        return sco.merge(data, selection)

    def f(self, *args):
        self.write(' '.join(chain('f', imap(str, args)))) 

    def i(self, *args):
        self.write(' '.join(chain('i', imap(str, args)))) 

    def t(self, *args):
        self.write(' '.join(chain('t 0', imap(str, args)))) 

    def p_callback(self, statement, identifier, pfield, func, *args, **kwargs):
        self.p_callbacks[-1].append(PCallback(statement, identifier, pfield,
                                    func, *args, **kwargs))

    def pmap(self, statement, identifier, pfield, func, *args, **kwargs):
        data = "\n".join(self.score_data)
        self.score_data = [self._map_process(data, statement, identifier,
                           pfield, func, *args, **kwargs)]

    def write(self, data):
        # Apply pfield callbacks
        for L in self.p_callbacks:
            for cb in L:
                data = self._map_process(data, cb.statement, cb.identifier,
                                         cb.pfield, cb.function, *cb.args,
                                         **cb.kwargs)

        # Apply time stack
        selected = sco.select(data, {0: 'i'})
        op = sco.selection.operate_numeric(selected, 2,
                                           lambda x: x + self.cue.now())
        self.score_data.append(sco.merge(data, op))


class Cue(object):

    def __init__(self, parent):
        self.stack = []
        self.parent = parent
        self.translation = 0;

    def __call__(self, when):
        self.when = when
        return self

    def __enter__(self):
        self.stack.append(self.when)
        self.parent.p_callbacks.append([])
        self.translation = sum(self.stack)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stack.pop()
        self.parent.p_callbacks.pop()
        self.translation = sum(self.stack)
        return False

    def now(self):
        return self.translation


class PythonScoreBin(PythonScore):

    def __init__(self):
        super(PythonScoreBin, self).__init__()   
        atexit.register(self._bin_end_score)

    def _bin_end_score(self):
        # TODO: This shouldn't run under certain circumstances
        with open(argv[1], 'w') as f:
        	f.write("\n".join(self.score_data))