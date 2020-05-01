file = open("E-TABM-185.sdrf.txt")
file.readline()
file2 = open("nf.txt", 'w')
HYB = "Hyb_"
hybPos = 0
wordExist = False
wordResult = ""

listwords = ["cancer", "myositis", "adenoma", "glioblastoma", "periodontitis", "asthma", "fibrillation", "myocardium", "sclerosis", "calpainopathy", "relapse", "paraplegia", "dysferlinopathy", "adenovirus", "Disease", "hnscc", "aml", "cardiomyopathy", "rejection", "pc3", "skmel5", "infarction", "esophagus", "disorder", "emphysema", "epithelia", "osteosarcoma", "adenovirus","dystrophy", "trauma", "Ischemia", "bipolar disorder", "ebv", "hyperparathyroidism", "metastasis", "dermatomyositis", "mcf7", "hl60", "pcos", "mcf10a", "lymphoma", "meningitis", "tumor", "glioblastoma", "fibrosis", "syndrome", "adenocarcinoma", "leukemia", "rhabdomyosarcoma", "KSHV", "AIDS", "XLA", "CVID", "neuroblastoma"]

for row in file:
    if HYB in row:
        hybPos = row.find(HYB)
        hybResult = row[hybPos:-1]
        hybResult = hybResult.split()
        hybResult = hybResult[0]
        #print(hybResult)
    else:
        hybResult = "ERRORE"
    for word in listwords:
        if word in row:
            wordPos = row.find(word)
            wordElemento = row[wordPos-10:wordPos+40].strip()
            wordResult = wordResult +  " | " + wordElemento
            wordExist = True
    if wordExist:
        file2.write(hybResult + " " + wordResult + "\n")
    else:
        file2.write(hybResult + " None\n")
    wordResult = ""
    wordExist = False
