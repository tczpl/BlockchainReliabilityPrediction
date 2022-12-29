# BlockchainReliabilityPrediction
Data and Implementaion of Paper &lt;Selecting Reliable Blockchain Peers via Hybrid Blockchain Reliability Prediction>

Blockchain and blockchain-based decentralized applications are attracting increasing attentions recently. In public blockchain systems, users usually connect to third-party peers or run a peer to join the P2P blockchain network. However, connecting to unreliable blockchain peers will make users waste resources and even lose millions of dollars of cryptocurrencies. In order to select the reliable blockchain peers, it is urgently needed to evaluate and predict the reliability of them. Faced with this problem, we propose H-BRP, Hybrid Blockchain Reliability Prediction model to extract the blockchain reliability factors then make personalized prediction for each user. Large-scale real-world experiments are conducted on 100 blockchain requesters and 200 blockchain peers. The implement and dataset of 2,000,000 test cases are released. The experimental results show that the proposed model obtains better accuracy than other approaches.

## Instruction
Use following 3 lines for quick running (on Ubuntu 20.04):

`git clone https://github.com/InPlusLab/BlockchainReliabilityPrediction.git`

`pip3 install pandas scipy xgboost`

`python3 run.py`

Then you can check the result from the `result` directory.


## Source Data


As for the source data, plase check the `data_source` directory.

As for the processing codes of the source data, plase check the `data_process` directory.

And then, you can run the `python3 generateMatrix.py` to generate the mentioned matrices in the paper.


