train_dev <- read.csv("D:/rawDataFiles/housePrice_train.csv",header=T)
test <- read.csv("D:/rawDataFiles/housePrice_test.csv",header=T)


train_dev$Alley <- as.character(train_dev$Alley)
train_dev$Alley[is.na(train_dev$Alley)] <- 'NoAlley'
train_dev$Alley <- as.factor(train_dev$Alley)

train_dev$BsmtQual <- as.character(train_dev$BsmtQual)
train_dev$BsmtQual[is.na(train_dev$BsmtQual)] <- 'NoBsmt'
train_dev$BsmtQual <- as.factor(train_dev$BsmtQual)

train_dev$BsmtCond <- as.character(train_dev$BsmtCond)
train_dev$BsmtCond[is.na(train_dev$BsmtCond)] <- 'NoBsmt'
train_dev$BsmtCond <- as.factor(train_dev$BsmtCond)

train_dev$BsmtExposure <- as.character(train_dev$BsmtExposure)
train_dev$BsmtExposure[is.na(train_dev$BsmtExposure)] <- 'NoBsmt'
train_dev$BsmtExposure <- as.factor(train_dev$BsmtExposure)

train_dev$BsmtFinType1 <- as.character(train_dev$BsmtFinType1)
train_dev$BsmtFinType1[is.na(train_dev$BsmtFinType1)] <- 'NoBsmt'
train_dev$BsmtFinType1 <- as.factor(train_dev$BsmtFinType1)

train_dev$BsmtFinType2 <- as.character(train_dev$BsmtFinType2)
train_dev$BsmtFinType2[is.na(train_dev$BsmtFinType2)] <- 'NoBsmt'
train_dev$BsmtFinType2 <- as.factor(train_dev$BsmtFinType2)

train_dev$FireplaceQu <- as.character(train_dev$FireplaceQu)
train_dev$FireplaceQu[is.na(train_dev$FireplaceQu)] <- 'NoFireplace'
train_dev$FireplaceQu <- as.factor(train_dev$FireplaceQu)

train_dev$GarageType <- as.character(train_dev$GarageType)
train_dev$GarageType[is.na(train_dev$GarageType)] <- 'NoGarage'
train_dev$GarageType <- as.factor(train_dev$GarageType)

train_dev$GarageFinish <- as.character(train_dev$GarageFinish)
train_dev$GarageFinish[is.na(train_dev$GarageFinish)] <- 'NoGarage'
train_dev$GarageFinish <- as.factor(train_dev$GarageFinish)

train_dev$GarageQual <- as.character(train_dev$GarageQual)
train_dev$GarageQual[is.na(train_dev$GarageQual)] <- 'NoGarage'
train_dev$GarageQual <- as.factor(train_dev$GarageQual)

train_dev$GarageCond <- as.character(train_dev$GarageCond)
train_dev$GarageCond[is.na(train_dev$GarageCond)] <- 'NoGarage'
train_dev$GarageCond <- as.factor(train_dev$GarageCond)

train_dev$PoolQC <- as.character(train_dev$PoolQC)
train_dev$PoolQC[is.na(train_dev$PoolQC)] <- 'NoPool'
train_dev$PoolQC <- as.factor(train_dev$PoolQC)

train_dev$Fence <- as.character(train_dev$Fence)
train_dev$Fence[is.na(train_dev$Fence)] <- 'NoFence'
train_dev$Fence <- as.factor(train_dev$Fence)

train_dev$MiscFeature <- as.character(train_dev$MiscFeature)
train_dev$MiscFeature[is.na(train_dev$MiscFeature)] <- 'None'
train_dev$MiscFeature <- as.factor(train_dev$MiscFeature)



plot(train_dev$LotFrontage, train_dev$LotArea)
plot(train_dev$LotFrontage**2, train_dev$LotArea)
plot(train_dev$LotFrontage, train_dev$GrLivArea)



plot(train_dev$MSZoning)
plot(train_dev$LotFrontage)
plot(train_dev$Neighborhood, train_dev$LotFrontage,
     main='Neighborhood & LotFrontage plot')
plot(train_dev$Utilities)
plot(train_dev$Exterior1st)
plot(train_dev$MasVnrType)
plot(train_dev$MasVnrArea)
plot(train_dev$BsmtFinSF1)
plot(train_dev$BsmtFinSF2)
plot(train_dev$BsmtUnfSF)
plot(test$BsmtUnfSF)
plot(train_dev$TotalBsmtSF)
plot(test$TotalBsmtSF)
plot(train_dev$BsmtFullBath)
plot(train_dev$BsmtHalfBath)
plot(train_dev$KitchenQual)
plot(test$KitchenQual)
plot(train_dev$Functional)
plot(train_dev$GarageType)
plot(train_dev$GarageYrBlt)
plot(train_dev$GarageType, train_dev$GarageYrBlt)
plot(train_dev$GarageCars)
plot(train_dev$GarageType, train_dev$GarageCars)
plot(train_dev$GarageArea)
plot(train_dev$GarageType, train_dev$GarageArea)
plot(train_dev$SaleType)
plot(train_dev$Electrical)
