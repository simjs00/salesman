import pickle
import numpy as np
import copy as cp
vocabs =set() 
dt = []

sequence_input_length = 100
sequence_output_length = 100
ori_dir = "./training/"
vocabs = set()
file = open("vocabs.pickle",'rb')
vocabs = list(pickle.load(file))
file.close()

vocab_length = len(vocabs)
print(vocab_length)
train_data_input = []
train_data_output = []

def check_string(data) :
        data = data.replace("\n", "")
        if(data!="") :
            i = vocabs.index(data.lower())
            if(i>=0) :
                return i
        return -1

def prepare_data() :
    f = open(ori_dir+"probe.txt", "r")
    for x in f:
        qa =  x.split('#')
        
        if(qa[0]=="0") :
            input_node=[]
            output_node=[]
            words=  qa[1].split(' ')
            if(len(words)!=0) :
                for wrd in words :    
                    wrd = wrd.replace("\n", "")
                    if(wrd!="") :
                        i = vocabs.index(wrd.lower())
                        if(i>=0) :
                            input_node.append(i+2)
            elif(len(words)==0) :
                    data = data.replace("\n", "")
                    if(data!="") :
                        i = vocabs.index(data.lower())
                        if(i>=0) :
                            input_node.append(i+2)
            words = qa[2].split(' ')
            if(len(words)!=0) :
                for wrd in words :    
                    wrd = wrd.replace("\n", "")
                    if(wrd!="") :
                        i = vocabs.index(wrd.lower())
                        if(i>=0) :
                            output_node.append(i+2)
            elif(len(words)==0) :
                    data = data.replace("\n", "")
                    if(data!="") :
                        i = vocabs.index(qa[2].lower())
                        if(i>=0) :
                            output_node.append(i+2)
            train_data_input.append(input_node)
            if(len(output_node)==0):
                output_node=[]
            train_data_output.append(output_node)
        elif(qa[0]=="1") :

            input_node=[]
            output_node=[]
              
                            
            words=  qa[1].split(' ')
            if(len(words)!=0) :
                for wrd in words :    
                    wrd = wrd.replace("\n", "")
                    if(wrd!="") :
                        i = vocabs.index(wrd.lower())
                        if(i>=0) :
                            input_node.append(i+2)
            elif(len(words)==0) :
                    data = data.replace("\n", "")
                    if(data!="") :
                        i = vocabs.index(data.lower())
                        if(i>=0) :
                            input_node.append(i+2)

            words=  qa[len(qa)-1].split(' ')
            if(len(words)!=0) :
                for wrd in words :    
                    wrd = wrd.replace("\n", "")
                    if(wrd!="") :
                        i = vocabs.index(wrd.lower())
                        if(i>=0) :
                            output_node.append(i+2)
            elif(len(words)==0) :
                    data = data.replace("\n", "")
                    if(data!="") :
                        i = vocabs.index(data.lower())
                        if(i>=0) :
                            output_node.append(i+2) 



            for data in qa[2:len(qa)-2] :
                copy = cp.copy(input_node)
                words=  data.split(' ')
                if(len(words)!=0 ) :
                    for val in words :
                        if(val!="") :
                            i = vocabs.index(val.lower()) 
                            if(i>=0) :
                                copy.append(i+2)
                else : 
                        if(data!="") :
                            i = vocabs.index(data.lower()) 
                            if(i>=0) :
                                copy.append(i+2)
                train_data_input.append(copy)
                if(len(output_node)==0):
                    output_node=[]
                train_data_output.append(output_node)

        elif(qa[0]=="2") :
            word_1 =[]
            word_2 = []
            input_node = []
            output_node = []
            ans = qa[1].split('~')  
            
            for data in ans[0].split(" ") :
               if(check_string(data)!=-1) :
                input_node.append(check_string(data)+2)
            
            for data in ans[1].split("^") :
                word_1.append(data)

            for data in ans[2].split("^") :
                word_2.append(data)

            words = qa[len(qa)-1].split(' ')
            if(len(words)!=0) :
                for wrd in words :    
                    wrd = wrd.replace("\n", "")
                    if(wrd!="") :
                        i = vocabs.index(wrd.lower())
                        if(i>=0) :
                            output_node.append(i+2) 
            elif(len(words)==0) :
                    data = data.replace("\n", "")
                    if(data!="") :
                        i = vocabs.index(qa[len(qa)-1].lower())
                        if(i>=0) :
                            output_node.append(i+2)
            for val in word_1 :
                
                #print(copy)
                for val2 in word_2 :
                    copy = cp.copy(input_node)
                    val_s1 = val.split(" ")
                    if(len(val_s1) !=0) :
                        for v in val_s1 :
                            if(check_string(v)!=-1) :
                                copy.append(check_string(v)+2)
                    else :
                         if(check_string(val)!=-1) :
                                copy.append(check_string(val)+2)           

                    val_s2 = val2.split(" ")
                    if(len(val_s1) !=0) :
                        for v in val_s2 :
                            if(check_string(v)!=-1) :
                                copy.append(check_string(v)+2)
                    else :
                         if(check_string(val2)!=-1) :
                                copy.append(check_string(val2)+2)  
                    #print(copy)
                    train_data_input.append(copy) 
                    if(len(output_node)==0):
                        output_node=[]
                    train_data_output.append(output_node)    

prepare_data()
print(len(train_data_input))
print(len(train_data_output))

with open(r"training/train_input.pickle", "wb") as output_file:
   pickle.dump(train_data_input, output_file)

with open(r"training/train_output.pickle", "wb") as output_file:
   pickle.dump(train_data_output, output_file)
# ##print(train_data_input)
# #print(train_data_output)
# print(vocab_length)
