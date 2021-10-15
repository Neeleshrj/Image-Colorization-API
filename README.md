## <center>Image Colorization API</center>

## Machine Learning Model used-
https://github.com/richzhang/colorization/tree/caffe

#### Paper - https://arxiv.org/abs/1603.08511

#### Steps to run the api locally-
<ol>
    <li>Clone the repository</li>
    <li>Run <code>pip install -r requirements.txt</code></li>
    <li>After successful installation run <code>uvicorn main:app --reload</code> to start the server</li>
    <li>Go to <code>127.0.0.1:8000</code> to check endpoints and <code>127.0.0.1:8000/docs#/</code> to test the endpoints</li>
</ol>