#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import chdir
import os.path
# import rpy2.robjects as R
from sys import argv
import shutil
from glob import glob
# from subprocess import call


def Resid(filename):
    o = open(filename, 'r')
    resid = o.read().split()
    o.close()
    return resid


conf = os.path.abspath('.').split('/')[-2]
a = os.path.abspath('.').split('/')
del a[-1]
root_dir = os.path.join('/', *a)
print root_dir
script, first_argv = argv
resid_list = Resid(first_argv)
working_path = os.path.dirname(os.path.abspath(__file__))
print type(working_path)
print working_path


def substring(mystr, mylist):
    return [i for i, val in enumerate(mylist) if mystr in val]


def replaceLine(search, replace, myfile):
    f = open(myfile, "r")
    contents = f.readlines()
    f.close()

    contents[substring(search, contents)[0]] = replace

    f = open(myfile, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def get_Header(resid):
    global header
    global working_path
    f = open(resid + '/energy.xvg', 'r')
    contents = f.readlines()
    f.close()
    header = '\ttime\tLJ14\tCoulomb14\tLJSR\tCoulombSR\tCoulombReciprocal\t\
        Potential\tKineticEnergy\tTotalEnergy\tCoulSRresRNA\t\
        LJSRresRNA\tCoul14resRNA\tLJ14resRNA\n'
    a = []
    for i in range(len(contents)):
        if contents[i].find('@') == 0 or contents[i].find('#') == 0:
            a.append(i)
    contents[a[0]] = header
    for i in range(1, len(a)):
        if contents[i].find('@') == 0 or contents[i].find('#') == 0:
            contents[a[i]] = ''
    print working_path + '/' + resid + '.dat'
    f = open(working_path + '/plot_potential/' + resid + '.dat', 'w')
    contents = "".join(contents)
    f.write(contents)
    f.close()

class mod_file(object):
    """calculate average potential and error of a residue and dsRNA"""
    def __init__(self, resid):
        self.resid = resid

    header = [' time', ' LJ14', ' Coulomb14', ' LJSR', ' CoulombSR',
              ' Coulrecip', ' Potential', ' KineticEn', ' TotalEnergy',
              ' CoulSRresidRNA', ' LJSRresidRNA', ' Coul14residRNA',
              ' LJ14residRNA']
    # chdir(resid)
    def substring(self, mystr, mylist):
        return [i for i, val in enumerate(mylist) if mystr in val]
    def searchLineIndex(search, myfile):
        f = open(myfile, "r")
        contents = f.readlines()
        f.close()
        string = []
        for i in range(len(contents)):
            if substring(search, contents[i]):
                string.append(i)
        return string
        # if len(substring(search,contents)) > 0:
        #     return contents[substring(search,contents)[0]]
        # else:
        #     return ''
    def replaceLine(self, search, replace, myfile):
        f = open(myfile, "r")
        contents = f.readlines()
        f.close()
        contents[substring(search, contents)[0]] = replace
        f = open(myfile, "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()
    def get_Header(resid):
        global header
        global working_path
        f = open(resid + '/energy.xvg', 'r')
        contents = f.readlines()
        f.close()
        header = '\ttime\tLJ14\tCoulomb14\tLJSR\tCoulombSR\tCoulombReciprocal\t\
            Potential\tKineticEnergy\tTotalEnergy\tCoulSRresRNA\t\
            LJSRresRNA\tCoul14resRNA\tLJ14resRNA\n'
        a = []
        for i in range(len(contents)):
            if contents[i].find('@') == 0 or contents[i].find('#') == 0:
                a.append(i)
        contents[a[0]] = header
        for i in range(1, len(a)):
            if contents[i].find('@') == 0 or contents[i].find('#') == 0:
                contents[a[i]] = ''
        print working_path + '/' + resid + '.dat'
        f = open(working_path + '/' + resid + '.dat', 'w')
        contents = "".join(contents)
        f.write(contents)
        f.close()


class calculate(mod_file):
    def average(self, resid):
        chdir(self.resid)
        # R("k = read.table('" + resid + ".dat', header=T)")
        # return R("mean(read.table('" + resid + ".dat', header=T)$time)")
        pass


k = []
for i in range(len(resid_list)):
    #k = calculate(str(resid_list[i]))#
    get_Header(resid_list[i])
    #print k.average(resid_list[i])#

#for i in glob('*/*.dat'):#
    #print working_path + '/plot_potential/'#
    #shutil.copyfile(i, working_path + '/plot_potential/')#
