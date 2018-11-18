import pickle
vocabs =set() 
dt = []
path = "./training/"
def prepare_vocab() :
    f = open("./training/probe.txt", "r")
    for x in f:
        qa =  x.split('#')
        if(qa[0]=="1" or qa[0]=="0") :
            for data in qa[1:len(qa)] :
                words=  data.split(' ')
                if(len(words)!=0) :
                    for wrd in words :
                        wrd = wrd.replace("\n", "")
                        if(wrd!="") :
                            vocabs.add(wrd.lower())
                            dt.append(wrd.lower())
                elif(len(words)==0) :
                        data = data.replace("\n", "")
                        if(data!="") :
                            vocabs.add(data.lower())
                            dt.append(data.lower())
        elif(qa[0]=="2") :

            split_qa =qa[1].split('~')

            qst = split_qa[0].split(' ')
            if(len(qst)!=0) :
                for data in qst :
                        data = data.replace("\n", "")
                        if(data!="") : 
                            vocabs.add(data.lower())
                            dt.append(data.lower())
            elif(len(qst)==0) :
                    qst = qst.replace("\n", "")
                    if(qst!="") :
                        vocabs.add(qst.lower())
                        dt.append(qst.lower())
           
            qst = split_qa[1].split('^')
            for data in qst :
                words=  data.split(' ')
                if(len(words)!=0) :
                    for wrd in words :
                        wrd = wrd.replace("\n", "")
                        if(wrd!="") :
                            vocabs.add(wrd.lower())
                            dt.append(wrd.lower())
                elif(len(words)==0) :
                        data = data.replace("\n", "")
                        if(data!="") :
                            vocabs.add(data.lower())
                            dt.append(data.lower())

            qst = split_qa[2].split('^')
            for data in qst :
                words=  data.split(' ')
                if(len(words)!=0) :
                    for wrd in words :
                        wrd = wrd.replace("\n", "")
                        if(wrd!="") :
                            vocabs.add(wrd.lower())
                            dt.append(wrd.lower())
                elif(len(words)==0) :
                        data = data.replace("\n", "")
                        if(data!="") :
                            vocabs.add(data.lower())
                            dt.append(data.lower())

           
            words=  qa[2].split(' ')
            if(len(words)!=0) :
                for wrd in words :
                    wrd = wrd.replace("\n", "")
                    if(wrd!="") :
                        #print(wrd)
                        vocabs.add(wrd.lower())
                        dt.append(wrd.lower())
            elif(len(words)==0) :
                    data = data.replace("\n", "")
                    if(data!="") :
                        vocabs.add(data.lower())
                        dt.append(data.lower())
prepare_vocab()
# print(vocabs)
print(len(vocabs))
vocabs=sorted(vocabs)
print(len(vocabs))
with open(r"training/vocabs.pickle", "wb") as output_file:
   pickle.dump(vocabs, output_file)
