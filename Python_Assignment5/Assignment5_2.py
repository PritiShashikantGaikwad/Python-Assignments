def ChkVowel(ch):
    
  if (ch=="a" or  ch=="A"or ch=="e"or ch=="E"or ch=="i"or ch=="I" or ch=="o"or ch=="O"or ch=="u "or ch=="U") :
      print("the given chracter is vowel",ch)

  else:
    print("the given character is Consonant",ch)



def main():
    print("Enter the character :")
    Value=input()
    ChkVowel(Value)
   
if __name__=="__main__":
    main() 