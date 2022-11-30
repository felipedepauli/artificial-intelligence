import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 

def plot(model, df, max_range=11):
    if model == 'KMeans':
        distortions = []
        for i in range(1, max_range):
            km = KMeans(
                n_clusters   = i, 
                init         = 'k-means++', 
                n_init       = 10, 
                max_iter     = 300, 
                random_state = 0
            )
            km.fit(df)
            distortions.append(km.inertia_)
    plt.plot(range(1, max_range), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.tight_layout()
    #plt.savefig('images/11_03.png', dpi=300)
    plt.show()