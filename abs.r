library(readabs)
library(tidyverse)
library(dplyr)
library(knitr)
library(kableExtra)
cpi <- read_abs(series_id="A128478317T")
cpi <- cpi %>%
  select(date, value)
View(cpi) 