from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize_text(text, num_sentences=5, algorithm='lsa'):
    if len(text.split()) < 10:
        return "Text is too short to summarize"
    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    if algorithm == 'lsa':
        summarizer = LsaSummarizer()
    elif algorithm == 'lex_rank':
        summarizer = LexRankSummarizer()
    elif algorithm == 'text_rank':
        summarizer = TextRankSummarizer()
    else:
        summarizer = LsaSummarizer()
    
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)
