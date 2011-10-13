# -*- coding: utf-8 -*-
from hip2unicode.tools import corpus_converter
from hip2unicode.functions import all_hip_conversions as ahc
from hip2unicode.functions import compile_conversion as cc
from hip2unicode.conversions import hip_civilrus

# def corpus_converter(path=None, corpus_folder='corpus', converted_corpus_folder='converted_corpus', conversions=None):

corpus_converter.corpus_converter(
    converted_corpus_folder = 'corpus-civilrus',
    conversions             =  ahc(
                                    slav=cc(hip_civilrus.conversion),
                                    rus='delete',
                                    lat='delete',
                                    grec='delete',
                                  ),
    )
