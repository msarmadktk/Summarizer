from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text):
    if len(text.split()) < 10:  # Ensure the text is long enough
        return "Text is too short to summarize"
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 10)  # Summarize the document into 2 sentences
    return ' '.join(str(sentence) for sentence in summary)
