import sys

nucleotidemap = {
'G':['GGT','GGC','GGA','GGG'],
'E':['GAG','GAA'],
'D':['GAC','GAT'],
'A':['GCG','GCA','GCC','GCT'],
'V':['GTG','GTA','GTC','GTT'],
'R':['AGG','AGA','CGG','CGA','CGC','CGT'],
'S':['AGC','AGT','TCG','TCA','TCC','TCT'],
'K':['AAG','AAA'],
'N':['AAC','AAT'],
'T':['ACG','ACA','ACC','ACT'],
'M':['ATG'],
'I':['ATA','ATC','ATT'],
'Q':['CAG','CAA'],
'H':['CAC','CAT'],
'P':['CCG','CCA','CCC','CCT'],
'L':['CTG','CTA','CTC','CTT','TTG','TTA'],
'W':['TGG'],
'C':['TGC','TGT'],
'Y':['TAC','TAT'],
'F':['TTC','TTT'],
'Stop':['TGA', 'TAG', 'TAA']
}

if len(sys.argv) != 5:
    sys.exit(1)

cDNASeq = []
with open(sys.argv[1]) as f: #Load your FASTA sequence here (Obs: Change 'U' to 'T', if it is the case)
    for line in f:
        line = line.rstrip()
        for letter in line:
            cDNASeq.append(letter)

listOfCodons=[]
with open(sys.argv[2]) as f: #Load the list of codons you want to check (Obs: It should be one codon per line)
    for line in f:
        line = line.rstrip()
        listOfCodons.append(line)

listOfChanges=[]    
with open(sys.argv[3]) as f: #Load the list of mutant aminoacid you want to check (Obs: It should be one mutant aminoacid per line)
    for line in f:
        line = line.rstrip()
        listOfChanges.append(line)

index = 0
file = open(f'{sys.argv[4]}.txt', "w")
for codonLocation in listOfCodons:
    arrayOfcNomenclature = []
    analyze = int(codonLocation) * 3 #for example if listOfCodons [1,2,3], then codon location = 1; 1*3 = 4 
    threeBasePair = str(cDNASeq[analyze-3]+cDNASeq[analyze-2]+cDNASeq[analyze-1]) #the three base pair should be the first 3 letters of cDNA (AUG)
    listOfPossibleChanges = nucleotidemap[listOfChanges[index]] #ListofPossibleChanges is the list of aminoacids changes we are querying on; for example "I", which map to 'I':['AUA', 'AUC', 'AUU'],
    for possibleChange in listOfPossibleChanges: #Iterate over all possibilities on the array
        indexOfDifferences = ([i for i in range(len(possibleChange)) if possibleChange[i] != threeBasePair[i]])#Points out the indexes where there are differences; for example AUG(origin) is different from AUA at index 2.
        if len(indexOfDifferences) == 1: #If the number of differences is equal to one, then is a missense 
            arrayOfcNomenclature.append("c."+ str(analyze - (-1*(indexOfDifferences[0]-2)))+ str(threeBasePair[indexOfDifferences[0]])+">"+ str(possibleChange[indexOfDifferences[0]]))#print out the nomenclature      
    index += 1
    file.write(str(arrayOfcNomenclature) +"\n")
file.close()
