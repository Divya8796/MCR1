import re

evidence_str = "_EVIDENCE_"
path = 'F:\\Divya\\MCR\\Data\\Final Data\\'
fo = open(path + 'MCR_Data.csv', 'r')


def preprocessing_evidence():
    fo = open(path + 'MCR_Data.csv', 'r')
    fw = open(path + 'new_evidence.csv', 'w')
    result = []
    for line in fo:
        line = line.replace('\n', '').strip()
        sp = line.split('|')
        evidence = sp[0]
        evidence = evidence.strip('\"\"')
        str_without_evi = evidence_remove(evidence)
        rename_str = rename_hiv(str_without_evi)
        clean_evidence = clean_unnecessary_data(rename_str)
        fw.write(str(clean_evidence) + "\n")
        result.append(str(clean_evidence))
    fw.close()
    return result


def clean_unnecessary_data(evidence):
    clean_Data = re.sub("[^a-zA-Z0-9]", " ", str(evidence))
    return clean_Data


def evidence_remove(evidence):
    if (evidence.find(evidence_str) > 0):
        word = evidence.split("_EVIDENCE_")
        # print word
        len_word = len(word)
        i = 0
        first_word = word[0]
        while (i < len_word and (i + 1) != len_word):
            if (word[0].upper() == word[i + 1].upper()):
                i += 1
                continue
            elif (first_word.upper().find(word[i + 1].upper()) >= 0):  # do something
                i += 1
                continue
            elif (word[i + 1].upper().find(first_word.upper()) >= 0):
                first_word = word[i + 1]
                i += 1
                continue
            else:
                first_word = first_word + " " + word[i + 1]
            i += 1
        return first_word.upper()
    else:
        return evidence.upper()


def rename_hiv(remove_evidence):
    if (re.match(r'^[+]$', str(remove_evidence), )):
        return "POSITIVE"
    elif (re.match(r'^[-]$', str(remove_evidence), )):
        return "NEGATIVE"
    elif (re.match(r'^[+].HIV$|^HIV.[+]$', str(remove_evidence), )):
        return "HIV POSITIVE"
    elif (re.match(r'^[-].HIV$|^HIV.[-]$', str(remove_evidence), )):
        return "HIV NEGATIVE"
    else:
        return remove_evidence


def copy(result_evidence, result_sectionname):
    fo = open(path + 'MCR_Data.csv', 'r')
    fw = open(path + 'clean_Data.csv', 'w')
    i = 0

    for line in fo:
        line = line.replace('\n', '').strip()
        sp = line.split('|')
        evidence = result_evidence[i]
        section_name = result_sectionname[i]
        i += 1
        l = evidence + "|" + "|".join(sp[1:3]) + "|" + section_name + "|".join(sp[5:]) + "\n"
        fw.write(l)
    fw.close()


def preprocessing_sectionname():
    result = []
    j = 0;
    fo = open(path + 'MCR_Data.csv', 'r')
    fw = open(path + 'new_section_name.csv', 'w')
    for line in fo:
        line = line.replace('\n', '').strip()
        sp = line.split('|')
        section_name = sp[4]
        section_name = section_name.strip('" "')
        clean_section_name = clean_unnecessary_data(section_name)
        fw.write(str(clean_section_name).upper() + "\n")
        result.append(str(clean_section_name).upper())
    fw.close()
    return result


def preprocessing():
    result_evidence = preprocessing_evidence()
    result_sectionname = preprocessing_sectionname()
    copy(result_evidence, result_sectionname)
    return


preprocessing()