library(readabs)
library(tidyverse)
library(DBI)
library(RMariaDB)
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
  weights$weights <- weights$weights / 100  # This line is added to divide weights by 100
  return(weights)
}

update_db <- function(cpi, weights) {
  # Establish a connection
  con <- dbConnect(RMariaDB::MariaDB(), 
                   host="inflationdb.mysql.database.azure.com", 
                   user="Oakmont", 
                   password="StrattonStonks741", 
                   dbname="oakmont_padb")
  
  # Insert the data
  dbWriteTable(con, "abs_inflation", cpi, append=FALSE, overwrite=TRUE, row.names=FALSE)
  #dbSendStatement(con, "UPDATE abs_inflation SET date = STR_TO_DATE(date, '%YYYY-%mm-%dd')")
  dbWriteTable(con, "abs_weights", weights, append=FALSE, overwrite=TRUE, row.names=FALSE)
  # Close the connection
  dbDisconnect(con)
}

cpi <- getPastCpi()
weights <- getWeights()
update_db(cpi,weights)

