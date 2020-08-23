from django.shortcuts import render
import operator
import string
from django.http import HttpResponse

# Create your views here.
def home(requests):
    return render(requests,'str1/home.html')
def revConcate(requests):
    mytext=requests.GET['fulltext']
    words=[]
    words1=[]
    str2=""
                            
        ###########################################################
        #words Reversal
    for word in mytext.split():
        
        words.append(word[::-1])
        #############################################################
        #whole paragraph Reversal
    
   # words1.reverse()
    words1=words[::-1]
        #############################################################
        #string concatenation
    for word in mytext.split():   
        str2=str2+word                                                      
        
        #############################################################
    return render(requests,'str1/revConcate.html',{'RevWords':words ,'RevPara':words1, 'StrConcate':str2})

                                                                    
