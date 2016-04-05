# coding=UTF-8
from __future__ import division
import re
import sys
from collections import *
import operator
from math import *



stop_words = ["", "a", "two", "i","able","about","above","abroad","according","accordingly","across","actually","adj","after","afterwards","again","against","ago","ahead","ain't","all","allow","allows","almost","alone","along","alongside","already","also","although","always","am","amid","amidst","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","a's","aside","ask","asking","associated","at","available","away","awfully","back","backward","backwards","be","became","because","become","becomes","becoming","been","before","beforehand","begin","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","came","can","cannot","cant","can't","caption","cause","causes","certain","certainly","changes","clearly","c'mon","co","co.","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","c's","currently","dare","daren't","definitely","described","despite","did","didn't","different","directly","do","does","doesn't","doing","done","don't","down","downwards","during","each","edu","eg","eight","eighty","either","else","elsewhere","end","ending","enough","entirely","especially","et","etc","even","ever","evermore","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","fairly","far","farther","few","fewer","fifth","first","five","followed","following","follows","for","forever","former","formerly","forth","forward","found","four","from","further","furthermore","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","had","hadn't","half","happens","hardly","has","hasn't","have","haven't","having","he","he'd","he'll","hello","help","hence","her","here","hereafter","hereby","herein","here's","hereupon","hers","herself","he's","hi","him","himself","his","hither","hopefully","how","howbeit","however","hundred","i'd","ie","if","ignored","i'll","i'm","immediate","in","inasmuch","inc","inc.","indeed","indicate","indicated","indicates","inner","inside","insofar","instead","into","inward","is","isn't","it","it'd","it'll","its","it's","itself","i've","just","k","keep","keeps","kept","know","known","knows","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","likewise","little","look","looking","looks","low","lower","ltd","made","mainly","make","makes","many","may","maybe","mayn't","me","mean","meantime","meanwhile","merely","might","mightn't","mine","minus","miss","more","moreover","most","mostly","mr","mrs","much","must","mustn't","my","myself","name","namely","nd","near","nearly","necessary","need","needn't","needs","neither","never","neverf","neverless","nevertheless","new","next","nine","ninety","no","nobody","non","none","nonetheless","noone","nor","normally","not","nothing","notwithstanding","novel","now","nowhere","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","one's","only","onto","opposite","or","other","others","otherwise","ought","oughtn't","our","ours","ourselves","out","outside","over","overall","own","particular","particularly","past","per","perhaps","placed","please","plus","possible","presumably","probably","provided","provides","que","quite","qv","rather","rd","re","really","reasonably","recent","recently","regarding","regardless","regards","relatively","respectively","right","round","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","shan't","she","she'd","she'll","she's","should","shouldn't","since","six","so","some","somebody","someday","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","that'll","thats","that's","that've","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby","there'd","therefore","therein","there'll","there're","theres","there's","thereupon","there've","these","they","they'd","they'll","they're","they've","thing","things","think","third","thirty","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","till","to","together","too","took","toward","towards","tried","tries","truly","try","trying","t's","twice","two","un","under","underneath","undoing","unfortunately","unless","unlike","unlikely","until","unto","up","upon","upwards","us","use","used","useful","uses","using","usually","v","value","various","versus","very","via","viz","vs","want","wants","was","wasn't","way","we","we'd","welcome","well","we'll","went","were","we're","weren't","we've","what","whatever","what'll","what's","what've","when","whence","whenever","where","whereafter","whereas","whereby","wherein","where's","whereupon","wherever","whether","which","whichever","while","whilst","whither","who","who'd","whoever","whole","who'll","whom","whomever","who's","whose","why","will","willing","wish","with","within","without","wonder","won't","would","wouldn't","yes","yet","you","you'd","you'll","your","you're","yours","yourself","yourselves","you've","zero"]  		
 
# Split text into sentences
def text_to_sentences(text):
    text = text.replace("\n", ". ")
    return text.split(". ")

 
# Split text into paragraphs
def text_to_paragraphs(text):
    return text.split("\n\n")

 
# Caculate the intersection between 2 sentences
#def sentences_intersection(sent1, sent2):
 
    # split the sentence into words/tokens
 #   s1 = set(sent1.split(" "))  
    #s2 = set(sent2.split(" "))
  #  s2 = set(sent2)
   # if (len(s1) + len(s2)) == 0:
    #    return 0
    #else: 
     #   return len(s1 & s2) / ((len(s1) + len(s2)) / 2)


 


 
