# read me

Create the index.html file from the index.md file using this pandoc command:

`pandoc index.md -f markdown -t html -s -o index.html --template "./template.html" --metadata title="Little Free Language Models"`

Based on [https://github.com/ProbablePrime/pandoc-water.css].