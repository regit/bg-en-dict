=============================================
Bulgarian - English dictionary in mobi format
=============================================

Introduction
============

This is a set of tools that can be used to to build a
Bulgarian to English dictionary in mobi format. It is
using the data file from BGOffice as a base. Result has
been tested successfully on Kindle.

Integration with Kindle is working correctly for words
as the different forms of the words have been extracted
from wiktionary content.

Download
========

You can download a built version at the following
url: https://home.regit.org/~regit/regit-bg-en.mobi

Motivation
==========

As I was not able to buy a Bulgarian English dictionary that
could be use on a Kindle, I decided to build one using freely
available resources.

Method
======

Start kiwix-server: ::

 bin/kiwix-serve --port=8080 wiktionary_bg_all_nopic_2015-08.zim

Launch conversion script: ::

 ./tab2opf -utf bg-en.csv

Convert opf output to mobi ::

 ./kindlegen  -verbose bg-en.opf

More to come...