"""
Title = " Reproducible research: Notes from the field " 
Title = 
paper = 
"Over the past year, I’ve been doing a lot of talking about reproducible research. Talking to people, talking on panel discussions, and talking about some of my own work. It seems to me that interest in the topic has exploded recently, in part due to some recent scandals, such as the Duke clinical trials fiasco.

If you are unfamiliar with the term “reproducible research”, the basic idea is that authors of published research should make available the necessary materials so that others may reproduce to a very high degree of similarity the published findings. If that definitions seems imprecise, well that’s because it is.

I think reproducibility becomes easier to define in the context of a specific field or application. Reproducibility often comes up in the context of computational science. In computational science fields, often much of the work is done on the computer using often very large amounts of data. In other words, the analysis of the data is of comparable difficulty as the collection of the data (maybe even more complicated). Then the notion of reproducibility typically comes down to the idea of making the analytic data and the computer code available to others. That way, knowledgeable people can run your code on your data and presumably get your results. If others do not get your results, then that may be a sign of a problem, or perhaps a misunderstanding. In either case, a resolution needs to be found. Reproducibility is key to science much the way it is key to programming. When bugs are found in software, being able to reproduce the bug is an important step to fixing it. Anyone learning to program in C knows the pain of dealing with a memory-related bug, which will often exhibit seemingly random and non-reproducible behavior."

My discussions with others about the need for reproducibility in science often range far and wide. One reason is that many people have very different ideas what (a) what is reproducibility and (b) why we need it. Here is my take on various issues.

    Reproducibility is not replication. There’s often honest confusion between the notion of reproducibility and what I would call a “full replication”. A full replication doesn’t analyze the same dataset, but rather involves an independent investigator collecting an independent dataset conducting an independent analysis. Full replication has been a fundamental component of science for a long time now and will continue to be the primary yardstick for measuring the plausibility of scientific claims. I think most would agree that full replication is preferable, but often it is simply not possible.

    Reproducibility is not needed solely to prevent fraud. I’ve heard many people emphasize reproducibility as a means to prevent fraud. Journal editors seem to think this is the main reason for demanding reproducibility. It is one reason, but to be honest, I’m not sure it’s all that useful for detecting fraud. If someone truly wants to commit fraud, then it’s possible to make the fraud reproducible. If I just generate a bunch of numbers and claim it as data that I collected, any analysis from that dataset can be reproducible. While demanding reproducibility may be useful for ferreting out certain types of fraud, it’s not a general solution and it’s not the primary reason we need it. 

    Reproducibility is not as easy as it sounds. Making one’s research reproducible is hard. It’s especially hard when you try to do it after the research has been done. In that case it’s more like an audit, and I’m guessing for most people the word “audit” is NOT synonymous with “fun”. Even if you set out to make your work reproducible from the get go, it’s easy to miss things. Code can get lost (even with a version control system) and metadata can slip through the cracks. Even when you’ve done everything right, computers and software can change. Virtual machines like Amazon EC2 and others seem to have some potential. The single most useful tool that I have found is a good version control system, like git. 
    At this point, anything would be better than nothing. Right now, I think the bar for reproducibility is quite low in the sense that most published work is not reproducible. Even if data are available, often the code that analyzed the data is not available. So if you’re publishing research and you want to make it at least partially reproducible, just put what you can out there. On the web, on github, in a data repository, wherever you can. If you can’t publish the data, make your code available. Even that is better than nothing. In fact, I find reading someone’s code to be very informative and often questions can arise without looking at the data. Until we have a better infrastructure for distributing reproducible research, we will have to make do with what we have. But if we all start putting stuff out there, the conversation will turn from “Why should I make stuff available?” to “Why wouldn’t I make stuff available?”
"""

def word_frequency(text):
    freq_dict = defaultdict(int)
    words = text.split(" ")
    words = [x.lower() for x in words]
    words = [re.sub('[^a-z]', '', word) for word in words]
    max_freq = 0
    for word in words:
        if not(word in stop_words):
            freq_dict[word] += 1
    #return len(freq_dict)
    if len(freq_dict) != 0:
        max_freq = max(freq_dict.iteritems(), key=operator.itemgetter(1))[1]
        for w in freq_dict.keys():
            freq_dict[w] = freq_dict[w]/max_freq
        return freq_dict
    else:
        return freq_dict
        
    


