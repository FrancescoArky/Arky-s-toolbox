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

    
    
    
    
    
    file = open("E-TABM-185.sdrf.txt")
file.readline()
file2 = open("nf4.txt", 'w')
HYB = "Hyb_"
hybPos = 0
wordExist = False
wordResult = ""

listwords = ["brain tumor","lymphoma","lung cancer, cytotoxicity","cololrectal tumor","bone marrow relapse","primary progeria syndrome","cardiomyopathy","cardiomyopathy, calcifications","metastasis","cockayne syndrome","hereditary spastic paraplegia","calpainopathy","limb-girdle muscular dystrophy type 2I","Emery-Dreifuss muscular dystrophy","calpainopathy","dysferlinopathy","amyotrophic lateral sclerosis","becker muscular dystrophy","adrenal gland metastasis","germ cell tumor","t4a, bladder tumor","t3a, bladder tumor","t4b, bladder tumor","t3b, bladder tumor","bladder tumor","carcinoma in situ, bladder tumor","primary breast cancer","brain tumor, glioblastoma","periodontitis","metastatic colon cancer","primary colon cancer","glioblastoma","irritable bowel syndrome","primary prostate cancer","primary uterated prostate cancer","pulmonary disease, cystic fibrosis","acute lymphoblastic leukemia, chemotherapy response","lymph node metastasis	squamous cell carcinoma","atrial fibrillation","lung cancer","atopic severe asthma","non-atopic mild asthma","atopic mild asthmatics","pituitary adenoma, PRL-secreting","pituitary adenoma, GH-secreting","pituitary adenoma, ACTH-secreting","pituitary adenoma, non-functioning","polymyositis","dermatomyositis","myositis","acute rejection", "pre-LVAD	nonischemic cardiomyopathy","pre-LVAD	ischemic cardiomyopathy","aml","grade 2, primary hnscc","acute monoblastic/monocytic leukemia","emphysema","B-cell acute lymphoblastic leukemia, B-ALL","T-cell acute lymphoblastic leukemia, T-ALL","T-cell lymphoblastic lymphoma, T-LL","breast cancer, inflammatory","mitochondrial disorder","adenocarcinoma","barrett's esophagus","colorectal cancer","breast cancer cells, adenovirus expressing GFP","acute myeloid leukemia","metabolic syndrome","bronchial epithelia","myocardial infarction","Ischemia","trauma","ebv infection","bipolar disorder","juvenile dermatomyositis","duchenne muscular dystrophy","facioscapulohumeral muscular dystrophy","dermatomyositis","pcos","lymph node metastasis breast tumor","breast tumor, normal like","breast tumor, basal","breast tumor, luminal","breast tumor","meningitis infected","cystic fibrosis","B-cell lymphoma, nhl","B-cell lymphoma, dlbcl","B-cell lymphoma","neuroblastoma cells high-stage neuroblastoma","neuroblastoma cells embryo high-stage neuroblastoma","neuroblastoma cells embryo low-stage neuroblastoma","neuroblastoma cells low-stage neuroblastoma","chronic myeloid leukemia","T cell acute lymphoblastic leukemia","SK-N-SH	neuroblastoma","Burkitt's lymphoma","precursor T lymphoblastic leukemia","prostate cancer","malignant peripheral nerve sheath tumor","osteosarcoma","adenocarcinoma mammary gland","lung adenocarcinoma (NCI_Thesaurus C0152013) has DiseaseStaging Stage IV","lung adenocarcinoma (NCI_Thesaurus C0152013) has DiseaseStaging Stage III","lung adenocarcinoma (NCI_Thesaurus C0152013) has DiseaseStaging Stage II","lung adenocarcinoma (NCI_Thesaurus C0152013) has DiseaseStaging Stage I","Raji Burkitt's lymphoma","colorectal adenocarcinoma","Daudi Burkitt's lymphoma","lymphoblastic leukemia MOLT-4","chronic myelogenous leukemia K562","promyelocytic leukemia HL-60","Huntington's Disease (HD) Pathological Grade 0","Huntington's Disease (HD) Pathological Grade 1","Huntington's Disease (HD) Pathological Grade 4","Huntington's Disease (HD) Pathological Grade 3","Huntington's Disease (HD) Pathological Grade 2","colon adenocarcinoma","acute promyelocytic leukemia","alveolar rhabdomyosarcoma","embryonal rhabdomyosarcoma","acute lymphoblastic leukemia","KSHV infection, 14 days","KSHV infection, 7 days","KSHV infection, 2 days","iatrogenic-KS, KSHV-","AIDS-KS, KSHV-","AIDS-KS, HIV+, nodular (late) stage","colon carcinoma","follicular thyroid adenoma","follicular thyroid carcinoma","XLA", "CVID", "neuroblastoma-differentiating", "ganglioneuroblastoma intermixed", "ganglioneuroblastoma", "neuroblastoma-poorly differentiated","Down syndrome, transient myleoproliferative disorder", "Down syndrome, acute megakaryoblastic leukaemia","Down syndrome, non-leukaemic"]


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
            wordElemento = row[wordPos:wordPos+len(word)].strip()
            if wordElemento not in wordResult:
                wordResult = wordResult + " | " + wordElemento
                wordExist = True
        if wordExist:
            file2.write(hybResult + " " + wordResult + "\n")
    else:
        file2.write(hybResult + " None\n")
    wordResult = ""
    wordExist = False
