# -*- coding: utf-8 -*-

from work.str_utils import reverse_string, get_odd_string, connect_string_alternately, split_sentence_to_words, count_words_length

u"""
NLP100本ノック 2015 Chapter1 の解答を作成し、実行する
"""

def answer_q00():
    problem_string = u'stressed'
    return reverse_string(problem_string)


def answer_q01():
    problem_string = u'パタトクカシーー'
    return get_odd_string(problem_string)
    

def answer_q02():
    problem_str1 = u"パトカー"
    problem_str2 = u"タクシー"
    return connect_string_alternately(problem_str1, problem_str2)


def answer_q03():
    problem_sentence = u'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    words = split_sentence_to_words(problem_sentence)
    return count_words_length(words)
    
    
if __name__ == '__main__':
    answer_string = ''
    answer_string += 'answer_q00: ' + answer_q00() + '\n'
    answer_string += 'answer_q01: ' + answer_q01() + '\n'
    answer_string += 'answer_q02: ' + answer_q02() + '\n'
    answer_string += 'answer_q03: ' + str(answer_q03()) + '\n'
    print answer_string