def sentences_intersection(sent1, sent2):
    s1 = word_frequency(sent1)
    s2 = word_frequency(sent2)
    key1 = s1.keys()
    key2 =  s2.keys()
    if (len(key1) ==0) or (len(key2) == 0):
        return 0
    else:
        sum1sq = sum([pow(s1[w],2) for w in key1])
        sum2sq = sum([pow(s2[w],2) for w in key2])
        common_keys = set(key1) & set(key2)
        dot_product = sum([s1[w]*s2[w] for w in common_keys])
        sim = dot_product/(sqrt(sum1sq)*sqrt(sum2sq))
        return sim



def centroid(text):        
    tf = word_frequency(text)
    tf = sorted(tf.iteritems(), key=operator.itemgetter(1), reverse=True)
    central_sentence = ""
    thematic_words = []
    i = 0
    while (i < 8):
        u, v = tf[i]
        thematic_words.append(u)
        i = i + 1
    for x in thematic_words:
        central_sentence = central_sentence + " " + str(x)
    return central_sentence

def paragraph_centroid_similarity(paragraph, central_sentence):
    centroid_sim = {}
    sentences = text_to_sentences(paragraph)
    n = len(sentences)
    if (n < 0):
        centroid_sim = {s:0 for s in sentences} 
    for s in sentences:
        #strip_s = format_sentence(s)
        score = sentences_intersection(s, central_sentence)
        centroid_sim[s] = score
    return centroid_sim    


def sentence_similarity(text):
 
    # Split into sentences
    sentences = text_to_sentences(text)
 
    # Calculate the intersection of every two sentences
    n = len(sentences)
    values = [[0 for x in xrange(n)] for x in xrange(n)]
    for i in range(0, n):
        for j in range(0, n):
            values[i][j] = sentences_intersection(sentences[i], sentences[j])
 
    # Build the sentence-rank dictionary
    # The score of a sentences is the sum of all its intersection
    sentences_dic = {}
    for i in range(0, n):
        score = 0
        for j in range(0, n):
            if i == j:
                continue
            score += values[i][j]
        sentences_dic[sentences[i]] = score
    return sentences_dic        


def similarity_with_title(text, title):
    sentences = text_to_sentences(text)
    title_similarity = {}
    for s in sentences:
        score = sentences_intersection(s,title)
        title_similarity[s] = score
    return title_similarity   



# Return the best sentence in a paragraph
def best_sentence(paragraph, sentences_dic, centroid_similarity, title_similarity): 
    # Split the paragraph into sentences
    sentences = text_to_sentences(paragraph)
 
    # Ignore short paragraphs
    if len(sentences) < 2:
        return ""
 
    # Get the best sentence according to the sentences dictionary
    best_sentence = ""
    max_value = 0
    for s in sentences:
        #strip_s = format_sentence(s)
        if (sentences_dic[s] + centroid_similarity[s] + title_similarity[s]) > max_value:
            max_value = sentences_dic[s] + centroid_similarity[s] + title_similarity[s]
            best_sentence = s
 
    return best_sentence



def summary(text, title):
    central_sentence = centroid(text)
    paragraphs = text_to_paragraphs(text)
    sentence_dic = sentence_similarity(text)
    if (title != None):
        title_similarity = similarity_with_title(text, title)
    else:
        title_similarity = {s:0 for s in sentence_dic.keys()}
    summary = []
    for p in paragraphs:
        centroid_similarity = paragraph_centroid_similarity(p, central_sentence)
        sentence = best_sentence(p, sentence_dic, centroid_similarity, title_similarity)
        summary.append(sentence)
    return ("\n").join(summary)   
        

#central_sentence = centroid(paper)       
#print summary(paper, Title)
#print similarity_with_title(paper, Title)
#dott = text_to_paragraphs(paper)[6]
#centroid_similarity = paragraph_centroid_similarity(dott, central_sentence)
#sentences_dic = sentence_similarity(paper)
#title_similarity = similarity_with_title(paper, Title)
#print best_sentence(dott, sentences_dic, centroid_similarity, title_similarity)


#sentences = text_to_sentences(paper)
#for s in sentences:
 #   print word_frequency(s)

if __name__ == "__main__":

    title = sys.argv[1]
    paper = sys.argv[2]
    print summary(paper, title)
