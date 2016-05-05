"""

PDF to json Parser

@author: Namita Maharanwar
@email: namitamaharanwar@gmail.com
5 May, 2016


"""


import slate
import re
import json
import unidecode


def parse_pdf_using_slate(filepath):
    """
    Parses the PDF file and returns its text in json format.
    :input: filepath: PDF file path which you want parse.
    :output: returns and creats a json file containg the text from PDF.
    """
    all_questions = []
    with open(filepath) as f:
    	document = slate.PDF(f)

    count = 0 
    for each_page in document:
    	questions = re.split(r"\d+[.]", unidecode.unidecode_expect_nonascii(each_page))
    	for each in questions:
            # print each
	    splited_question = each.split("(A")
            count = count + 1
	    try:
                question_dict = {}
            	if splited_question[0] != "":
            	    question_dict["question_statement"] = splited_question[0]
            	    question_dict["answer_options"] = "(A" + splited_question[1]
                    all_questions.append(question_dict)
	    except:
                pass  # clock 9.50 pattern fails
    with open("data/parsed_questions.json", "w") as q_file:
	json.dump(all_questions, q_file, indent=4)
    return all_questions

if __name__ == "__main__":
    parse_pdf_using_slate("data/SSC_paper_1.pdf")
