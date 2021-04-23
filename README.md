# WholeHog

WholeHog is a python library for performing text analyis on product reviews from Amazon, app reviews from Apple store, etc. It is built around an interface provided through Dash and Plotly with interactive plots. 

## Installation

Install using setup.py

```bash
python setup.py install --user
```

## Usage

This section covers Amazon and Apple reviews separately.

### Apple App Store Reviews

```python
from wholehog.apple_review import AppReview

ap = AppReview("us", "kardia")
df = ap.get_reviews(num_reviews=20)
ap.generate_embeddings()
ap.cluster_embeddings(num_topics=10)
ap.plot_embeddings(port_num=9050)
```

Open localhost:(port number) to view the Dash interface. Click generate CSV button to obtain topics in the form of a CSV.

