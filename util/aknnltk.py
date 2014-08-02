#! /usr/bin/python3 -uW all
# -*- coding: utf-8 -*-
##
# Corpus reader for Akoma Ntoso documents.
#
# import nltk.text, aknnltk
# t = nltk.text.Text(aknnltk.AKNCorpusReader('/tmp/openlaw-test', '.*\.xml').words('pen.xml'))
# t.plot(20)
#

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus.reader.xmldocs import XMLCorpusReader

class AKNCorpusReader(XMLCorpusReader):
	"""
	Corpus reader for Akoma Ntoso documents.

	"""
	def __init__(self, root, fileids):
		XMLCorpusReader.__init__(self, root, fileids)
	
	def words(self, fileid=None):
		"""
		Returns all of the words and puncuation symbols in the specified file
		that were in '//section//content' text nodes.
		"""
		return [val for subl in [word_tokenize(sent) for sent in self.sents(fileid)] for val in subl]

	def sents(self, fileid=None):
		"""
		Returns all of the sentences in the specified file
		that were in '//section//content' text nodes.
		"""
		return [val for subl in [sent_tokenize(para) for para in self.paras(fileid)] for val in subl]
	
	def paras(self, fileid=None):
		"""
		Returns all of the paragraphs in the specified file
		that were in '//section//content' text nodes.
		"""
		els = self.xml(fileid).iterfind('.//{http://docs.oasis-open.org/legaldocml/ns/akn/3.0/CSD14}section//{http://docs.oasis-open.org/legaldocml/ns/akn/3.0/CSD14}content')
		return [''.join(el.itertext()) for el in els]

