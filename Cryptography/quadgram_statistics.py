# -*- coding: UTF-8 -*-
import random
from ngram_score import ngram_score
#参数初始化
# ciphertext = 'JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVQVFIEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX'
ciphertext = 'xubbemehbtcovhyudtxemqhuoek'
ciphertext = ciphertext.upper()

parentkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#只是用来声明key是个字典
key = {'A':'A'}
#读取quadgram statistics
fitness = ngram_score('quadgrams.txt')
parentscore = -99e9
maxscore = -99e9
j = 0

print('---------------------------start---------------------------')
while 1:
  j = j+1
  #随机打乱key中的元素
  random.shuffle(parentkey)
  #将密钥做成字典
  for i in range(len(parentkey)):
    key[parentkey[i]] = chr(ord('A')+i)
    #用字典一一映射解密
  decipher = ""
  for i in range(len(ciphertext)):
    decipher += key[ciphertext[i]]
  parentscore = fitness.score(decipher)#计算适应度
  #在当前密钥下随机交换两个密钥的元素从而寻找是否有更优的解
  count = 0
  while count < 1000:
    a = random.randint(0,25)
    b = random.randint(0,25)
    #随机交换父密钥中的两个元素生成子密钥，并用其进行解密
    child = parentkey[:]
    child[a],child[b] = child[b],child[a]
    childkey = {'A':'A'}
    for i in range(len(child)):
      childkey[child[i]] = chr(ord('A')+i)
    decipher = ciphertext
    for i in range(len(decipher)):
      decipher = decipher[:i] + childkey[decipher[i]] + decipher[i+1:]
    score = fitness.score(decipher)
    #此子密钥代替其对应的父密钥，提高明文适应度
    if score > parentscore:
      parentscore = score
      parentkey = child[:]
      count = 0
    count = count+1
  #输出该key和明文
  if parentscore > maxscore:
    maxscore = parentscore
    maxkey = parentkey[:]
    for i in range(len(maxkey)):
      key[maxkey[i]] = chr(ord('A')+i)
    decipher = ciphertext
    for i in range(len(decipher)):
      decipher = decipher[:i] + key[decipher[i]] + decipher[i+1:]

    print ('Currrent key: '+''.join(maxkey))
    print ('Iteration total:', j)
    print ('Plaintext: ', decipher)