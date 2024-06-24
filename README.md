# PubMed Article Summarizer 
------------------------------------------------------------------------------------------------------------

# Overview:

The PubMed Article Summarizer is a web application built with Flask that allows users to summarize PubMed articles using various algorithms. It provides a simple interface for entering an article, choosing the number of sentences for the summary, and selecting a summarization algorithm.

# Features
Summarization Algorithms: Offers three summarization algorithms:

LSA (Latent Semantic Analysis):
Uses singular value decomposition to analyze relationships between terms and concepts within a document.

LexRank:

Applies graph-based centrality scoring to sentences, similar to Google's PageRank algorithm.

TextRank:

An extractive summarization technique that computes sentence importance based on graph-based ranking.
# Customizable Summary Length:

Users can specify the number of sentences for the summary, providing flexibility in summary length.

# User-Friendly Interface:

Simple and intuitive web interface for entering PubMed article text and viewing the summarized output.
