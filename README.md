Overview
This script is designed to transcribe variants from p. nomenclature format to c. nomenclature format. It takes a DNA sequence in text format, a list of codons positions to check, and a list of mutant amino acids correspondent to the positions as inputs. It then searches the missense mutations based on the provided codons and amino acids and outputs a file with the c. nomenclatures.

Usage
Input Files
DNA Sequence (FASTA format): Provide the DNA sequence file where 'U' is converted to 'T' if applicable. This sequence will be used for analysis.
List of Codons: Input a list of codons to check, with one codon per line. The script will analyze these specific codons from the DNA sequence.
List of Mutant Amino Acids: Input a list of mutant amino acids to check, with one amino acid per line. The script will search for mutations leading to these amino acid changes.
Output File
The script generates an output file with potential missense mutations in cDNA nomenclature format. Each line in the output corresponds to a codon from the input list and contains the potential missense mutations for that codon.

Command Line Execution
Ensure you have Python installed on your system. Execute the script from the command line using the following syntax:

bash
Copy code
python script_name.py <input_fasta_file> <list_of_codons_file> <list_of_mutant_amino_acids_file> <output_file_name>
Replace script_name.py with the actual name of the script file and provide the appropriate input files and output file name.

Configuration for Galaxy Platform
The XML file provided with the project is configured to run the script on the Galaxy platform. Galaxy is a web-based platform for data-intensive biomedical research. This XML file specifies the inputs, outputs, and parameters required to integrate the script into the Galaxy environment.
