library(readabs)
library(tidyverse)
library(DBI)
library(RMySQL)
library(readxl)

getPastCpi<- function() {
  cpi <- read_abs(series_id="A128478317T")
  cpi <- cpi %>%
    select(date, value)
  return(cpi)
}
getWeights <- function() {
  weights_path <- download_abs_data_cube("annual-weight-update-cpi-and-living-cost-indexes", "consumer")
  weights <- read_excel(weights_path, sheet = 2)
  weights <- weights %>% 
    select(3,6) %>%
    na.omit()
  colnames(weights) <- c("expenditure_class","weights")
  return(weights)
}

update_db <- function(cpi, weights) {
  # Establish a connection
  con <- dbConnect(RMySQL::MySQL(), 
                   host="inflationdb.mysql.database.azure.com", 
                   user="Oakmont", 
                   password="StrattonStonks741", 
                   dbname="testdb")
  
  # Insert the data
  dbWriteTable(con, "abs_inflation", cpi, append=FALSE, overwrite=TRUE, row.names=FALSE)
  dbWriteTable(con, "abs_Weights", weights, append=FALSE, overwrite=TRUE, row.names=FALSE)
  # Close the connection
  dbDisconnect(con)
}

cpi <- getPastCpi()
weights <- getWeights()
update_db(cpi,weights)

