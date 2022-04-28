from numpy import ones, concatenate

from numpy.random import RandomState

import os

import pandas as pd

import scipy as sp

from limix_core.util.preprocess import gaussianize

from struct_lmm import run_structlmm

from pandas_plink import read_plink

import geno_sugar as gs

from struct_lmm.utils.sugar_utils import norm_env_matrix

from limix.qtl import st_sscan

from struct_lmm import StructLMM

from sklearn.impute import SimpleImputer

import geno_sugar.preprocess as prep

from sklearn.impute import SimpleImputer

import numpy as np

import csv

import sys 


random = RandomState(1)

bedfile = sys.argv[1]

(bim, fam, G) = read_plink(bedfile, verbose=False)

print("finish read bedfile")

 

                

phenofile = sys.argv[2]

pheno = sp.loadtxt(phenofile)

pheno = pheno[:,sp.newaxis]

pheno = gaussianize(pheno)



 
print("finish read phenofile")
 

envfile = sys.argv[3]

E = sp.loadtxt(envfile)

E = norm_env_matrix(E)

print("finish read envfile")
 

covs = sys.argv[4]

covs = sp.loadtxt(covs)

print("finish read covs")


imputer = SimpleImputer(missing_values=sp.nan, strategy="mean")

 

preprocess = prep.compose(

    [

        #prep.filter_by_missing(max_miss=0.10),

        prep.impute(imputer),

        #prep.filter_by_maf(min_maf=0.001),

        prep.standardize(),

    ]

)

res = []

a = []

queue = gs.GenoQueue(G,bim,batch_size=50,preprocess=preprocess)

for _G, _bim in queue:

  r = st_sscan(_G,pheno,E,covs,tests=["inter"],verbose=False)

  res.append(_bim)

  print(r)

  a.append(r)

res = pd.concat(res).reset_index(drop=True)

print(res)

print(a)

aa = pd.DataFrame([res,a],index=False)


aa.to_csv("Results_stlmm.csv",index=False) 
