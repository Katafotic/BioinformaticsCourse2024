# install.packages("stringr")
# install.packages("purrr")
library("stringr", "purrr")

data <- readLines(con = "stdin")

count_nucl <- function(dna){
    c(str_count(dna, "A"), str_count(dna, "C"), str_count(dna, "G"), str_count(dna, "T"))
}

count <- purrr::map(data, count_nucl)
print(count)