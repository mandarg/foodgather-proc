# probably need a better format for importing this
source("calendarHeat.R")

# read date from the logfile
mealdata <- read.csv(file="kitchenmeallog.csv")
attach(mealdata)

# select only lunches
lunchdata <- mealdata[Meal=='lunch'| Meal=='Lunch',]

# convert dates into POSIX format
posixdates <- as.Date(lunchdata$Date, format="%m/%d/%Y")

# plot the heatmap
calendarHeat(posixdates, lunchdata$Meals_Served, varname="Lunches Served", color="g2r")
