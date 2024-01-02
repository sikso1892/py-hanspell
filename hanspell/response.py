# -*- coding: utf-8 -*-
from collections import namedtuple, OrderedDict

# 조사와 어미도 단어로 처리함. 마땅한 영단어가 생각이 안 나서..
_checked = namedtuple('Checked',
    ['result', 'original', 'checked', 'errors', 'words', 'time'])


class Checked(_checked):
    def __new__(cls, result=False, original='', checked='', errors=0, words=[], time=0.0):
        return super(Checked, cls).__new__(
            cls, result, original, checked, errors, words, time)

    def as_dict(self):
        d = {
            'result': self.result,
            'original': self.original,
            'checked': self.checked,
            'errors': self.errors,
            'words': self.words,
            'time': self.time,
        }
        return d

    def only_checked(self):
        return self.checked
    
    @classmethod
    def merge_instances(cls, instances):
        result = False
        original = ''
        checked = ''
        errors = 0
        words = OrderedDict()
        total_time = 0.0

        for instance in instances:
            if instance.result:
                result = True
            original += instance.original + ' '
            checked += instance.checked + ' '
            errors += instance.errors
            
            for word, check_result in instance.words.items():
                words[word] = check_result
                
            total_time += instance.time

        return cls(result, original.strip(), checked.strip(), errors, words, total_time)
