from konlpy.tag import Okt
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Komoran
from konlpy.tag import Twitter


kkma = Kkma()
okt = Okt()
komoran = Komoran()
hannanum = Hannanum()
twitter = Twitter()


# Morpheme analysis 1 using konlpy
print("okt 형태소 분석 : ", okt.morphs(u"집에 가면 감자 좀 쪄줄래?"))
print("kkma 형태소 분석 : ", kkma.morphs(u"집에 가면 감자 좀 쪄줄래?"))
print("hannanum 형태소 분석 : ", hannanum.morphs(u"집에 가면 감자 좀 쪄줄래?"))
print("komoran 형태소 분석 : ", komoran.morphs(u"집에 가면 감자 좀 쪄줄래?"))
print("twitter 형태소 분석 : ", twitter.morphs(u"집에 가면 감자 좀 쪄줄래?"))


# Morpheme analysis 2 using konlpy
print("okt 형태소 분석 : ", okt.morphs(u"아버지가방에들어가신다"))
print("kkma 형태소 분석 : ", kkma.morphs(u"아버지가방에들어가신다"))
print("hannanum 형태소 분석 : ", hannanum.morphs(u"아버지가방에들어가신다"))
print("komoran 형태소 분석 : ", komoran.morphs(u"아버지가방에들어가신다"))
print("twitter 형태소 분석 : ", twitter.morphs(u"아버지가방에들어가신다"))


# Part of speech tagging comparison 1 using konlpy
print("okt 품사태깅 : ", okt.pos(u"집에 가면 감자 좀 쪄줄래?"))
print("kkma 품사태깅 : ", kkma.pos(u"집에 가면 감자 좀 쪄줄래?"))
print("hannanum 품사태깅 : ", hannanum.pos(u"집에 가면 감자 좀 쪄줄래?"))
print("komoran 품사태깅 : ", komoran.pos(u"집에 가면 감자 좀 쪄줄래?"))
print("twitter 품사태깅 : ", twitter.pos(u"집에 가면 감자 좀 쪄줄래?"))


# Part of speech tagging comparison 1 using konlpy
print("okt 품사태깅 : ", okt.pos(u"아버지가 방에 들어 가신다"))
print("kkma 품사태깅 : ", kkma.pos(u"아버지가 방에 들어 가신다"))
print("hannanum 품사태깅 : ", hannanum.pos(u"아버지가 방에 들어 가신다"))
print("komoran 품사태깅 : ", komoran.pos(u"아버지가 방에 들어 가신다"))
print("twitter 품사태깅 : ", twitter.pos(u"아버지가 방에 들어 가신다"))