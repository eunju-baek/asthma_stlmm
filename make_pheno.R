#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)
action = args[1]
pheno = args[-1]

pheno <- read.table(pheno,sep="\t",header=T)
if(action == "--pheno"){
        stph <- pheno[,3]
        stph <- data.frame(stph)
        write.table(stph,paste("pheno_",names(pheno)[19],".txt",sep=""),col.names=F,sep='\t',row.names=F)
}else if(action == "--cov"){
        stcov <- pheno[,4:20]
        stcov <- data.frame(stcov)
        write.table(stcov,paste("cov_",names(pheno)[19],".txt",sep=""),col.names=F,sep='\t',row.names=F)
}else if(action == "--env"){
        stenv <- pheno[,19]
        stenv <- data.frame(stenv)
        write.table(stenv,paste("env_",names(pheno)[19],".txt",sep=""),col.names=F,sep='\t',row.names=F)
}
