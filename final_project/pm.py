def predict(tag, c, array, result_queue):
    # Get the probability for the classifier
    Prob = c.predict_proba(array)[0][1]
    result_queue.put((tag, Prob))
    
    
def predict_pool(tag, c, array):
    # Get the probability for the classifier
    Prob = c.predict_proba(array)[0][1]
    return (tag, Prob)