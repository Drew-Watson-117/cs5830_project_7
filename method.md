# Method for Applying SVM to GOES X Ray Flux Dataset

- Started by just throwing the SVM at it
- Results were off, especially trying to predict whether there is a flare or not
- Realized that the dataset only contains data from solar flare events. There are data points corresponding to the beginning, ending, and peak of each event. Only the "peak" data point is associated with a flare class, so the beginning and ending data points just create noise
- Decided to only consider the peak of each solar flare for classification
- Decided not to consider A class flares, as there were only **two** in the data
  
- Plotted on a logscale and looked at decision boundaries
- Standardized the data
- Supplied standardized training data to an SVM model with a RBF kernel.
- Tested model on testing data, plotted confusion matrix
- Noticed most of the errors were coming when trying to classify B and C class flares. 
- Gave B and C classes more weight to try to remedy this problem

- X-class flares affect the Earth most, so we care the most about classifying them