import pandas as pd
import numpy as np
path = 'F:\\Divya\\MCR\\Data\\Final Data\\clean_Data.csv'

def OneHotEncoder():
    df=pd.read_csv(path,sep="|");
    evidence=df.EVIDENCE;
    code=df.code;
    codetype=df.codeType
    sectionname=df.SECTIONNAME
    worktype=df.WorkType
    serviceline=df.ServiceLine
    hospitalid=df.HospitalId

    print "evidence"
    onehot_evidecne=convert_to_id(evidence,"evidence")
    print "code"
    onehot_code=convert_to_id(code,"code")
    print onehot_code
    print "codetype"
    onehot_codetype=convert_to_id(codetype,"codetype")
    print onehot_codetype
    print "sectionname"
    onehot_sectionname=convert_to_id(sectionname,"sectionname")
    print "worktype"
    onehot_worktype=convert_to_id(worktype,"worktype")
    print "serviceline"
    onehot_serviceline=convert_to_id(serviceline,"serviceline")
    print "hospitalid"
    onehot_hospitalid=convert_to_id(hospitalid,"hospitalid")

def convert_to_id(name,field_name):
    retvec1 = []
    a=[]
    i=0;
    #d=pd.DataFrame(columns=['evidence','code','codetype','sectionname','worktype','serviceline','hospitalid']);

    if(field_name=="evidence"):
        print ("in evidence")
        for x in name:
            for y in (str(x).split(" ")):
                a.append(y)

        unique_evidence_name=list(set(a))
        field2id = dict([(f, icnt) for icnt, f in enumerate(unique_evidence_name)]);

        for x in name:
            retvec = np.zeros(len(field2id));
            for y in (str(x).replace('\n',' ').strip().split(" ")):
                cid = field2id[y];
                retvec[cid] = 1;
            retvec1.append(retvec)
            if (i % 100000 == 0):
                print i
            i += 1
            #print retvec1
        return retvec1

    elif(field_name=="code"):
        print ("in code")
        onehot_code=generate_onehot(name)
        return onehot_code

    elif (field_name == "codetype"):
        print ("in codetype")
        onehot_codetype=generate_onehot(name)
        return onehot_codetype

    elif (field_name == "sectionname"):
        print ("in sectionname")
        onehot_sectionname = generate_onehot(name)
        return onehot_sectionname

    elif (field_name == "worktype"):
        print ("in worktype")
        onehot_worktype = generate_onehot(name)
        return onehot_worktype

    elif (field_name == "serviceline"):
        print ("in serviceline")
        onehot_serviceline = generate_onehot(name)
        return onehot_serviceline

    elif (field_name == "hospitalid"):
        print ("in hospitalid")
        onehot_hospitalid = generate_onehot(name)
        return onehot_hospitalid

def generate_onehot(name):
    unique_name = list(set(name));
    field2id = dict([(f, icnt) for icnt, f in enumerate(unique_name)]);
    retvec1 = []
    i=0
    for x in name:
        cid = field2id[x];
        retvec = np.zeros(len(field2id));
        retvec[cid] = 1;
        retvec1.append(retvec)
        if(i%100000==0):
            print i
        i+=1
        #print retvec1
    return retvec1


OneHotEncoder()