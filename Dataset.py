import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import prince
import matplotlib.pyplot as plt
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

class Dataset():   
    # Constructor
    def __init__ (self, data):
        self.data = data
        
    # Attributes
    def display_data(self):
        return self.data
    
    def get_values(self):
        return self.data.values
                
    def save_data(self, path, name):
        self.data.to_csv(path + '/' + name + '.csv', index = False, header = True)
    
    def isEmpty(self):
        if self.data.empty:
            return True
        else:
            return False
    
    def reduce_PCA(self, components):
        '''
    Function that standardizes data reduces it using Principal Component Analysis
    
    Arguments:
            components (int) - number of components to reduce dataset to
            
    Returns:
            float - return total explained variance rounded to two decimal places
    '''
        # Normalizing the features
        data = StandardScaler().fit_transform(self.data.values)
        
        # Dimensionality Reduction
        pca = PCA(n_components = components)
        trans_data = pca.fit_transform(data)
        variance_ratio = pca.explained_variance_ratio_
        column_names = ['Principal Component {} ({}% explained variance)'.format(i+1, round(variance_ratio[i]*100,2)) for i in range(0, components)]
        self.data = pd.DataFrame(data = trans_data,
                                 columns = column_names)
        
        return round(sum(variance_ratio)*100, 2)
        
    def graph(self, color_by = None, variance = None):
        '''
    Function that creates a matplotlib graph and returns it
    
    Arguments:
            color_by (pd.Series) - indicates what to use to color graph
            
            variance (float) - total variance explained by reduced data
            
    Returns:
            ax - graph figure
    '''
        if variance is None: # Numeric data
            if color_by is None: # Initial Graph
                ax = plt.figure(figsize=(6,5))
                
                plt.scatter(self.data.iloc[:,0], self.data.iloc[:,1])
                plt.xlabel(self.data.columns[0])
                plt.ylabel(self.data.columns[1])
                plt.close()
                
                return ax
            else: # Graph colored by a column
                ax = plt.figure(figsize=(6,5))
                
                plt.scatter(self.data.iloc[:,0], self.data.iloc[:,1], c = color_by, cmap = 'rainbow')
                plt.xlabel(self.data.columns[0])
                plt.ylabel(self.data.columns[1])
                plt.close()
                
                return ax     
        else: # Mixed Data
            if color_by is None: # Initial Graph
                ax = plt.figure(figsize=(6,5))
                
                plt.scatter(self.data.iloc[:,0], self.data.iloc[:,1])
                plt.xlabel('Factor 1 ({}% explained variance)'.format(variance[0]))
                plt.ylabel('Factor 2 ({}% explained variance)'.format(variance[1]))
                plt.close()
                
                return ax
            else: # Graph Colored by a column
                ax = plt.figure(figsize=(6,5))
                
                plt.scatter(self.data.iloc[:,0], self.data.iloc[:,1], c = color_by, cmap = 'rainbow')
                plt.xlabel('Factor 1 ({}% explained variance)'.format(variance[0]))
                plt.ylabel('Factor 2 ({}% explained variance)'.format(variance[1]))
                plt.close()
                
                return ax
                
    def reduce_FA(self, components):
        '''
    Function that reduces data it using Factor Analysis for Mixed Data
    
    Arguments:
            components (int) - number of components to reduce dataset to
            
    Returns:
            percentage_variance = list of explained variance by each component
                
            float - return total explained variance rounded to two decimal places
    '''
        # Dimensionality Reduction
        famd = prince.FAMD(n_components = components,
                           n_iter = 3,
                           random_state = 42
                           )
        
        trans_data = famd.fit_transform(self.data)
        variance = famd.explained_inertia_
        self.data = pd.DataFrame(data = trans_data)
        # Assign variance for each column in reduced data
        percentage_variance = [round(i*100, 2) for i in variance]

        return percentage_variance, round(sum(variance)*100, 2)
        
        
        