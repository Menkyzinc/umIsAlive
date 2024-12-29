def makecipher(plaintext):
  keym = [int(k) for k in str(key)]
  key_length = len(keym)
  
  chunks = [plaintext[i:i+key_length] for i in range(0, len(plaintext), key_length)]
  
  ciphertext = ""
  for chunk in chunks:
    temp = [''] * key_length
    for i, char in enumerate(chunk):
      temp[keym[i]-1] = char
    ciphertext += ''.join(temp)
  
  return ciphertext

def makeplain(ciphertext):
  key2n = [int(k) for k in str(key2)]
  key2n_length = len(key2n)
  
  chunks = [ciphertext[i:i+key2n_length] for i in range(0, len(ciphertext), key2n_length)]
  
  plaintext = ""
  for chunk in chunks:
    temp = [''] * key2n_length
    for i, char in enumerate(chunk):
      temp[key2n[i]-1] = char
    plaintext += ''.join(temp)
  
  return plaintext

def askKey():
  global key
  key = input('암호화 키를 입력하세요:')

def whatIsKey2():
  global key2
  llist = []
  jlist = []
  for i in key :
    llist.append(int(i))
  c = 0
  for j in llist :
    c += 1
    jlist.append(llist.index(c)+1)
  key2 = ''.join(map(str, jlist))

def asking () :
  answer = input('명령어를 입력하세요: ')
  
  if answer == '암호화':
    a = input('암호화할 문장을 띄어쓰기 없이 입력하세요: ')
    return makecipher(a)
    

  elif answer == '복호화':
    a = input('복호화할 문장을 띄어쓰기 없이 입력하세요: ')
    return makeplain(a)
  
  elif answer == '암호화 키 입력':
    askKey()
    return('암호화 키가 변경되었습니다.')



askKey()
while True:
  whatIsKey2()
  print('현재 사용되는 암호화 키는',key,'입니다.')
  answer = asking()
  print(answer)
