# pdf-parser

This is sample PDF parser specific to the certain PDF files. I have used one of the open source libraries for parsing PDFs
called slate. 

Running Instructions: `\n`
1. If you already `virtualenv` set up and if `pdfminer` is already installed, then I would suggest you to setup a seperate
   `virtualenv`, as `slate` lib internally used `pdfminer` and there are some version issues with `pdfminer`. So, its better to keep 
   this seperate.
2. Install requiremnets.txt using `pip install -r requirements.txt` command.
3. Now run `python slate_parser.py`.
4. You can find output file at `data/all_questions.json` path.
