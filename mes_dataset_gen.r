library(tidyverse)

header <- c('chrom','chromStart', 'chromEnd', 'name', 'score', 'strand', 'thickStart', 'thickEnd', 'itemRgb', 'blockCount', 'blockSizes', 'blockStarts')

dat = read.csv(
  "/home/vinicius/Downloads/GRCh38_gencode_v28.bed",
  sep = "\t",
  header=F,
  stringsAsFactors = F
)

colnames(dat) <- header

data.frame(dat$blockSizes, lapply(dat$blockSizes, blocksSize))

dat$blockSizes = lapply(strsplit(dat$blockSizes,"\\,"),as.integer)
dat$blockSizes 
