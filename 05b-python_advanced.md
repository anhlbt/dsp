## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> There are 8 different degrees.

>> |         |   count |
|:--------|--------:|
| Ph.D.   |      32 |
| Sc.D.   |       6 |
| M.P.H.  |       2 |
| M.S.    |       2 |
| B.S.Ed. |       1 |
| J.D.    |       1 |
| M.D.    |       1 |
| M.A.    |       1 |

>> The missing degree could be readily determined from external sources, so I added it. (There is also a method for scraping the UPenn data in [advanced_python_scraping.py](python/advanced_python_scraping.py).) However, if the degree could not be determined, I would have omitted it from this analysis and then noted that there was one piece of missing data.

>> For individuals who have multiple degrees, each degree was counted separtely.

>> For cleaning the degrees, it would have been simpler to strip all periods, but I enjoy regular expressions, so I decided to write one that would add all appropriate periods.

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> There are 3 different faculty titles.

>> |                     |   count |
|:--------------------|--------:|
| Professor           |      13 |
| Associate Professor |      12 |
| Assistant Professor |      12 |

>> Titles were cleaned by removing department afilliation. 

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> [bellamys@mail.med.upenn.edu,  
 warren@upenn.edu,  
 bryanma@upenn.edu,  
 jinboche@upenn.edu,  
 sellenbe@upenn.edu,  
 jellenbe@mail.med.upenn.edu,  
 ruifeng@upenn.edu,  
 bcfrench@mail.med.upenn.edu,  
 pgimotty@upenn.edu,  
 wguo@mail.med.upenn.edu,  
 hsu9@mail.med.upenn.edu,  
 rhubb@mail.med.upenn.edu,  
 whwang@mail.med.upenn.edu,  
 mjoffe@mail.med.upenn.edu,  
 jrlandis@mail.med.upenn.edu,  
 liy3@email.chop.edu,  
 mingyao@mail.med.upenn.edu,  
 hongzhe@upenn.edu,  
 rlocalio@upenn.edu,  
 nanditam@mail.med.upenn.edu,  
 knashawn@mail.med.upenn.edu,  
 propert@mail.med.upenn.edu,  
 mputt@mail.med.upenn.edu,  
 sratclif@upenn.edu,  
 michross@upenn.edu,  
 jaroy@mail.med.upenn.edu,  
 msammel@cceb.med.upenn.edu,  
 shawp@upenn.edu,  
 rshi@mail.med.upenn.edu,  
 hshou@mail.med.upenn.edu,  
 jshults@mail.med.upenn.edu,  
 alisaste@mail.med.upenn.edu,  
 atroxel@mail.med.upenn.edu,  
 rxiao@mail.med.upenn.edu,  
 sxie@mail.med.upenn.edu,  
 dxie@upenn.edu,  
 weiyang@mail.med.upenn.edu]

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> There are 4 different email domains.

>> [mail.med.upenn.edu,  
 upenn.edu,  
 email.chop.edu,  
 cceb.med.upenn.edu]

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

>> **NOTE:** My code functions make use of two external files:

>> * One the performs data cleaning: [advanced_python_cleaning.py](python/advanced_python_cleaning.py)
* And an optional one (written for fun) that will scrape the UPenn faculty webpage for missing information: [advanced_python_scraping.py](python/advanced_python_scraping.py)


---

###Part II - Write to CSV File

####Q5. Write email addresses from Part I to csv file.

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

>> The first ten lines of the email.csv file are:

>> [bellamys@mail.med.upenn.edu,  
 warren@upenn.edu,  
 bryanma@upenn.edu,  
 jinboche@upenn.edu,  
 sellenbe@upenn.edu,  
 jellenbe@mail.med.upenn.edu,  
 ruifeng@upenn.edu,  
 bcfrench@mail.med.upenn.edu,  
 pgimotty@upenn.edu,  
 wguo@mail.med.upenn.edu]

---

### Part III - Dictionary

####Q6. Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> {Putt   : [['Ph.D. Sc.D.', 'Professor', 'mputt@mail.med.upenn.edu']],  
  Feng   : [['Ph.D.', 'Assistant Professor', 'ruifeng@upenn.edu']],  
  Bilker : [['Ph.D.', 'Professor', 'warren@upenn.edu']]}



