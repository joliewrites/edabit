def encrypt(word):
  v= {'a':'0','e':'1','o':'2','u':'3'}
  return ''.join(v[i] if i in v else i for i in word[::-1]) +'aca'
