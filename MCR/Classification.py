from sklearn import preprocessing
import numpy as np
enc=preprocessing.OneHotEncoder();
print (enc.fit([{"Apple", "Beer", "Rice", "Chicken"},
                          {"Apple", "Beer", "Rice"},
                          {"Apple", "Beer"},
                          {"Apple", "Bananas"},
                          {"Milk", "Beer", "Rice", "Chicken"},
                          {"Milk", "Beer", "Rice"},
                          {"Milk", "Beer"},
                          {"Apple", "Bananas"}]));
print (enc.n_values_)
print (enc.feature_indices_)