####Q7. The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>> {('Yimei', 'Li')         : ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],  
 ('Hongzhe', 'Li')       : ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'],  
 ('Knashawn', 'Morales') : ['Sc.D.', 'Associate Professor', 'knashawn@mail.med.upenn.edu']}

>> **NOTE**: my dictionary is not printing as sorted by first name, but this is likely due to differences in the dictionary creation method since dictionary keys aren't inherently sorted anyway. I'm creating my dictionary by converting from a Pandas dataframe.



####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> {('Scarlett', 'Bellamy') : ['Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu'],  
 ('Warren', 'Bilker')    : ['Ph.D.', 'Professor', 'warren@upenn.edu'],  
 ('Matthew', 'Bryan')    : ['Ph.D.', 'Assistant Professor', 'bryanma@upenn.edu']}


Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)


--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

>> Sample text produced from `markov.py markov_trump_gop_debate_transcripts.txt 200`:

>> People are coming in favor of people in the world. We pay more business tax, and I was saying do it but if I am elected dog catcher right the lead plaintiff signed a letter saying how great company. But they are also great love for clothingmakers in this. If these countries, and other hotels in charge of amnesty, he was a little bit of an apology from Ted. Was listening, to, that now for the makebelieve, Chris will tell you have to speak, is taking our jobs. Have just been a lot stronger military, much evolved. And to make America. So I also happened to endorse me is an incident done, is made -- New York, a very nice, and they do not just with respect them greatly. And on budget. It out, you -- they devalue their currencies. That makes absolutely no -- problems, no longer defend all, Marco said under no circumstances will I run, that I raised million for this man, on borders is the best by senators and congressmen. They have to tell me, audit me because I said it loud and insurance lobbyists, and donors that works out I may have discussed that subject. Of conversation by everybody, which

>> **NOTE:** My code makes use of three external files:

>> * A Python library that facilitated scraping the transcripts from the web [markov_text_download.py](python/markov_text_download.py). Note that this code is not needed for running the program and I did not upload the raw text.
* The transcripts from the GOP Presidential Debates for the 2016 election with Donald Trump's portion only: [markov_trump_gop_debate_transcripts.txt](python/markov_trump_gop_debate_transcripts.txt)
* A file that creates the required weighted n-gram tables from the cleaned text: [markov_table_creation.py](python/markov_table_creation.py)

>> **Design decisions and discussion:** 

>> The downloaded transcripts were cleaned in the following way:

>> * All text other than that from Donald Trump was removed.
* Remaining text was combined into a single, continuous file.
* With the exception of possessive forms of words, all contractions were converted to their expanded (proper) form. This was intended to improve accuracy of the statistics. Without cleaning, `I'm` and `I am` would be considered different by the model.
* Possesive forms of words were maintained, although in some cases the apostrophe was inadvertently removed. Efforts were made to remedy this mistake, but missing apostrophes may persist.
* All punctuation (`.` `,` `;` `!` `?` `--`) was retained but tokenized separately from the words themselves. Within the cleaned text file, spaces were added between all punctuation marks to facilitate tokenization. Unecessary spaces were cleaned from the final text.
* With the exception of proper nouns and acronyms, all words were converted to their lower case forms. This was intended to further improve accuracy of the probability distribution used by the model. Every effort was made to clean the proper nouns, but as this text contains MANY proper nouns (a downside of using political speeches), there may be words which were errantly not capitalized.

>> Design decisions were also made with regards to n-gram and model creation:


>> * Tokenized punctuation was not counted as part of the requested word count.
* Tokenized text was also ignored when the next n-gram was chosen. Instead, the non-punctuation word closest to the end of the nascent text list was chosen. This was done since the flow of text likely depends more on the previous (real) word than on punctuation.
* Rather than retaining duplicate copies of n-grams as a means of representing a distribution and then randomly selecting from them, I decided to use a discrete distribution sampler from SciPy (`rv_discrete`). Besides affording me the opportunity to learn how it works, there are some potential advantages for very large corpora with regards to memory useage. 
* The standard method of creating a text Markov chain model with Python usually involves dictionaries, and I read through several of them online. I decided to use Pandas for fun. There are both potential upsides and downsides with regards to memory usage and speed for very large models, but more testing would be needed to fully understand them. Pandas did have some advantages with regards to normalizing the data for the discrete distribution sampler used.
* To further improve accuracy, one could use larger n-gram models and/or longer sequences of words to select the next n-gram. The downside is that more stringent models will tend to simply pull out the original text.





