file = open("GPL96-15653.txt")
listwords = ["cancer", "diabetes", "disease", "neuropathy"]

nf = open("nf.txt", 'w')

for row in file:
    for word in listwords:
        temp = row.split()
        if row[0] == "#" or row[0:2] == "ID":
            pass
        elif word in row:
            i = row.find(word)
            #nf.write(temp[0] + " " + row[i - 4] + " " + row[i - 3] + " " + row[i - 2] + " " + row[i - 1] + " " + row[i] + " " + row[i + 1] + " " + row[i + 2])
            nf.write(temp[0] + " " + row[i-25:i+len(word)+16] + "\n")
        else:
            nf.write(temp[0] + " None\n")
            
            #ONCE THE DATASET HAS BEEN CLEANED
           
 #CREATE AND FILL A NEW CLEAN FILE


file = open("GPL96-15653.txt")
listwords = ["DiGeorge syndrome", "hyper-IgM syndrome", "Crouzon syndrome", "myelodysplasia syndrome 1", "Lowe oculocerebrorenal syndrome", "stiff man syndrome", "nephrogenic diabetes", "lung and esophageal cancer", "macular dystrophy", "QT syndrome 3", "Pendred syndrome", "Waardenburg syndrome 1", "hyper-IgM syndrome", "Williams Beuren syndrome", "cancertestis antigen 2", "Williams-Beuren syndrome", "McLeod syndrome", "Norrie disease", "McArdle syndrome", "Morquio syndrome", "Werner syndrome", "Canavan disease", "Angelman syndrome", "colorectal cancers", "skin fragility syndrome", "Bloom syndrome", "Duncans disease", "hemophilia B", "Machado-Joseph disease", "glycogen storage disease type I", "Liddle syndrome", "glycogen storage disease type V", "Ellis-van Creveld syndrome", "Usher syndrome", "Menkes syndrome", "Stiff-Mann syndrome", "Lafora disease", "renal cancer", "brain-testis-cancer antigen", "Putative prostate cancer tumor suppressor", "alpha thalassemiamental retardation syndrome", "Hirschprung disease", "Hodgkins disease", "Meckel syndrome", "giant axonal neuropathy", "cancertestis specific", "putative prostate cancer susceptibility", "Alagille syndrome", "Kallmann syndrome", "Wolf-Hirschhorn syndrome candidate", "Thomsen disease", "Wernicke-Korsakoff syndrome"
             ,"cephalopolysyndactyly syndrome", "Rubinstein-Taybi syndrome", "Zellweger syndrome", "liver cancer", "autoimmunogenic cancertestis antigen", "Charcot-Marie-Tooth neuropathy", "von Recklinghausen disease", "Hunter syndrome", "Alzheimer disease 3", "Alzheimer disease 4", "Collins-Franceschetti syndrome", "Cockayne syndrome", "ceroid-lipofuscinosis", "Crouzon syndrome" , "Pfeiffer syndrome", "Sanfilippo disease IIID" ,"Ehlers-Danlos syndrome type IV", "Chediak-Higashi syndrome 1", "Ras-related associated with diabetes (RRAD)", "Deleted in split-handsplit-foot 1", "Mast syndrome", "McKusick-Kaufman syndrome", "Aarskog-Scott syndrome", "Dent disease", "OpitzBBB syndrome", "MASA", "Smith-Magenis syndrome", "Li-Fraumeni syndrome", "Andersen disease", "Hermansky-Pudlak syndrome", "oral cancer", "Refsum disease", "Down syndrome", "oculocerebrorenal syndrome of Lowe", "Nijmegen breakage syndrome", "oral-facial-digital syndrome", "mental retardation syndrome", "velocardiofacial syndrome", "lung cancer candidate", "colon cancer, nonpolyposis type 2", "colon cancer antigen 8", "colon cancer antigen 16", "colon cancer antigen 7", "esophageal cancer", "prostate cancer", "colon cancer antigen 3", "lung cancer", "Lesch-Nyhan syndrome", "putative prostate cancer", "colon cancer", "Rett syndrome", "Wiskott-Aldrich syndrome", "Pompe disease", "Marfan syndrome", "Jackson-Weiss syndrome", "Osler-Rendu-Weber syndrome 1", "Greig cephalopolysyndactyly syndrome", "Ehlers-Danlos syndrome type VI", "Hirschsprung disease", "Jansky-Bielschowsky disease", "bladder cancer", "Sjogren syndrome", "diabetes"
             ,"Niemann-Pick disease type C1", "Peutz-Jeghers syndrome", "Barth syndrome" ,"fibroelastosis 2",
             "neurofibromatosis type 1", "neurofibromatosis type 2", "Niemann-Pick disease type C2",
             "Pelizaeus-Merzbacher disease", "Prader-Willi/Angelman syndrome", "Saethre-Chotzen syndrome",
             "Prader-Willi syndrome", "turban tumor syndrome", "Alport syndrome", "Troyer syndrome",
             "paraneoplastic cancer", "breast and ovarian cancer susceptibility ", "ovarian cancer",
             "Alzheimer disease", "Parkinson disease", "neuropathy", "Watson disease", "Krabbe disease",
             "von Hippel-Lindau syndrome", "Graves disease", "Batten, Spielmeyer-Vogt disease", "Bardet-Biedl syndrome",
             "polycystic kidney disease 2", "fatal familial insomnia", "Wolman disease",
             "chronic granulomatous disease", "polycystic kidney disease 1", "maple syrup urine disease",
             "Huntingtons disease", "Kennedy disease", "variant metachromatic leukodystrophy",
             "variant Gaucher disease", "Gerstmann-Strausler-Scheinker syndrome", "breast cancer 1", "ovarian cancer 1",
             "breast cancer anti-estrogen resistance", "multiple advanced cancers 1", "Hermansky-Pudlak syndrome",
             "velocardiofacial syndrome", "Hers disease", "Nijmegen breakage syndrome 1"]

nf = open("nf.txt", 'w')

for row in file:
    result = "" #Such variable starts as null
    wordExist = False #Such variable is false by default
    temp = row.split() #It will split a string into a list
    if row[0] != "#" and row[0:2] != "ID":
        for word in listwords:
            if word in row:
                i = row.find(word) 
                result += " | " + row[i:i + len(word)]
                wordExist = True #if that condition happens the wordexist condition will become from false to true
        if wordExist: #Such condition will happen only for a certain condition
            nf.write(temp[0] + " " + result + "\n")
        else:
            nf.write(temp[0] + " None\n") #If the condition for word in row is not respected
