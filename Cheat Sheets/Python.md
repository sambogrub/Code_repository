# Python
 The Python language and it's libraries
 
## Python basics
 - use context managers! with()
 - lambda is a single line, one-off function. 
   - lambda x: x+2 will give the result of whatever you put in plus 2.
   - can be used with dataframes like .apply(lambda row: row.sum(), axis =1), where axis =1 means itterate over the rows
 - map() => map(function,iterable)
 - match statements
   - variable = 'value'
   - match variable:
     - case 'value':
       - do something
     - case 'value2':
       - do something else
     - case default:
       - do something when nothing matches
 - using _variable with the underscore allows the use of a setter method. it allows you to assign a value to the variable and the class object will run the corrisponding function.
 - list comprehension, making a list from another action. list = [operation for value in list]
   - can be used with zip => dict = {x: y for x,y in zip(listx,listy)}
 - slices
   - [first: last(not inclusive): steps]
## Datetime
 - date.today() - returns current local date

## Random
 - random.shuffle, rearranges items in a mutable object like a list

## Decimal
 - Decimal('some number') keeps it at the decimal points you set

## Tkinter
 - .place(anchor, x coor, y coor, height, width) all in pixels, can be relative using rel*. anchor is default NW
 - .resizable(width = True/False, height = True/False)
 - .tkraise() brings the widget to the front

## Pandas
 - pd.melt(frame, id_vars, value_vars, var_name, value_name, col_level, ignore_index) 
   - id_vars - columns that will stay the same
   - value_vars - columns to unpivot
   - var_name - new column name that will store original column names
   - value_name - new column that stores values from original columns
 - contingency table - pd.crosstab(x,y)
 - pd.get_dummies(df[columns], drop_first = True)
   - creates a df with given columns and fills in dummy variables
   - drop_first = True, drops the first category to help with regression models
   - 
  
## numpy
 - np.mean() gives mean/average of list/array
 - np.std() gives standard deviation of list/array
 - np.max() give max value
 - np.min() gives min value
 - np.array() sets list into a numpy array
 - .reshape(-1,1) -1 is to have numpy arrange number of rows, 1 is number of columns
 - 

## Matplotlib
 - plt.hist() plots a histogram
   - use bins = some_value to set the intervals by which the data is devided
 - plt.show() to show the current plot
 - plt.close() to close the current plot, allowing you to build and show a new one without interference

## Seaborn
 - df.corr(), correlation matrix of the dataframe


## Scipy
 - ttest_ind - two sample t-test (tstat, pval = ttest_ind(samp1,samp2))
 - ttest_1samp - one sample t-test (tstat, pval = ttest_1samp(popsample, popmean))
 - .stats => chi2, pval, dof, expected = chi2_contingency(contingency table) 

## statsmodels
 - pairwise_tukeyhsd - used to compare multiple groups and their dependent variables
   - example: stores A, B, C and their sales
   - results = pairwise_tukeyhsd(dependant variables, groups, type 1 error rate)

## Scikit_learn
 - __Linear regression__
   - from sklearn.linear_model import LinearRegression
   - your_model = LinearRegression()
   - your_model.fit(x_training_data, y_training_data)
     - .coef_ contains the coefficients
     - .intercept_ contains the intercept
   - predictions = your_model.predict(your_x_data)
     - .score() returns the coefficient of the determination R^2
 - __Naive Bayes__
   - from sklearn.naive_bayes import MultinomialNB
   - your_model = MultinomialNB()
   - your_model.fit(x_training_data, y_training_data)
   - //Returns a list of predicted classes - one prediction for every data point
   - predictions = your_model.predict(your_x_data)
   - //For every data point, returns a list of probabilities of each class
   - probabilites = your_model.predict_proba(your_x_data)
 - __K-Nearest Neightbors__
   - from sklearn.Neightbors import KNeighborsClassifier
   - your_model = KNeighborsClassifier
   - your_model.fit(x_training_data, y_training_data)
   - //Returns a list of predicted classes - one prediction for every data point
   - predictions = your_model.predict(your_x_data)
   - //For every data point, returns a list of probabilities of each class
   - probabilites = your_model.predict_proba(your_x_data)
 - __K-Means__
   - from sklearn.cluster imort KMeans
   - your_model= KMeans(n_clusters=4, init='random')
     - n_clusters - number of clusters to form and number of centroids to generate
     - init - method for initialization
       - k-means++ - K-Means++ (default)
       - random - K-Means
     - random_state - the seed used by the random number generation (optional)
   - your_model.fit(x_training_data)
   - predictions = your_model.predict(your_x_data)
 - __Validating the Model__
   - __accuracy, recall, precision, and F1 score__
   - from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
   - print(accuracy_score(true_labels, guesses))
   - print(recall_score(true_labels, guesses))
   - print(precision_score(true_labels, guesses))
   - print(f1_score(true_labels, guesses))
   - __confusion matrix__
   - from sklearn.metrics import confusion_matrix
   - print(confusion_matrix(true_labels, guesses))
 - __Training sets and test sets__
   - from sklearn.model_selection import train_test_split
   - x_train, x_test, y_train, y_test = train_test_split(x,y,train_size = 0.8, test_size = 0.2)
     - train_size - the proportion of the dataset to include in the train split
     - test_size - the proportion of the dataset to include in the test split
     - random_state - the see used by the random number generator (optional)

## sklearn
 - .preprocessing
   - StandardScaler - transforms a dataset feature, standardizing it
     - use scaler = StandardScaler to instantiate it
     - .fit_transform() takes a one column array and standardizes it
   - MinMaxScaler
     - use mmscaler = MinMaxScaler() to instantiate it
     - .fit_transform() take a one column array and standardizes it
 - .neighbors
   - KNeighborsClassifier - uses neighbors around an unknow to classify based on training data
     - takes an n_neighbors attribute when instantiated
     - .fit(training_points,training_labels) trains the classifier on the given data 
     - .predict(list_of_points) takes a list of the points you want to classify then returns a list of those classifications