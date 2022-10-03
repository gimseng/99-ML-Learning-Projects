### LIBRARY CALL ###
library("rpart")
library("rpart.plot")	
#library("rattle")

#######################################################################################################

### READING DATA ###
train <- read.csv("../input/train.csv")
test  <- read.csv("../input/test.csv")
test$Survived <- 0

#######################################################################################################

### CLEANING DATA ###
combi <- rbind(train, test)
combi$Name <- as.character(combi$Name)
strsplit(combi$Name[1], split='[,.]')
strsplit(combi$Name[1], split='[,.]')[[1]]
strsplit(combi$Name[1], split='[,.]')[[1]][2]
combi$Title <- sapply(combi$Name, FUN=function(x) {strsplit(x, split='[,.]')[[1]][2]})
combi$Title <- sub(' ', '', combi$Title)
combi$Title[combi$PassengerId == 797] <- 'Mrs' # female doctor
combi$Title[combi$Title %in% c('Lady', 'the Countess', 'Mlle', 'Mee', 'Ms')] <- 'Miss'
combi$Title[combi$Title %in% c('Capt', 'Don', 'Major', 'Sir', 'Col', 'Jonkheer', 'Rev', 'Dr', 'Master')] <- 'Mr'
combi$Title[combi$Title %in% c('Dona')] <- 'Mrs'
combi$Title <- factor(combi$Title)

# Passenger on row 62 and 830 do not have a value for embarkment. 
# Since many passengers embarked at Southampton, we give them the value S.
# We code all embarkment codes as factors.
combi$Embarked[c(62,830)] = "S"
combi$Embarked <- factor(combi$Embarked)

# Passenger on row 1044 has an NA Fare value. Let's replace it with the median fare value.
combi$Fare[1044] <- median(combi$Fare, na.rm=TRUE)

# Create new column -> family_size
combi$family_size <- combi$SibSp + combi$Parch + 1


# How to fill in missing Age values?
# We make a prediction of a passengers Age using the other variables and a decision tree model. 
# This time you give method="anova" since you are predicting a continuous variable.

predicted_age <- rpart(Age ~ Pclass + Sex + SibSp + Parch + Fare + Embarked + Title + family_size,
                       data=combi[!is.na(combi$Age),], method="anova")
combi$Age[is.na(combi$Age)] <- predict(predicted_age, combi[is.na(combi$Age),])


#######################################################################################################

### CREATING MODEL ###
train_new <- combi[1:891,]
test_new <- combi[892:1309,]
test_new$Survived <- NULL

# Find Cabin Class 
train_new$Cabin <- substr(train_new$Cabin,1,1)
train_new$Cabin[train_new$Cabin == ""] <- "H"
train_new$Cabin[train_new$Cabin == "T"] <- "H"

test_new$Cabin <- substr(test_new$Cabin,1,1)
test_new$Cabin[test_new$Cabin == ""] <- "H"

train_new$Cabin <- factor(train_new$Cabin)
test_new$Cabin <- factor(test_new$Cabin)

# train_new and test_new are available in the workspace
str(train_new)
str(test_new)

# Create a new model `my_tree`
my_tree <- rpart(Survived ~ Age + Sex + Pclass  + family_size, data = train_new, method = "class", control=rpart.control(cp=0.0001))
#my_tree <- rpart(Survived ~ Pclass + Sex + Fare  + family_size, data = train_new, method = "class", control=rpart.control(cp=0.0001))
#my_tree <- rpart(Survived ~ Pclass + Sex + SibSp + Parch + Fare + Embarked + Title + family_size, data = train_new, method = "class", control=rpart.control(cp=0.0001))
# Cabin - family_size ???
summary(my_tree)

# Visualize your new decision tree
#fancyRpartPlot(my_tree)
prp(my_tree, type = 4, extra = 100)

# Make your prediction using `my_tree` and `test_new`
my_prediction <- predict(my_tree, test_new, type = "class")
head(my_prediction)

# Create a data frame with two columns: PassengerId & Survived. Survived contains your predictions
vector_passengerid <- test_new$PassengerId

my_solution <- data.frame(PassengerId = vector_passengerid, Survived = my_prediction)

head(my_solution)

# Write your solution to a csv file with the name my_solution.csv
write.csv(my_solution, file = "my_solution.csv",row.names=FALSE)